# Automação de Validação de Chaves NF-e/NFS-e

Sistema automatizado para validação de chaves de Notas Fiscais Eletrônicas (NF-e) e Notas Fiscais de Serviços Eletrônicas (NFS-e) através de consulta aos sites da Receita Federal e Prefeituras.

## 🚀 Funcionalidades

- ✅ **Leitura de planilhas Excel** contendo chaves de NF
- ✅ **Validação automática no site da Receita Federal** (NF-e)  
- ✅ **Validação automática em sites de Prefeituras** (NFS-e)
- ✅ **Interface gráfica** intuitiva para facilitar o uso
- ✅ **Sistema de logs** detalhado para acompanhar o progresso
- ✅ **Atualização automática da planilha** com resultados
- ✅ **Suporte a múltiplas cidades** para NFS-e
- ✅ **Modo headless** para execução em background

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Selenium WebDriver** - Automação web
- **Pandas & OpenPyXL** - Manipulação de arquivos Excel
- **Tkinter** - Interface gráfica
- **Requests** - Requisições HTTP
- **BeautifulSoup4** - Parse de HTML
- **WebDriver Manager** - Gerenciamento automático de drivers

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd validador-nfe-nfse
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Verifique se o Chrome está instalado
O sistema utiliza o Chrome WebDriver. Certifique-se de ter o Google Chrome instalado no sistema.

## � Como Executar

### 🐧 Linux
1. **Instalação rápida:** `./install.sh`
2. **Teste do sistema:** `python test_system.py`
3. **Executar aplicação:** `python main.py`
4. **Criar exemplo:** `python create_example.py`
5. **Gerar executável:** `./build_executable.sh`

### 🪟 Windows
1. **Instalar dependências:** `pip install -r requirements.txt`
2. **Gerar executável:** `build_executable_windows.bat`
3. **Criar release:** `create_release_windows.bat`
4. **Instruções detalhadas:** Ver `INSTRUÇÕES_WINDOWS.md`

## 📋 Status de Validação

O sistema atualiza a coluna `STATUS_VALIDACAO` com os seguintes valores:

- `ENCONTRADO` - NF encontrada e válida
- `NAO_ENCONTRADO` - NF não encontrada nos órgãos
- `ERRO` - Erro durante a validação (detalhes na coluna DETALHES_ERRO)

## 🗂️ Estrutura do Projeto

```
validador-nfe-nfse/
├── main.py                     # Aplicação principal com interface gráfica
├── requirements.txt            # Dependências do projeto
├── modules/                    # Módulos da aplicação
│   ├── __init__.py
│   ├── excel_handler.py        # Manipulação de arquivos Excel
│   ├── nfe_validator.py        # Validação de NF-e (Receita Federal)
│   ├── nfse_validator.py       # Validação de NFS-e (Prefeituras)
│   └── web_automation.py       # Funções base para automação web
├── config/                     # Configurações
│   ├── __init__.py
│   ├── logging_config.py       # Configuração de logs
│   └── settings.py             # Configurações gerais
├── logs/                       # Arquivos de log
│   ├── validation.log          # Log principal
│   └── errors.log              # Log de erros
├── examples/                   # Exemplos de uso
│   ├── exemplo_planilha.xlsx   # Planilha de exemplo
│   └── exemplo_nfe.csv         # CSV de exemplo
└── README.md                   # Este arquivo
```

## ⚙️ Configurações Avançadas

### Logging

Os logs são salvos automaticamente em:
- `logs/validation.log` - Log geral da aplicação
- `logs/errors.log` - Apenas erros

### Personalização de Cidades (NFS-e)

Para adicionar novas cidades, edite o arquivo `config/settings.py`:

```python
CITY_CONFIGS = {
    'nova_cidade': {
        'name': 'Nova Cidade',
        'url': 'https://site-da-prefeitura.com/consulta',
        'type': 'selenium',
        'selectors': {
            'input_field': 'campo_numero_nota',
            'submit_button': 'botao_consultar'
        }
    }
}
```

## 🚨 Limitações e Considerações

1. **CAPTCHA**: Sites podem exigir resolução manual de CAPTCHA
2. **Rate Limiting**: Pausas automáticas entre requisições para evitar bloqueios
3. **Mudanças nos sites**: Seletores podem precisar de atualização se sites mudarem
4. **Conectividade**: Requer conexão estável com a internet
5. **Chaves válidas**: O sistema valida formato mas não garante existência real

## 🔧 Solução de Problemas

### Erro "ChromeDriver not found"
```bash
# O WebDriver Manager instala automaticamente, mas se houver problemas:
pip install --upgrade webdriver-manager
```

### Erro ao ler arquivo Excel
- Verifique se o arquivo não está aberto em outro programa
- Confirme se a coluna 'CHAVE_NF' existe
- Verifique permissões de escrita no arquivo

### Site não responde
- Verifique sua conexão com a internet
- Alguns sites podem estar temporariamente indisponíveis
- Tente novamente após alguns minutos

### CAPTCHA aparece constantemente
- Execute em modo não-headless para resolver manualmente
- Reduza a velocidade das consultas
- Considere usar intervalos maiores entre requisições

## 🤝 Contribuição

1. Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ⚠️ Aviso Legal

Este software é fornecido "como está", sem garantias. Use por sua própria conta e risco. Sempre verifique as informações importantes manualmente. O uso deve estar em conformidade com os termos de uso dos sites consultados.

## 📞 Suporte

Para dúvidas ou problemas:
1. Consulte a documentação acima
2. Verifique os logs em `logs/`
3. Abra uma issue no repositório

---

Desenvolvido com ❤️ para automatizar a validação de notas fiscais.