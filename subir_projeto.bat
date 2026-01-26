@echo off
echo --- Verificando instalação do Git ---
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] O Git nao foi encontrado!
    echo Por favor, instale o Git baixando de: https://git-scm.com/download/win
    echo Apos instalar e reiniciar o computador, execute este arquivo novamente.
    pause
    exit /b
)

echo.
echo --- Inicializando Repositorio ---
git init

echo.
echo --- Adicionando arquivos ---
git add .

echo.
echo --- Criando Commit Inicial ---
git commit -m "Upload inicial: Pipeline RAG Outline"

echo.
echo --- Configurando Branch Principal ---
git branch -M main

echo.
echo --- Configurando Repositorio Remoto ---
rem Remove origin caso ja exista para evitar erro de duplicidade
git remote remove origin >nul 2>&1
git remote add origin https://github.com/victorhugosdj/Projetos-.git

echo.
echo --- Enviando para o GitHub (Push) ---
git push -u origin main

echo.
echo [SUCESSO] Processo finalizado!
pause
