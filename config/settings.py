# Configurações gerais da aplicação

# URLs base para consulta
RECEITA_FEDERAL_URL = "https://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx"

# Configurações de cidades para NFS-e
CITY_CONFIGS = {
    'sao_paulo': {
        'name': 'São Paulo',
        'url': 'https://nfse.prefeitura.sp.gov.br/contribuinte/consultaNota.aspx',
        'type': 'selenium',
        'selectors': {
            'input_field': 'txtNumeroNota',
            'submit_button': 'btnConsultar',
            'success_indicators': [
                "//span[contains(text(), 'encontrada')]",
                "//td[contains(text(), 'Autorizado')]"
            ],
            'error_indicators': [
                "//span[contains(text(), 'não encontrada')]",
                "//span[contains(text(), 'inválida')]"
            ]
        }
    },
    'rio_de_janeiro': {
        'name': 'Rio de Janeiro',
        'url': 'https://notacarioca.rio.gov.br/contribuinte/consultaNota.aspx',
        'type': 'selenium',
        'selectors': {
            'input_field': 'txtNumeroNota',
            'submit_button': 'btnConsultar'
        }
    },
    'belo_horizonte': {
        'name': 'Belo Horizonte',
        'url': 'https://bhissdigital.pbh.gov.br/nfse/pages/consultarNota.jsf',
        'type': 'selenium',
        'selectors': {
            'input_field': 'form:numeroNota',
            'submit_button': 'form:consultar'
        }
    },
    'brasilia': {
        'name': 'Brasília',
        'url': 'https://www.nfse.df.gov.br/consulta/ConsultarNota.aspx',
        'type': 'selenium',
        'selectors': {
            'input_field': 'txtNumeroNota',
            'submit_button': 'btnConsultar'
        }
    }
}

# Configurações do Selenium
SELENIUM_CONFIG = {
    'implicit_wait': 10,
    'page_load_timeout': 30,
    'script_timeout': 30,
    'window_size': (1920, 1080),
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Configurações de pausa entre requests
REQUEST_DELAYS = {
    'between_requests': 2,  # segundos entre requisições
    'after_error': 5,       # segundos após erro
    'captcha_wait': 30,     # segundos para aguardar resolução de CAPTCHA
}

# Configurações do Excel
EXCEL_CONFIG = {
    'default_key_column': 'CHAVE_NF',
    'status_column': 'STATUS_VALIDACAO',
    'date_column': 'DATA_VALIDACAO',
    'details_column': 'DETALHES_ERRO',
    'sheet_name': 'Dados'
}

# Status possíveis
VALIDATION_STATUS = {
    'FOUND': 'ENCONTRADO',
    'NOT_FOUND': 'NAO_ENCONTRADO',
    'ERROR': 'ERRO',
    'PENDING': 'PENDENTE'
}