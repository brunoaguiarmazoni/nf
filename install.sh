#!/bin/bash

echo "🚀 Instalando Validador de NF-e/NFS-e..."
echo "======================================"

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale o Python 3.8+"
    exit 1
fi

# Verifica versão do Python
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $python_version encontrado"

# Instala dependências
echo "📦 Instalando dependências..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependências instaladas com sucesso"
else
    echo "❌ Erro ao instalar dependências"
    exit 1
fi

# Cria diretórios necessários
mkdir -p logs examples

# Cria planilha de exemplo
echo "📊 Criando planilha de exemplo..."
python3 create_example.py

# Testa importações
echo "🧪 Testando importações..."
python3 -c "
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk
print('✅ Todas as bibliotecas importadas com sucesso')
"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Instalação concluída com sucesso!"
    echo ""
    echo "📋 Para usar o sistema:"
    echo "   1. Execute: python3 main.py"
    echo "   2. Selecione a planilha: examples/exemplo_planilha.xlsx"
    echo "   3. Escolha o tipo de validação e inicie o processo"
    echo ""
    echo "📖 Documentação completa: README.md"
    echo ""
else
    echo "❌ Erro durante os testes"
    exit 1
fi