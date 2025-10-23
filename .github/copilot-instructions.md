# Automação de Validação de Chaves NF-e/NFS-e

Sistema completo para automatizar a validação de chaves de Notas Fiscais Eletrônicas (NF-e) e Notas Fiscais de Serviços Eletrônicas (NFS-e) através de consulta aos sites da Receita Federal e Prefeituras.

## 🚀 Funcionalidades Implementadas
- ✅ Leitura e escrita de planilhas Excel com validação de formato
- ✅ Validação automática de NF-e no site da Receita Federal
- ✅ Validação automática de NFS-e em sites de múltiplas prefeituras
- ✅ Interface gráfica completa com Tkinter
- ✅ Sistema robusto de logging com rotação de arquivos
- ✅ Tratamento de CAPTCHAs e timeouts
- ✅ Modo headless para execução em background
- ✅ Pausas inteligentes entre requisições
- ✅ Atualização automática da planilha com resultados
- ✅ Sistema de resumo e estatísticas

## 🛠️ Tecnologias Utilizadas
- **Python 3.8+** - Linguagem principal
- **Selenium WebDriver** - Automação web com Chrome
- **Pandas & OpenPyXL** - Manipulação de arquivos Excel
- **Tkinter** - Interface gráfica nativa
- **WebDriver Manager** - Gerenciamento automático de drivers
- **Requests & BeautifulSoup** - Requisições HTTP e parse HTML

## 📁 Estrutura Completa do Projeto
```
validador-nfe-nfse/
├── main.py                     # ✅ Aplicação principal com GUI
├── requirements.txt            # ✅ Dependências do projeto
├── install.sh                  # ✅ Script de instalação automática
├── test_system.py             # ✅ Script de testes do sistema
├── create_example.py          # ✅ Gerador de planilhas exemplo
├── modules/                   # ✅ Módulos da aplicação
│   ├── excel_handler.py       # ✅ Manipulação robusta de Excel
│   ├── nfe_validator.py       # ✅ Validador de NF-e (Receita)
│   ├── nfse_validator.py      # ✅ Validador de NFS-e (Prefeituras)
│   └── web_automation.py      # ✅ Base para automação web
├── config/                    # ✅ Configurações do sistema
│   ├── logging_config.py      # ✅ Configuração avançada de logs
│   └── settings.py            # ✅ Configurações gerais e URLs
├── logs/                      # ✅ Diretório de logs
├── examples/                  # ✅ Planilhas e arquivos exemplo
└── README.md                  # ✅ Documentação completa
```

## 🎯 Como Executar
1. **Instalação rápida:** `./install.sh`
2. **Teste do sistema:** `python test_system.py`
3. **Executar aplicação:** `python main.py`
4. **Criar exemplo:** `python create_example.py`

## ✅ Status do Desenvolvimento
- ✅ **Projeto 100% funcional e pronto para uso**
- ✅ **Todos os módulos implementados e testados**
- ✅ **Interface gráfica completa e intuitiva**
- ✅ **Sistema robusto de tratamento de erros**
- ✅ **Documentação completa e exemplos incluídos**
- ✅ **Scripts de instalação e teste automatizados**

## 🔧 Recursos Avançados
- **Detecção automática** de formato de chaves NF
- **Suporte a múltiplas cidades** para NFS-e (SP, RJ, BH, BSB)
- **Sistema de logs com rotação** e níveis configuráveis  
- **Interface responsiva** com barra de progresso
- **Validação de integridade** de arquivos Excel
- **Tratamento inteligente** de CAPTCHAs
- **Pausas adaptativas** para evitar bloqueios
- **Resumos estatísticos** detalhados