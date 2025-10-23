from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import logging
import re


class BaseWebAutomation:
    """
    Classe base para automação web com Selenium
    """
    
    def __init__(self, headless: bool = True, timeout: int = 30):
        self.driver = None
        self.wait = None
        self.timeout = timeout
        self.headless = headless
        self.logger = logging.getLogger(__name__)
        
    def setup_driver(self) -> None:
        """
        Configura o driver do Chrome
        """
        try:
            chrome_options = Options()
            if self.headless:
                chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
            
            # Instala automaticamente o ChromeDriver
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, self.timeout)
            
            self.logger.info("Driver Chrome configurado com sucesso")
            
        except Exception as e:
            self.logger.error(f"Erro ao configurar driver: {str(e)}")
            raise
    
    def close_driver(self) -> None:
        """
        Fecha o driver
        """
        if self.driver:
            try:
                self.driver.quit()
                self.logger.info("Driver fechado com sucesso")
            except Exception as e:
                self.logger.warning(f"Erro ao fechar driver: {str(e)}")
    
    def wait_for_element(self, by: By, value: str, timeout: int = None) -> bool:
        """
        Aguarda um elemento aparecer na página
        
        Args:
            by: Tipo de seletor (By.ID, By.CLASS_NAME, etc.)
            value: Valor do seletor
            timeout: Tempo limite em segundos
            
        Returns:
            True se elemento encontrado
        """
        try:
            wait_time = timeout or self.timeout
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((by, value))
            )
            return True
            
        except TimeoutException:
            self.logger.warning(f"Timeout aguardando elemento: {value}")
            return False
    
    def click_element(self, by: By, value: str) -> bool:
        """
        Clica em um elemento
        
        Args:
            by: Tipo de seletor
            value: Valor do seletor
            
        Returns:
            True se clique realizado com sucesso
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
            return True
            
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.warning(f"Erro ao clicar elemento {value}: {str(e)}")
            return False
    
    def fill_input(self, by: By, value: str, text: str) -> bool:
        """
        Preenche um campo de input
        
        Args:
            by: Tipo de seletor
            value: Valor do seletor
            text: Texto para preencher
            
        Returns:
            True se preenchido com sucesso
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            element.clear()
            element.send_keys(text)
            return True
            
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.warning(f"Erro ao preencher campo {value}: {str(e)}")
            return False
    
    def get_text_from_element(self, by: By, value: str) -> str:
        """
        Obtém texto de um elemento
        
        Args:
            by: Tipo de seletor
            value: Valor do seletor
            
        Returns:
            Texto do elemento ou string vazia
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            return element.text
            
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.warning(f"Erro ao obter texto do elemento {value}: {str(e)}")
            return ""
    
    def handle_captcha_if_present(self) -> bool:
        """
        Verifica se há captcha na página e aguarda resolução manual
        
        Returns:
            True se não há captcha ou se foi resolvido
        """
        captcha_selectors = [
            "//img[contains(@src, 'captcha')]",
            "//div[contains(@class, 'captcha')]",
            "//*[contains(text(), 'CAPTCHA')]",
            "//iframe[contains(@src, 'recaptcha')]"
        ]
        
        for selector in captcha_selectors:
            try:
                if self.driver.find_elements(By.XPATH, selector):
                    self.logger.warning("CAPTCHA detectado. Aguardando resolução manual...")
                    if not self.headless:
                        input("Por favor, resolva o CAPTCHA e pressione Enter para continuar...")
                    return True
            except:
                continue
        
        return True