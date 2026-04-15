@echo off
title FaceSwap Studio - Production Server
color 0A
echo.
echo ========================================
echo    🎭 FaceSwap Studio v1.0.0
echo ========================================
echo.

REM Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado!
    echo Instale Python 3.10+ e adicione ao PATH
    pause
    exit /b 1
)

REM Verificar dependencias
echo [INFO] Verificando dependencias...
pip install -r requirements.txt --quiet --disable-pip-version-check >nul 2>&1

REM Criar diretorios
for %%d in (models input output temp) do (
    if not exist "%%d" mkdir "%%d"
)

REM Verificar CUDA
nvidia-smi >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK]   GPU CUDA detectada
    echo [INFO] Otimizando para GPU...
) else (
    echo [WARN] GPU nao detectada - usando CPU
)

REM Verificar modelos
if not exist "models\buffalo_l" (
    echo [WARN] Modelos nao baixados. Baixe manualmente:
    echo [INFO] InsightFace: pip install insightface
    echo [INFO] SimSwap: models/simswap_512.pth
)

echo.
echo [START] Iniciando servidor em http://localhost:8000
echo [START] Web UI: http://localhost:8000/static/index.html
echo.
echo ========================================
echo.

REM Executar servidor em background com log
start /min cmd /c "python -m backend.main --host 0.0.0.0 --port 8000 --log-level info"

REM Aguardar servidor iniciar
timeout /t 3 /nobreak >nul

REM Abrir navegador automaticamente (Windows)
start http://localhost:8000/static/index.html

echo.
echo [OK] Servidor rodando! Pressione qualquer tecla para parar...
pause >nul

REM Parar servidor (Ctrl+C no terminal do servidor)
taskkill /f /im python.exe /t >nul 2>&1
echo [STOP] Servidor finalizado.
