from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import logging
import requests
from .web_automation import BaseWebAutomation


class NFSEValidator(BaseWebAutomation):
    """
    Classe para validar chaves de NFS-e em sites de prefeituras
    """
    
    def __init__(self, headless: bool = True):
        super().__init__(headless=headless)
        self.logger = logging.getLogger(__name__)
        
        # Mapeamento de sites de prefeituras (pode ser expandido)
        self.city_urls = {
            'sao_paulo': {
                'url': 'https://nfse.prefeitura.sp.gov.br/contribuinte/consultaNota.aspx',
                'type': 'selenium'
            },
            'rio_de_janeiro': {
                'url': 'https://notacarioca.rio.gov.br/contribuinte/consultaNota.aspx',
                'type': 'selenium'
            },
            'belo_horizonte': {
                'url': 'https://bhissdigital.pbh.gov.br/nfse/pages/consultarNota.jsf',
                'type': 'selenium'
            },
            'brasilia': {
                'url': 'https://www.nfse.df.gov.br/consulta/ConsultarNota.aspx',
                'type': 'selenium'
            }
        }
    
    def detect_city_from_key(self, nfse_key: str) -> str:
        """
        Tenta detectar a cidade baseado na chave NFS-e
        (Implementação básica - pode ser aprimorada)
        
        Args:
            nfse_key: Chave da NFS-e
            
        Returns:
            Nome da cidade ou 'unknown'
        """
        # Esta é uma implementação simplificada
        # Na prática, seria necessário conhecer os padrões específicos de cada prefeitura
        key_patterns = {
            'sao_paulo': ['11', '35'],  # Códigos que podem indicar São Paulo
            'rio_de_janeiro': ['21', '33'],  # Códigos do Rio de Janeiro
            'belo_horizonte': ['31'],  # Código de Belo Horizonte
            'brasilia': ['53']  # Código de Brasília
        }
        
        clean_key = ''.join(filter(str.isdigit, str(nfse_key)))
        
        if len(clean_key) >= 2:
            prefix = clean_key[:2]
            for city, patterns in key_patterns.items():
                if prefix in patterns:
                    return city
        
        return 'unknown'
    
    def validate_nfse_sao_paulo(self, nfse_key: str) -> dict:
        """
        Valida NFS-e específica para São Paulo
        
        Args:
            nfse_key: Chave de acesso da NFS-e
            
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
            
            url = self.city_urls['sao_paulo']['url']
            self.driver.get(url)
            time.sleep(3)
            
            # Implementação específica para São Paulo
            # (Os seletores podem mudar - seria necessário verificar o site atual)
            
            # Exemplo genérico de campos que podem existir
            possible_selectors = [
                "txtNumeroNota",
                "txtChaveAcesso", 
                "txtCodVerificacao",
                "//input[@placeholder='Número da Nota']",
                "//input[contains(@name, 'numero')]"
            ]
            
            filled = False
            for selector in possible_selectors:
                try:
                    if selector.startswith("//"):
                        if self.fill_input(By.XPATH, selector, nfse_key):
                            filled = True
                            break
                    else:
                        if self.fill_input(By.ID, selector, nfse_key):
                            filled = True
                            break
                except:
                    continue
            
            if not filled:
                result['error_message'] = "Campo de entrada não encontrado"
                return result
            
            # Procura botão de consulta
            button_selectors = [
                "//input[@value='Consultar']",
                "//button[contains(text(), 'Consultar')]",
                "//input[@type='submit']"
            ]
            
            for selector in button_selectors:
                if self.click_element(By.XPATH, selector):
                    break
            
            time.sleep(3)
            
            # Verifica resultado
            if self._check_nfse_result():
                result['status'] = 'ENCONTRADO'
                result['found'] = True
                result['details'] = "NFS-e encontrada"
            else:
                result['status'] = 'NAO_ENCONTRADO'
                result['found'] = False
                result['details'] = "NFS-e não encontrada"
                
        except Exception as e:
            result['error_message'] = f"Erro durante validação: {str(e)}"
            self.logger.error(f"Erro ao validar NFS-e São Paulo: {str(e)}")
        
        return result
    
    def validate_nfse_generic(self, nfse_key: str, city_config: dict) -> dict:
        """
        Validação genérica para NFS-e
        
        Args:
            nfse_key: Chave da NFS-e
            city_config: Configuração da cidade
            
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
            
            self.driver.get(city_config['url'])
            time.sleep(3)
            
            # Tenta encontrar campo de input genérico
            input_selectors = [
                "//input[@type='text']",
                "//input[contains(@placeholder, 'número')]",
                "//input[contains(@name, 'numero')]",
                "//input[contains(@id, 'numero')]",
                "//input[contains(@name, 'chave')]"
            ]
            
            filled = False
            for selector in input_selectors:
                if self.fill_input(By.XPATH, selector, nfse_key):
                    filled = True
                    break
            
            if not filled:
                result['error_message'] = "Campo de entrada não encontrado"
                return result
            
            # Procura botão genérico
            if self.click_element(By.XPATH, "//input[@type='submit'] | //button[contains(text(), 'Consultar')]"):
                time.sleep(3)
                
                if self._check_nfse_result():
                    result['status'] = 'ENCONTRADO'
                    result['found'] = True
                else:
                    result['status'] = 'NAO_ENCONTRADO'
                    result['found'] = False
            else:
                result['error_message'] = "Botão de consulta não encontrado"
                
        except Exception as e:
            result['error_message'] = f"Erro durante validação: {str(e)}"
        
        return result
    
    def _check_nfse_result(self) -> bool:
        """
        Verifica se a NFS-e foi encontrada na página de resultado
        
        Returns:
            True se encontrada
        """
        success_indicators = [
            "//*[contains(text(), 'encontrada')]",
            "//*[contains(text(), 'válida')]",
            "//*[contains(text(), 'autorizada')]",
            "//table//td",  # Tabela com dados da nota
            "//*[contains(@class, 'success')]"
        ]
        
        error_indicators = [
            "//*[contains(text(), 'não encontrada')]",
            "//*[contains(text(), 'inválida')]",
            "//*[contains(text(), 'inexistente')]",
            "//*[contains(@class, 'error')]"
        ]
        
        # Verifica indicadores de sucesso primeiro
        for indicator in success_indicators:
            try:
                elements = self.driver.find_elements(By.XPATH, indicator)
                if elements and any(elem.is_displayed() for elem in elements):
                    return True
            except:
                continue
        
        # Se não encontrou sucesso, verifica se há erro explícito
        for indicator in error_indicators:
            try:
                elements = self.driver.find_elements(By.XPATH, indicator)
                if elements and any(elem.is_displayed() for elem in elements):
                    return False
            except:
                continue
        
        return False
    
    def validate_nfse_key(self, nfse_key: str, city: str = None) -> dict:
        """
        Valida uma chave de NFS-e
        
        Args:
            nfse_key: Chave da NFS-e
            city: Cidade específica (opcional)
            
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
            # Se cidade não especificada, tenta detectar
            if not city:
                city = self.detect_city_from_key(nfse_key)
            
            # Validação específica por cidade
            if city == 'sao_paulo':
                result = self.validate_nfse_sao_paulo(nfse_key)
            elif city in self.city_urls:
                result = self.validate_nfse_generic(nfse_key, self.city_urls[city])
            else:
                # Tenta validação genérica em uma cidade padrão
                result = self.validate_nfse_generic(nfse_key, self.city_urls['sao_paulo'])
                
            self.logger.info(f"Validação NFS-e concluída: {nfse_key} - Status: {result['status']}")
                
        except Exception as e:
            result['error_message'] = f"Erro geral durante validação: {str(e)}"
            self.logger.error(f"Erro ao validar NFS-e {nfse_key}: {str(e)}")
        
        return result
    
    def validate_multiple_keys(self, keys: list, city: str = None) -> list:
        """
        Valida múltiplas chaves de NFS-e
        
        Args:
            keys: Lista de chaves para validar
            city: Cidade específica (opcional)
            
        Returns:
            Lista com resultados das validações
        """
        results = []
        
        try:
            for i, key in enumerate(keys):
                self.logger.info(f"Validando NFS-e {i+1}/{len(keys)}")
                result = self.validate_nfse_key(key, city)
                results.append(result)
                
                # Pausa entre consultas
                if i < len(keys) - 1:
                    time.sleep(3)
                    
        except Exception as e:
            self.logger.error(f"Erro durante validação múltipla NFS-e: {str(e)}")
        
        finally:
            self.close_driver()
        
        return results