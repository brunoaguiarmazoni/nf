#!/usr/bin/env python3
"""
Script de teste para verificar o funcionamento do sistema
"""

import sys
import logging
from pathlib import Path

# Adiciona o diretório atual ao path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Testa se todas as importações estão funcionando"""
    try:
        print("🧪 Testando importações...")
        
        # Testa pandas e openpyxl
        import pandas as pd
        print("  ✅ pandas")
        
        # Testa selenium
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        print("  ✅ selenium")
        
        # Testa tkinter
        import tkinter as tk
        print("  ✅ tkinter")
        
        # Testa requests
        import requests
        print("  ✅ requests")
        
        # Testa módulos locais
        from modules.excel_handler import ExcelHandler
        print("  ✅ excel_handler")
        
        from modules.nfe_validator import NFEValidator
        print("  ✅ nfe_validator")
        
        from modules.nfse_validator import NFSEValidator
        print("  ✅ nfse_validator")
        
        print("✅ Todas as importações OK!")
        return True
        
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

def test_excel_handler():
    """Testa o manipulador de Excel"""
    try:
        print("\n📊 Testando manipulação de Excel...")
        
        # Cria dados de teste
        import pandas as pd
        data = {
            'CHAVE_NF': ['35240123456789012345678901234567890123456789'],
            'STATUS_VALIDACAO': [''],
            'DATA_VALIDACAO': [''],
            'DETALHES_ERRO': ['']
        }
        df = pd.DataFrame(data)
        
        # Salva arquivo de teste
        test_file = Path('test_temp.xlsx')
        df.to_excel(test_file, index=False)
        
        # Testa leitura
        from modules.excel_handler import ExcelHandler
        handler = ExcelHandler(str(test_file))
        df_read = handler.read_excel_data()
        
        print(f"  ✅ Arquivo lido: {len(df_read)} registros")
        
        # Remove arquivo de teste
        test_file.unlink()
        
        print("✅ Manipulação de Excel OK!")
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste Excel: {e}")
        return False

def test_logging():
    """Testa o sistema de logging"""
    try:
        print("\n📝 Testando sistema de logging...")
        
        # Configura logging
        from config.logging_config import setup_logging
        setup_logging()
        
        # Testa log
        logger = logging.getLogger(__name__)
        logger.info("Teste de logging funcionando")
        
        print("✅ Sistema de logging OK!")
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste de logging: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🔬 VALIDADOR NF-e/NFS-e - TESTE DO SISTEMA")
    print("=" * 50)
    
    tests = [
        ("Importações", test_imports),
        ("Excel Handler", test_excel_handler), 
        ("Logging", test_logging)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        results[test_name] = test_func()
    
    # Resumo dos resultados
    print("\n" + "=" * 50)
    print("📋 RESUMO DOS TESTES:")
    
    success_count = 0
    for test_name, success in results.items():
        status = "✅ PASSOU" if success else "❌ FALHOU"
        print(f"  {test_name}: {status}")
        if success:
            success_count += 1
    
    print(f"\n📊 Resultado: {success_count}/{len(tests)} testes passaram")
    
    if success_count == len(tests):
        print("\n🎉 Todos os testes passaram! O sistema está pronto para uso.")
        print("\n🚀 Para executar a aplicação:")
        print("   python main.py")
    else:
        print("\n⚠️  Alguns testes falharam. Verifique as dependências e configurações.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())