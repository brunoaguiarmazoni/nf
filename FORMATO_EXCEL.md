# 📊 Formato Específico do Arquivo Excel

## ✅ Formato Obrigatório

Seu arquivo Excel **DEVE** ter pelo menos uma coluna com as chaves das notas fiscais:

### Coluna Obrigatória:
- **`CHAVE_NF`** - Contém as chaves de 44 dígitos das notas fiscais

### Colunas Opcionais (serão criadas automaticamente se não existirem):
- **`STATUS_VALIDACAO`** - Resultado da validação
- **`DATA_VALIDACAO`** - Data/hora da validação  
- **`DETALHES_ERRO`** - Detalhes de erros (se houver)

## 📋 Exemplo de Estrutura Mínima

| CHAVE_NF |
|----------|
| 35240123456789012345678901234567890123456789 |
| 35240223456789012345678901234567890123456789 |
| 35240323456789012345678901234567890123456789 |

## 📋 Exemplo de Estrutura Completa (Recomendada)

| CHAVE_NF | NUMERO_NF | EMPRESA | VALOR | STATUS_VALIDACAO | DATA_VALIDACAO | DETALHES_ERRO |
|----------|-----------|---------|-------|------------------|----------------|---------------|
| 35240123456789012345678901234567890123456789 | 001 | Empresa A Ltda | 1000.50 | | | |
| 35240223456789012345678901234567890123456789 | 002 | Empresa B S.A. | 2500.75 | | | |
| 35240323456789012345678901234567890123456789 | 003 | Empresa C ME | 850.25 | | | |

## 🔍 Detalhes Importantes

### ✅ **Formato das Chaves de NF:**
- **44 dígitos numéricos** para NF-e
- Pode conter espaços ou traços (serão removidos automaticamente)
- Exemplos válidos:
  ```
  35240123456789012345678901234567890123456789
  3524 0123 4567 8901 2345 6789 0123 4567 8901 2345 6789
  35240123456789012345678901234567890123456789
  ```

### 🏷️ **Nome da Coluna de Chaves:**
O sistema procura por colunas nesta ordem:
1. `CHAVE_NF` (padrão)
2. Qualquer coluna que contenha a palavra "chave" (ex: `CHAVE_ACESSO`, `chave_nota`)

### 📄 **Formato do Arquivo:**
- **.xlsx** (Excel 2007+) - **Recomendado**
- **.xls** (Excel 97-2003) - Também suportado

### 📑 **Abas/Planilhas:**
- Se não especificar, usa a **primeira aba**
- Pode especificar o nome da aba no código se necessário

## 🚨 Validações Automáticas

### ✅ **O que o sistema faz automaticamente:**
1. **Remove espaços e caracteres especiais** das chaves
2. **Valida se a chave tem 44 dígitos**
3. **Cria colunas de resultado** se não existirem
4. **Detecta automaticamente** colunas com "chave" no nome
5. **Preserva dados existentes** nas outras colunas

### ❌ **O que causará erro:**
- Arquivo Excel corrompido ou protegido por senha
- Nenhuma coluna com chaves identificada
- Arquivo em uso por outro programa
- Chaves com menos ou mais de 44 dígitos

## 📊 Resultado Após Validação

Seu arquivo será atualizado com:

| STATUS_VALIDACAO | Significado |
|------------------|-------------|
| `ENCONTRADO` | ✅ Nota fiscal encontrada e válida |
| `NAO_ENCONTRADO` | ❌ Nota fiscal não encontrada |
| `ERRO` | ⚠️ Erro durante a validação |

## 💡 Exemplos Práticos

### ✅ **Formato Simples (Mínimo):**
```excel
CHAVE_NF
35240123456789012345678901234567890123456789
35240223456789012345678901234567890123456789
```

### ✅ **Formato Completo (Recomendado):**
```excel
CHAVE_NF | NUMERO | EMPRESA | VALOR | STATUS_VALIDACAO | DATA_VALIDACAO | DETALHES_ERRO
35240123456789012345678901234567890123456789 | NF-001 | Empresa ABC | 1500.00 | | | 
35240223456789012345678901234567890123456789 | NF-002 | Empresa XYZ | 2300.50 | | |
```

### ✅ **Variações Aceitas no Nome da Coluna:**
```excel
CHAVE_ACESSO | chave_nota | CHAVE_NF_E | chave
35240123... | 35240223... | 35240323... | 35240423...
```

## 🛠️ Gerar Arquivo de Exemplo

Execute este comando para criar um exemplo pronto:

```bash
python create_example.py
```

Será criado o arquivo: `examples/exemplo_planilha.xlsx`

## 📞 Dicas de Uso

1. **Teste primeiro** com poucas chaves (5-10) para verificar o formato
2. **Faça backup** do arquivo original antes da validação
3. **Não abra o arquivo** no Excel durante a validação
4. **Verifique os logs** em caso de erro para diagnóstico detalhado

---

**💡 Resumo:** O arquivo Excel precisa de **pelo menos uma coluna com chaves de 44 dígitos**. O sistema é flexível e detecta automaticamente a maioria dos formatos comuns!