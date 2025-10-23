@echo off
echo 🚀 SETUP COMPLETO WINDOWS - Validador NF-e/NFS-e
echo ====================================================
echo.
echo Este script irá:
echo 1. ✅ Verificar se Python está instalado
echo 2. 📥 Baixar e instalar Python se necessário
echo 3. 📦 Instalar dependências do projeto
echo 4. 🔨 Gerar executável Windows
echo 5. 📁 Criar release para distribuição
echo.
pause

REM Verificar se Python está instalado
echo 🔍 Verificando Python...
python --version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo ✅ Python encontrado!
    python --version
    goto :install_deps
)

echo ⚠️  Python não encontrado no sistema!
echo.
echo 📥 OPÇÕES DE INSTALAÇÃO:
echo.
echo [1] AUTOMÁTICA - Baixar e instalar Python automaticamente
echo [2] MANUAL - Abrir site do Python para download manual
echo [3] CANCELAR - Sair sem instalar
echo.
set /p choice="Escolha uma opção (1, 2 ou 3): "

if "%choice%"=="1" goto :install_python_auto
if "%choice%"=="2" goto :install_python_manual
if "%choice%"=="3" goto :exit_script
goto :invalid_choice

:install_python_auto
echo.
echo 📥 Baixando Python 3.11 (versão recomendada)...
echo ⏳ Isso pode levar alguns minutos...

REM Criar diretório temporário
if not exist "temp" mkdir temp

REM Baixar Python usando PowerShell
powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe' -OutFile 'temp\python-installer.exe'}"

if not exist "temp\python-installer.exe" (
    echo ❌ Erro ao baixar Python!
    echo 🔗 Tente a instalação manual: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Download concluído!
echo 🔧 Instalando Python (pode aparecer UAC - clique em SIM)...

REM Instalar Python silenciosamente
temp\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo ⏳ Aguardando instalação...
timeout /t 30 /nobreak >nul

REM Limpar arquivo temporário
del temp\python-installer.exe
rmdir temp

REM Verificar se instalação foi bem-sucedida
echo 🔍 Verificando instalação...
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ❌ Instalação falhou ou Python não foi adicionado ao PATH
    echo 🔄 Feche e reabra o Prompt de Comando, depois execute novamente
    echo 🔗 Ou instale manualmente: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python instalado com sucesso!
python --version
goto :install_deps

:install_python_manual
echo.
echo 🌐 Abrindo site oficial do Python...
echo.
echo 📋 INSTRUÇÕES PARA INSTALAÇÃO MANUAL:
echo 1. O navegador abrirá no site https://www.python.org/downloads/
echo 2. Clique em "Download Python 3.x.x" (versão mais recente)
echo 3. Execute o arquivo baixado
echo 4. ⚠️  IMPORTANTE: Marque "Add Python to PATH" durante a instalação
echo 5. Após instalar, feche e reabra este prompt
echo 6. Execute este script novamente
echo.

start https://www.python.org/downloads/

echo ⏸️  Execute este script novamente após instalar o Python!
pause
exit /b 0

:invalid_choice
echo ❌ Opção inválida! Digite 1, 2 ou 3.
goto :install_python_auto

:install_deps
echo.
echo 📦 Instalando dependências do projeto...

REM Verificar se requirements.txt existe
if not exist "requirements.txt" (
    echo ❌ Arquivo requirements.txt não encontrado!
    echo 🔄 Execute este script no diretório do projeto.
    pause
    exit /b 1
)

REM Atualizar pip
echo 🔄 Atualizando pip...
python -m pip install --upgrade pip

REM Instalar dependências
echo 📋 Instalando dependências...
pip install -r requirements.txt

if %ERRORLEVEL% neq 0 (
    echo ❌ Erro ao instalar dependências!
    echo 🔧 Tente executar manualmente: pip install -r requirements.txt
    pause
    exit /b 1
)

echo ✅ Dependências instaladas com sucesso!

:build_executable
echo.
echo 🔨 Gerando executável Windows...
echo ⏳ Isso pode levar alguns minutos...

REM Verificar se script de build existe
if not exist "build_executable_windows.bat" (
    echo ❌ Script build_executable_windows.bat não encontrado!
    pause
    exit /b 1
)

REM Executar build
call build_executable_windows.bat

REM Verificar se executável foi criado
if exist "dist\ValidadorNF.exe" (
    echo.
    echo 🎉 SETUP COMPLETO FINALIZADO COM SUCESSO!
    echo.
    echo 📁 Executável criado: dist\ValidadorNF.exe
    echo.
    echo 🚀 PRÓXIMOS PASSOS:
    echo 1. Para criar release distribuível: create_release_windows.bat
    echo 2. Para testar: cd dist ^&^& ValidadorNF.exe
    echo.
    echo ❓ Criar release agora? (s/n)
    set /p create_release="Digite s para SIM ou n para NÃO: "
    
    if /i "%create_release%"=="s" (
        echo 📦 Criando release...
        call create_release_windows.bat
    )
) else (
    echo ❌ Erro ao gerar executável!
    echo 📋 Verifique os logs acima para mais detalhes.
)

:exit_script
echo.
echo 👋 Setup finalizado!
pause
exit /b 0