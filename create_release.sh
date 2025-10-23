#!/bin/bash

echo "📦 CRIANDO RELEASE DISTRIBUÍVEL"
echo "==============================="

VERSION="1.0.0"
RELEASE_NAME="ValidadorNF_v${VERSION}"

# Verificar se executável existe
if [ ! -f "dist/ValidadorNF" ]; then
    echo "❌ Executável não encontrado!"
    echo "Execute primeiro: ./build_executable.sh"
    exit 1
fi

# Criar diretório de release
mkdir -p releases
rm -rf releases/${RELEASE_NAME}
mkdir -p releases/${RELEASE_NAME}

echo "📁 Copiando arquivos para release..."

# Copiar executável
cp dist/ValidadorNF releases/${RELEASE_NAME}/

# Copiar documentação
cp README.md releases/${RELEASE_NAME}/
cp QUICK_START.md releases/${RELEASE_NAME}/
cp FORMATO_EXCEL.md releases/${RELEASE_NAME}/
cp LICENSE releases/${RELEASE_NAME}/

# Copiar exemplos
cp -r examples/ releases/${RELEASE_NAME}/

# Criar arquivo de versão
cat > releases/${RELEASE_NAME}/VERSION.txt << EOF
Validador NF-e/NFS-e v${VERSION}
================================

Data de compilação: $(date)
Plataforma: $(uname -s) $(uname -m)
Tamanho do executável: $(du -h dist/ValidadorNF | cut -f1)

Funcionalidades:
✅ Validação automática de NF-e (Receita Federal)
✅ Validação automática de NFS-e (Prefeituras)
✅ Interface gráfica completa
✅ Manipulação de arquivos Excel
✅ Sistema de logs
✅ Múltiplas cidades suportadas

Para usar:
1. Execute o arquivo ValidadorNF
2. Selecione sua planilha Excel
3. Escolha o tipo de validação
4. Inicie o processo

Suporte: Consulte os arquivos de documentação incluídos
EOF

# Criar script de execução
cat > releases/${RELEASE_NAME}/executar.sh << EOF
#!/bin/bash
echo "🚀 Iniciando Validador NF-e/NFS-e..."
./ValidadorNF
EOF

chmod +x releases/${RELEASE_NAME}/executar.sh

# Criar arquivo ZIP
cd releases/
echo "🗜️  Compactando release..."
zip -r ${RELEASE_NAME}.zip ${RELEASE_NAME}/
cd ..

echo ""
echo "✅ RELEASE CRIADO COM SUCESSO!"
echo ""
echo "📁 Localização: releases/${RELEASE_NAME}.zip"
echo "📊 Tamanho: $(du -h releases/${RELEASE_NAME}.zip | cut -f1)"
echo ""
echo "📋 Conteúdo do release:"
ls -la releases/${RELEASE_NAME}/
echo ""
echo "🚀 Para distribuir:"
echo "   Envie o arquivo: releases/${RELEASE_NAME}.zip"
echo ""
echo "💡 O usuário deve:"
echo "   1. Descompactar o arquivo ZIP"
echo "   2. Executar: ./ValidadorNF ou ./executar.sh"
echo "   3. Instalar Google Chrome se necessário"