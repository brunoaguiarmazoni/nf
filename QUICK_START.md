# 🚀 INÍCIO RÁPIDO - Validador NF-e/NFS-e

## ⚡ Executar em 3 passos:

### 1. Instalar dependências
```bash
pip install pandas openpyxl selenium webdriver-manager requests beautifulsoup4 lxml tqdm
```

### 2. Executar aplicação
```bash
python main.py
```

### 3. Na interface:
- Clique em "Procurar" e selecione sua planilha Excel
- Escolha o tipo: **NF-e** (Receita Federal) ou **NFS-e** (Prefeitura)
- Para NFS-e, selecione a cidade
- Clique em "Iniciar Validação"

## 📊 Formato da Planilha Excel

Sua planilha deve ter a coluna:
- **CHAVE_NF** - com as chaves de 44 dígitos

Exemplo:
| CHAVE_NF | 
|----------|
| 35240123456789012345678901234567890123456789 |
| 35240223456789012345678901234567890123456789 |

> As colunas STATUS_VALIDACAO, DATA_VALIDACAO e DETALHES_ERRO serão criadas automaticamente.

## 🎯 Resultado

Após a validação, sua planilha será atualizada com:
- ✅ **ENCONTRADO** - NF válida
- ❌ **NAO_ENCONTRADO** - NF não encontrada  
- ⚠️ **ERRO** - Erro na validação

## 🔧 Gerar Planilha de Exemplo

```bash
python create_example.py
```

Será criada: `examples/exemplo_planilha.xlsx`

## 🧪 Testar Sistema

```bash
python test_system.py
```

## 📖 Documentação Completa

Veja `README.md` para instruções detalhadas.

---
**💡 Dica:** Execute primeiro com uma planilha pequena (5-10 chaves) para testar!