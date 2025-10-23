#!/bin/bash

echo "🔨 GERANDO EXECUTÁVEL DO VALIDADOR NF-e/NFS-e"
echo "=============================================="

# Verificar se está no diretório correto
if [ ! -f "main.py" ]; then
    echo "❌ Erro: Execute este script no diretório do projeto!"
    exit 1
fi

# Criar diretório build se não existir
mkdir -p build
mkdir -p dist

echo ""
echo "📦 Instalando dependências necessárias..."
pip install pyinstaller

echo ""
echo "🔨 Gerando executável..."
echo "Isso pode levar alguns minutos..."

# Gerar executável usando o arquivo .spec
pyinstaller --clean ValidadorNF.spec

# Verificar se foi gerado com sucesso
if [ -f "dist/ValidadorNF" ] || [ -f "dist/ValidadorNF.exe" ]; then
    echo ""
    echo "✅ EXECUTÁVEL GERADO COM SUCESSO!"
    echo ""
    echo "📁 Localização:"
    ls -la dist/
    echo ""
    echo "📋 Como usar:"
    echo "1. Navegue até a pasta 'dist/'"
    echo "2. Execute o arquivo ValidadorNF (Linux/Mac) ou ValidadorNF.exe (Windows)"
    echo ""
    echo "📦 Para distribuir:"
    echo "- Copie toda a pasta 'dist/' para o computador de destino"
    echo "- Ou apenas o arquivo executável se for self-contained"
    echo ""
    echo "💾 Tamanho do executável:"
    du -h dist/ValidadorNF* 2>/dev/null || echo "Executável gerado"
else
    echo ""
    echo "❌ ERRO ao gerar executável!"
    echo "Verifique os logs acima para mais detalhes."
    echo ""
    echo "🔧 Possíveis soluções:"
    echo "1. Verifique se todas as dependências estão instaladas"
    echo "2. Tente executar: pip install --upgrade pyinstaller"
    echo "3. Verifique se há espaço suficiente em disco"
    exit 1
fi

echo ""
echo "🧪 Para testar o executável:"
echo "cd dist && ./ValidadorNF"