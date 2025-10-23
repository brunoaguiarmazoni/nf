@echo off
echo 📦 CRIANDO RELEASE WINDOWS - Validador NF-e/NFS-e
echo ===================================================

REM Verificar se executável existe
if not exist "dist\ValidadorNF.exe" (
    echo ❌ Executável não encontrado!
    echo Execute primeiro: build_executable_windows.bat
    pause
    exit /b 1
)

REM Criar diretório de release
if exist "release_windows" rmdir /s /q release_windows
mkdir release_windows

echo.
echo 📂 Copiando arquivos necessários...

REM Copiar executável principal
copy "dist\ValidadorNF.exe" "release_windows\"

REM Copiar documentação
copy "README.md" "release_windows\"
copy "requirements.txt" "release_windows\"

REM Copiar exemplos se existirem
if exist "examples" (
    mkdir "release_windows\examples"
    xcopy "examples\*" "release_windows\examples\" /E /I /Y
) else (
    echo ℹ️  Criando exemplo básico...
    mkdir "release_windows\examples"
    python create_example.py
    if exist "exemplo_planilha_nf.xlsx" (
        copy "exemplo_planilha_nf.xlsx" "release_windows\examples\"
        del "exemplo_planilha_nf.xlsx"
    )
)

REM Criar arquivo de instruções Windows
echo # 🚀 Validador NF-e/NFS-e - Versão Windows > release_windows\INSTRUÇÕES.md
echo. >> release_windows\INSTRUÇÕES.md
echo ## Como usar: >> release_windows\INSTRUÇÕES.md
echo 1. **Execute ValidadorNF.exe** >> release_windows\INSTRUÇÕES.md
echo 2. **Selecione sua planilha Excel** com as chaves >> release_windows\INSTRUÇÕES.md
echo 3. **Escolha o tipo de validação** (NF-e ou NFS-e) >> release_windows\INSTRUÇÕES.md
echo 4. **Aguarde o processamento** >> release_windows\INSTRUÇÕES.md
echo. >> release_windows\INSTRUÇÕES.md
echo ## 📋 Formato da Planilha: >> release_windows\INSTRUÇÕES.md
echo - **Coluna A**: Chaves das Notas Fiscais >> release_windows\INSTRUÇÕES.md
echo - **Coluna B**: Status (será preenchido automaticamente) >> release_windows\INSTRUÇÕES.md
echo. >> release_windows\INSTRUÇÕES.md
echo ## 🔧 Suporte: >> release_windows\INSTRUÇÕES.md
echo - Verifique o arquivo README.md para mais detalhes >> release_windows\INSTRUÇÕES.md
echo - Logs são salvos automaticamente na pasta logs/ >> release_windows\INSTRUÇÕES.md

REM Obter tamanho do executável
for %%I in ("release_windows\ValidadorNF.exe") do set size=%%~zI
set /a size_mb=%size%/1024/1024

echo.
echo ✅ RELEASE WINDOWS CRIADO COM SUCESSO!
echo.
echo 📁 Pasta: release_windows\
echo 📊 Tamanho do executável: %size_mb% MB
echo.
echo 📋 Conteúdo do release:
dir /b release_windows

echo.
echo 🚀 PRONTO PARA DISTRIBUIÇÃO!
echo.
echo 📦 Para compactar:
echo 1. Clique com botão direito na pasta 'release_windows'
echo 2. Selecione 'Enviar para' -^> 'Pasta compactada'
echo 3. Ou use 7-Zip/WinRAR para criar um arquivo ZIP
echo.
pause