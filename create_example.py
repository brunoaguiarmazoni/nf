#!/usr/bin/env python3
"""
Script para criar planilha de exemplo
"""
import pandas as pd
from pathlib import Path

def create_example_spreadsheet():
    print("📊 Criando planilhas de exemplo...")
    
    # Dados de exemplo com chaves válidas (formato correto)
    data_completa = {
        'CHAVE_NF': [
            '35240123456789012345678901234567890123456789',
            '35240223456789012345678901234567890123456789', 
            '35240323456789012345678901234567890123456789',
            '35240423456789012345678901234567890123456789',
            '35240523456789012345678901234567890123456789'
        ],
        'NUMERO_NF': ['NF-001', 'NF-002', 'NF-003', 'NF-004', 'NF-005'],
        'EMPRESA': ['Empresa A Ltda', 'Empresa B S.A.', 'Empresa C ME', 'Empresa D EIRELI', 'Empresa E Ltda'],
        'CNPJ': ['11.222.333/0001-44', '55.666.777/0001-88', '99.888.777/0001-66', '33.444.555/0001-22', '77.888.999/0001-11'],
        'VALOR': [1000.50, 2500.75, 850.25, 3200.00, 1500.80],
        'DATA_EMISSAO': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19'],
        'STATUS_VALIDACAO': ['', '', '', '', ''],
        'DATA_VALIDACAO': ['', '', '', '', ''],
        'DETALHES_ERRO': ['', '', '', '', '']
    }

    # Dados simples (formato mínimo)
    data_simples = {
        'CHAVE_NF': [
            '35240123456789012345678901234567890123456789',
            '35240223456789012345678901234567890123456789', 
            '35240323456789012345678901234567890123456789'
        ]
    }

    # Criar diretório se não existir
    Path('examples').mkdir(exist_ok=True)
    
    # Salvar planilha completa
    df_completa = pd.DataFrame(data_completa)
    df_completa.to_excel('examples/exemplo_completo.xlsx', index=False, sheet_name='NFe_Dados')
    print('✅ Planilha completa criada: examples/exemplo_completo.xlsx')
    
    # Salvar planilha simples
    df_simples = pd.DataFrame(data_simples)  
    df_simples.to_excel('examples/exemplo_simples.xlsx', index=False, sheet_name='Dados')
    print('✅ Planilha simples criada: examples/exemplo_simples.xlsx')
    
    # Criar exemplo com nome de coluna alternativo
    data_alternativa = data_simples.copy()
    data_alternativa['CHAVE_ACESSO'] = data_alternativa.pop('CHAVE_NF')
    df_alternativa = pd.DataFrame(data_alternativa)
    df_alternativa.to_excel('examples/exemplo_chave_acesso.xlsx', index=False, sheet_name='Dados')
    print('✅ Planilha com nome alternativo criada: examples/exemplo_chave_acesso.xlsx')
    
    print("\n📋 Arquivos criados:")
    print("  • exemplo_completo.xlsx - Planilha com todas as colunas recomendadas")
    print("  • exemplo_simples.xlsx - Planilha com formato mínimo")  
    print("  • exemplo_chave_acesso.xlsx - Exemplo com nome de coluna alternativo")
    print("\n💡 Use qualquer um destes exemplos para testar o sistema!")

if __name__ == "__main__":
    create_example_spreadsheet()