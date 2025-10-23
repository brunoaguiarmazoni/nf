from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import logging
from .web_automation import BaseWebAutomation


class NFEValidator(BaseWebAutomation):
    """
    Classe para validar chaves de NF-e no site da Receita Federal
    """
    
    def __init__(self, headless: bool = True):
        super().__init__(headless=headless)
        self.logger = logging.getLogger(__name__)
        self.base_url = "https://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx"
        
    def validate_nfe_key(self, nfe_key: str) -> dict:
        """
        Valida uma chave de NF-e no site da Receita Federal
        
        Args:
            nfe_key: Chave de acesso da NF-e (44 dígitos)
            
        Returns:
            Dicionário com resultado da validação
        """
        result = {
            'status': 'ERRO',
            'found': False,
            'details': '',
            'error_message': ''
        }
        
        try:
            if not self.driver:
                self.setup_driver()
            
            # Limpa a chave (remove espaços e caracteres especiais)
            clean_key = ''.join(filter(str.isdigit, str(nfe_key)))
            
            if len(clean_key) != 44:
                result['error_message'] = f"Chave inválida: deve ter 44 dígitos (encontrados: {len(clean_key)})"
                return result
            
            self.logger.info(f"Validando chave NF-e: {clean_key}")
            
            # Acessa a página de consulta
            self.driver.get(self.base_url)
            time.sleep(2)
            
            # Aguarda carregamento da página
            if not self.wait_for_element(By.ID, "ctl00_ContentPlaceHolder1_txtChaveAcesso"):
                result['error_message'] = "Página de consulta não carregou corretamente"
                return result
            
            # Preenche a chave de acesso
            if not self.fill_input(By.ID, "ctl00_ContentPlaceHolder1_txtChaveAcesso", clean_key):
                result['error_message'] = "Erro ao preencher chave de acesso"
                return result
            
            # Verifica e lida com CAPTCHA
            self.handle_captcha_if_present()
            
            # Tenta diferentes seletores para o botão de consulta
            button_selectors = [
                "ctl00_ContentPlaceHolder1_btnConsultar",
                "ctl00$ContentPlaceHolder1$btnConsultar",
                "//input[@value='Consultar']",
                "//button[contains(text(), 'Consultar')]"
            ]
            
            button_clicked = False
            for selector in button_selectors:
                try:
                    if selector.startswith("//"):
                        if self.click_element(By.XPATH, selector):
                            button_clicked = True
                            break
                    else:
                        if self.click_element(By.ID, selector):
                            button_clicked = True
                            break
                except:
                    continue
            
            if not button_clicked:
                result['error_message'] = "Botão de consulta não encontrado"
                return result
            
            # Aguarda resultado da consulta
            time.sleep(3)
            
            # Verifica se a NF-e foi encontrada
            success_indicators = [
                "//span[contains(text(), 'Autorizado o uso da NF-e')]",
                "//td[contains(text(), 'Autorizado')]",
                "//div[contains(@class, 'success')]",
                "//*[contains(text(), 'autorizada')]"
            ]
            
            error_indicators = [
                "//span[contains(text(), 'não encontrada')]",
                "//span[contains(text(), 'Rejeição')]",
                "//td[contains(text(), 'não encontrada')]",
                "//*[contains(text(), 'inexistente')]",
                "//*[contains(text(), 'inválida')]"
            ]
            
            # Procura por indicadores de sucesso
            for indicator in success_indicators:
                try:
                    elements = self.driver.find_elements(By.XPATH, indicator)
                    if elements:
                        result['status'] = 'ENCONTRADO'
                        result['found'] = True
                        result['details'] = elements[0].text
                        self.logger.info(f"NF-e encontrada: {clean_key}")
                        return result
                except:
                    continue
            
            # Procura por indicadores de erro/não encontrada
            for indicator in error_indicators:
                try:
                    elements = self.driver.find_elements(By.XPATH, indicator)
                    if elements:
                        result['status'] = 'NAO_ENCONTRADO'
                        result['found'] = False
                        result['details'] = elements[0].text
                        self.logger.info(f"NF-e não encontrada: {clean_key}")
                        return result
                except:
                    continue
            
            # Se chegou até aqui, tenta capturar qualquer mensagem na página
            try:
                page_text = self.driver.find_element(By.TAG_NAME, "body").text
                if "autorizado" in page_text.lower():
                    result['status'] = 'ENCONTRADO'
                    result['found'] = True
                    result['details'] = "NF-e autorizada (detectado no texto da página)"
                elif "não encontrada" in page_text.lower() or "inexistente" in page_text.lower():
                    result['status'] = 'NAO_ENCONTRADO'
                    result['found'] = False
                    result['details'] = "NF-e não encontrada (detectado no texto da página)"
                else:
                    result['error_message'] = "Resultado da consulta não foi identificado"
            except:
                result['error_message'] = "Erro ao analisar resultado da consulta"
            
        except Exception as e:
            result['error_message'] = f"Erro durante validação: {str(e)}"
            self.logger.error(f"Erro ao validar NF-e {nfe_key}: {str(e)}")
        
        return result
    
    def validate_multiple_keys(self, keys: list) -> list:
        """
        Valida múltiplas chaves de NF-e
        
        Args:
            keys: Lista de chaves para validar
            
        Returns:
            Lista com resultados das validações
        """
        results = []
        
        try:
            for i, key in enumerate(keys):
                self.logger.info(f"Validando chave {i+1}/{len(keys)}")
                result = self.validate_nfe_key(key)
                results.append(result)
                
                # Pausa entre consultas para evitar bloqueios
                if i < len(keys) - 1:
                    time.sleep(2)
                    
        except Exception as e:
            self.logger.error(f"Erro durante validação múltipla: {str(e)}")
        
        finally:
            self.close_driver()
        
        return results