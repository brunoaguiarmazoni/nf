#!/bin/bash

echo "🧪 TESTANDO EXECUTÁVEL DO VALIDADOR NF-e/NFS-e"
echo "==============================================="

# Verificar se executável existe
if [ ! -f "dist/ValidadorNF" ]; then
    echo "❌ Executável não encontrado!"
    echo "Execute primeiro: ./build_executable.sh"
    exit 1
fi

echo "📋 Informações do executável:"
echo "Tamanho: $(du -h dist/ValidadorNF | cut -f1)"
echo "Tipo: $(file dist/ValidadorNF | cut -d: -f2)"
echo ""

echo "🔍 Verificando dependências..."
ldd dist/ValidadorNF | head -5

echo ""
echo "✅ Executável pronto para uso!"
echo ""
echo "🚀 Para executar:"
echo "cd dist/"
echo "./ValidadorNF"
echo ""

echo "📦 Para criar versão distribuível:"
echo "./create_release.sh"