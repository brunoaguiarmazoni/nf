# 🎯 GUIA PARA USUÁRIOS SEM PYTHON

## 🚀 Solução Completa para Windows

### ❓ Não tem Python instalado? Sem problema!

Criei um **setup automático** que resolve tudo para você:

```batch
# 1. Baixar o projeto (escolha uma opção):

# OPÇÃO A: Download direto (mais fácil)
# - Vá para: https://github.com/seu-usuario/validador-nfe-nfse
# - Clique em "Code" → "Download ZIP"
# - Extrair em uma pasta (ex: C:\validador-nfe-nfse)

# OPÇÃO B: Git clone (se tiver Git)
git clone https://github.com/seu-usuario/validador-nfe-nfse.git

# 2. Executar setup AUTOMÁTICO
SETUP_WINDOWS_COMPLETO.bat
```

## 🔧 O que o Setup Automático faz:

### ✅ Verifica Python
- Detecta se Python está instalado
- Se não tiver, oferece instalação automática

### ✅ Instala Python (se necessário)
- Baixa Python 3.11 oficial
- Instala automaticamente
- Configura PATH corretamente

### ✅ Configura o Projeto
- Instala todas as dependências
- Gera o executável final
- Cria release para distribuição

## 🎯 Resultado Final:

Após executar `SETUP_WINDOWS_COMPLETO.bat`:

```
✅ Python instalado e configurado
✅ Dependências instaladas
✅ Executável gerado: dist/ValidadorNF.exe
✅ Release criado: release_windows/
✅ Pronto para usar!
```

## 🚀 Como Usar o Executável:

1. **Navegue para** `dist/` ou `release_windows/`
2. **Execute** `ValidadorNF.exe`
3. **Use normalmente** - não precisa mais de Python!

## 💡 Alternativas se o Setup Automático Falhar:

### Instalação Manual do Python:
1. **Site oficial**: https://www.python.org/downloads/
2. **Baixar** a versão mais recente
3. **⚠️ IMPORTANTE**: Marcar "Add Python to PATH"
4. **Instalar** e reiniciar o Prompt
5. **Executar** `build_executable_windows.bat`

### Download do Executável Pronto:
- Se disponível, baixar diretamente o `.exe` das releases
- Não precisa instalar nada, apenas executar

## 🆘 Troubleshooting:

### "Python não encontrado" após instalação:
```batch
# Fechar e reabrir o Prompt de Comando
# Ou executar:
refreshenv
```

### "UAC - Controle de Conta de Usuário":
- **Clicar em "SIM"** quando aparecer
- É necessário para instalar o Python

### Antivírus bloqueando:
- **Temporariamente desativar** antivírus
- Ou **adicionar exceção** para a pasta do projeto

---

🎯 **Objetivo**: Qualquer pessoa conseguir usar, mesmo sem conhecimento técnico
✅ **Status**: Setup 100% automático criado
🚀 **Próximo passo**: Execute `SETUP_WINDOWS_COMPLETO.bat`