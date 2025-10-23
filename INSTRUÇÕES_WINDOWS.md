# 🎯 INSTRUÇÕES RÁPIDAS: Executável Windows

## 🚀 SETUP AUTOMÁTICO (Recomendado)

### ⚡ Para usuários SEM Python instalado:
```batch
# 1. Baixar o projeto (ZIP ou Git)
# Baixar ZIP: https://github.com/seu-usuario/validador-nfe-nfse/archive/main.zip
# Ou com Git: git clone https://github.com/seu-usuario/validador-nfe-nfse.git

# 2. Executar setup completo (AUTOMÁTICO!)
SETUP_WINDOWS_COMPLETO.bat
```

### ⚡ Para usuários COM Python instalado:
```batch
# 1. Baixar o projeto
git clone https://github.com/seu-usuario/validador-nfe-nfse.git
cd validador-nfe-nfse

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Gerar executável (automático)
build_executable_windows.bat

# 4. Criar release distribuível
create_release_windows.bat
```

### Resultado:
- 📁 `dist/ValidadorNF.exe` (~70 MB)
- 📦 `release_windows/` (pasta completa)
- 🎯 100% funcional e independente

## Como Usar o Executável

1. **Execute** `ValidadorNF.exe`
2. **Selecione** sua planilha Excel
3. **Escolha** tipo de validação (NF-e/NFS-e)
4. **Aguarde** o processamento
5. **Verifique** os resultados na planilha

## Formato da Planilha

```
| Coluna A        | Coluna B     |
|-----------------|--------------|
| Chave da NF     | Status       |
| 35200114200[...] | [automático] |
```

## 🔧 Troubleshooting

### Problemas Comuns:
- **Python não encontrado**: Instale Python 3.8+ oficial
- **PyInstaller falha**: Execute `pip install --upgrade pyinstaller`
- **Antivírus bloqueia**: Adicionar exceção para a pasta

### Suporte:
- 📊 Logs automáticos em `logs/`
- 📖 README.md completo
- 📝 Planilha exemplo incluída

---

🚀 **Status**: ✅ Pronto para Windows
📞 **Suporte**: Verifique logs para detalhes