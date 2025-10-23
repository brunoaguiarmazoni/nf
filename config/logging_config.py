# Arquivo de configuração de logging
import logging
import logging.config
from pathlib import Path
import os

# Cria diretório de logs se não existir
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Configuração de logging
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': 'logs/validation.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'encoding': 'utf8'
        },
        'error_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': 'logs/errors.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 3,
            'encoding': 'utf8'
        }
    },
    'loggers': {
        '': {  # root logger
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'error_file']
        },
        'selenium': {
            'level': 'WARNING',
            'handlers': ['file'],
            'propagate': False
        },
        'urllib3': {
            'level': 'WARNING',
            'handlers': ['file'],
            'propagate': False
        }
    }
}

def setup_logging():
    """
    Configura o sistema de logging da aplicação
    """
    logging.config.dictConfig(LOGGING_CONFIG)
    
    # Logger principal
    logger = logging.getLogger(__name__)
    logger.info("Sistema de logging configurado com sucesso")
    
    return logger

def get_logger(name: str):
    """
    Obtém um logger com o nome especificado
    
    Args:
        name: Nome do logger
        
    Returns:
        Logger configurado
    """
    return logging.getLogger(name)