#!/bin/bash

echo "🚀 COMANDOS PARA SUBIR NO GITHUB"
echo "================================="
echo ""
echo "📋 PRÉ-REQUISITOS:"
echo "1. Crie um repositório no GitHub:"
echo "   - Vá para: https://github.com/new"
echo "   - Nome: validador-nfe-nfse"
echo "   - Descrição: Sistema automatizado para validação de chaves de NF-e e NFS-e"
echo "   - Público ou Privado (sua escolha)"
echo "   - NÃO adicione README, .gitignore ou LICENSE (já temos)"
echo "   - Clique 'Create repository'"
echo ""
echo "2. Substitua 'SEU_USUARIO' pelo seu username do GitHub nos comandos abaixo"
echo ""

echo "🔗 COMANDOS PARA EXECUTAR:"
echo ""

echo "# 1. Verificar status atual"
echo "git status"
echo ""

echo "# 2. Adicionar origin remote (SUBSTITUA SEU_USUARIO!)"
echo "git remote add origin https://github.com/SEU_USUARIO/validador-nfe-nfse.git"
echo ""

echo "# 3. Verificar remote"
echo "git remote -v"
echo ""

echo "# 4. Fazer push inicial"
echo "git push -u origin main"
echo ""

echo "✅ VERIFICAÇÃO:"
echo "Após executar, acesse: https://github.com/SEU_USUARIO/validador-nfe-nfse"
echo ""

echo "🔧 SE DER ERRO DE AUTENTICAÇÃO:"
echo "- Use Personal Access Token (GitHub Settings > Developer settings > Tokens)"
echo "- Ou configure SSH keys"
echo ""

echo "📊 STATUS ATUAL:"
git log --oneline -1
git status --porcelain | wc -l | xargs -I {} echo "{} arquivos não commitados"