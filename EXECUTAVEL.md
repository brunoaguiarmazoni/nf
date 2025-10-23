# 🚀 Executável do Validador NF-e/NFS-e

## 📦 Sobre o Executável

O executável permite usar a aplicação **sem instalar Python** ou dependências no computador de destino.

## 🔨 Como Gerar o Executável

### **Método 1: Script Automático (Recomendado)**
```bash
# No diretório do projeto:
./build_executable.sh
```

### **Método 2: Comando Manual**
```bash
# Instalar PyInstaller
pip install pyinstaller

# Gerar executável
pyinstaller --clean ValidadorNF.spec
```

### **Método 3: One-File (arquivo único)**
```bash
pyinstaller --onefile --windowed --name ValidadorNF main.py
```

## 📁 Estrutura Gerada

Após a geração, você terá:

```
projeto/
├── dist/                    # 📂 Executável final
│   ├── ValidadorNF          # 🚀 Executável (Linux/Mac)
│   ├── ValidadorNF.exe      # 🚀 Executável (Windows)
│   └── _internal/           # 📁 Bibliotecas necessárias
├── build/                   # 📂 Arquivos temporários
└── ValidadorNF.spec         # ⚙️ Configuração do build
```

## 🖥️ Como Usar o Executável

### **Linux/Mac:**
```bash
cd dist/
./ValidadorNF
```

### **Windows:**
```cmd
cd dist\
ValidadorNF.exe
```

### **Interface Gráfica:**
1. Clique duas vezes no executável
2. A interface gráfica abrirá automaticamente
3. Use normalmente como a versão Python

## 📦 Distribuição

### **Para distribuir o executável:**

1. **Opção 1: Pasta Completa (Recomendado)**
   - Compacte toda a pasta `dist/`
   - Envie o arquivo ZIP
   - O usuário descompacta e executa

2. **Opção 2: Arquivo Único**
   - Use `--onefile` no PyInstaller
   - Gera um único arquivo executável
   - Maior tempo de inicialização

### **Exemplo de distribuição:**
```bash
# Criar arquivo ZIP para distribuição
cd dist/
zip -r ValidadorNF_v1.0.zip ValidadorNF*

# Para Windows (PowerShell)
Compress-Archive -Path ValidadorNF* -DestinationPath ValidadorNF_v1.0.zip
```

## 🛠️ Requisitos do Sistema

### **Para executar:**
- ✅ **Nenhuma dependência Python necessária**
- ✅ Sistema operacional: Windows 7+, Linux, macOS
- ✅ Google Chrome instalado (para automação web)
- ✅ Conexão com internet (para validação)

### **Para gerar:**
- Python 3.8+
- PyInstaller
- Todas as dependências do projeto

## 🔧 Solução de Problemas

### **Executável não inicia:**
```bash
# Linux/Mac - executar no terminal para ver erros
./ValidadorNF

# Windows - executar no CMD
ValidadorNF.exe
```

### **Erro de "arquivo não encontrado":**
- Certifique-se de executar na pasta `dist/`
- Verifique se todos os arquivos da pasta `dist/` estão presentes

### **Erro de Chrome/WebDriver:**
- Instale o Google Chrome no sistema
- O executável baixa automaticamente o WebDriver

### **Executável muito grande:**
```bash
# Gerar versão otimizada
pyinstaller --onefile --optimize=2 --strip main.py
```

## 📊 Tamanhos Típicos

- **Pasta completa:** ~150-200 MB
- **Arquivo único:** ~80-120 MB
- **Com UPX compressão:** ~40-60 MB

## 🎯 Vantagens do Executável

- ✅ **Portabilidade:** Funciona sem Python instalado
- ✅ **Simplicidade:** Usuário final só precisa executar
- ✅ **Distribuição:** Fácil de compartilhar
- ✅ **Segurança:** Código fonte não visível

## 📝 Versões

### **Configurações no arquivo .spec:**

- `console=False` - Sem janela de console
- `onefile=False` - Múltiplos arquivos (mais rápido)
- `upx=True` - Compressão UPX
- `debug=False` - Sem informações de debug

### **Personalização:**
```python
# No arquivo ValidadorNF.spec
exe = EXE(
    # ...
    name='ValidadorNF_v1.0',     # Nome personalizado
    icon='icon.ico',             # Ícone personalizado
    console=False,               # Sem console
    # ...
)
```

## 🔄 Atualizações

Para criar nova versão:
1. Modifique o código Python
2. Execute `./build_executable.sh` novamente
3. Teste o novo executável
4. Distribua a nova versão

---

**💡 Dica:** Teste sempre o executável em um computador limpo (sem Python) antes de distribuir!