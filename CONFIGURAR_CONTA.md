# 🔄 Configurar Conta Temporária para o Repositório

## 📋 Configuração Atual
- **Nome:** F1690974 Bruno Apolonio de Aguiar Mazoni
- **Email:** bruno.mazoni@bb.com.br

## 🔧 Para Mudar Temporariamente (apenas neste projeto):

### 1. **Configurar nova identidade local:**
```bash
cd /home/wsl/Projetos/teste

# Configurar nome (apenas para este repositório)
git config user.name "Seu Nome Aqui"

# Configurar email (apenas para este repositório)
git config user.email "seu-email@exemplo.com"
```

### 2. **Verificar a mudança:**
```bash
# Ver configuração local (apenas deste projeto)
git config user.name
git config user.email

# Ver configuração global (não mudou)
git config --global user.name
git config --global user.email
```

### 3. **Refazer o commit com a nova identidade:**
```bash
# Corrigir o commit anterior com nova identidade
git commit --amend --reset-author --no-edit
```

### 4. **Comandos prontos para executar:**
```bash
# Exemplo - SUBSTITUA pelos seus dados:
git config user.name "João Silva"
git config user.email "joao.silva@gmail.com"

# Refazer último commit com nova identidade
git commit --amend --reset-author --no-edit

# Verificar
git log --oneline -1 --pretty=format:"%h %s (%an <%ae>)"
```

## 🌐 Para subir no GitHub com nova conta:

```bash
# 1. Adicionar remote com nova conta
git remote add origin https://github.com/NOVO_USUARIO/validador-nfe-nfse.git

# 2. Fazer push
git push -u origin main
```

## 🔄 Para Voltar à Configuração Original:

### **Opção A: Remover configuração local (volta para global)**
```bash
git config --unset user.name
git config --unset user.email
```

### **Opção B: Configurar explicitamente**
```bash
git config user.name "F1690974 Bruno Apolonio de Aguiar Mazoni"
git config user.email "bruno.mazoni@bb.com.br"
```

## ℹ️ **Importante:**
- As configurações com `git config` (sem --global) afetam **apenas este repositório**
- Suas configurações globais permanecem inalteradas
- Outros projetos continuarão usando a conta original

## 🎯 **Exemplo Completo:**
```bash
# Entrar no diretório
cd /home/wsl/Projetos/teste

# Configurar nova identidade
git config user.name "Minha Conta Pessoal"
git config user.email "minha-conta@gmail.com"

# Refazer commit com nova identidade
git commit --amend --reset-author --no-edit

# Verificar
echo "Nova configuração:"
echo "Nome: $(git config user.name)"
echo "Email: $(git config user.email)"

# Configuração global (não mudou)
echo ""
echo "Configuração global (inalterada):"
echo "Nome: $(git config --global user.name)"
echo "Email: $(git config --global user.email)"
```