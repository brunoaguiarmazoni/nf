@echo off
echo 🚀 GERADOR DE EXECUTÁVEL WINDOWS - Validador NF-e/NFS-e
echo =========================================================

REM Verificar se está no diretório correto
if not exist "main.py" (
    echo ❌ Erro: Execute este script no diretório do projeto!
    pause
    exit /b 1
)

REM Criar diretórios
if not exist "build" mkdir build
if not exist "dist" mkdir dist

echo.
echo 📦 Verificando Python...
python --version
if %ERRORLEVEL% neq 0 (
    echo ❌ Python não encontrado! Instale Python 3.8+ primeiro.
    pause
    exit /b 1
)

echo.
echo 📦 Instalando PyInstaller...
pip install pyinstaller

echo.
echo 🔨 Gerando executável Windows...
echo Isso pode levar alguns minutos...

REM Limpar builds anteriores
if exist "build\ValidadorNF" rmdir /s /q "build\ValidadorNF"
if exist "dist\ValidadorNF.exe" del "dist\ValidadorNF.exe"

REM Gerar executável usando spec file
pyinstaller --clean ValidadorNF_Windows.spec

REM Verificar se foi gerado com sucesso
if exist "dist\ValidadorNF.exe" (
    echo.
    echo ✅ EXECUTÁVEL WINDOWS GERADO COM SUCESSO!
    echo.
    echo 📁 Localização: dist\ValidadorNF.exe
    dir dist\ValidadorNF.exe
    echo.
    echo 📋 Como usar:
    echo 1. Navegue até a pasta 'dist\'
    echo 2. Execute ValidadorNF.exe
    echo.
    echo 🧪 Para testar:
    echo cd dist
    echo ValidadorNF.exe
) else (
    echo.
    echo ❌ ERRO ao gerar executável Windows!
    echo Verifique os logs acima para mais detalhes.
    echo.
    echo 🔧 Possíveis soluções:
    echo 1. Verifique se todas as dependências estão instaladas
    echo 2. Execute: pip install -r requirements.txt
    echo 3. Tente: pip install --upgrade pyinstaller
    pause
    exit /b 1
)

echo.
echo 📦 Para criar versão distribuível:
echo call create_release_windows.bat
echo.
pause