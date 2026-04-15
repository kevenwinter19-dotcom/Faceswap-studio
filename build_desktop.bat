@echo off
title FaceSwap Studio - Build Desktop
color 0B

echo ========================================
echo  🖥️  Build Desktop Application
echo ========================================
echo.

REM Verificar PyInstaller
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Instalando PyInstaller...
    pip install pyinstaller
)

echo [BUILD] Criando executavel...
pyinstaller --onefile --windowed ^
    --add-data "frontend;frontend" ^
    --add-data "pipeline;pipeline" ^
    --add-data "models;models" ^
    --add-data "backend;backend" ^
    --hidden-import=torch ^
    --hidden-import=cv2 ^
    --hidden-import=insightface ^
    --name "FaceSwapStudio" ^
    backend/main.py

if %errorlevel% equ 0 (
    echo.
    echo [OK] Build concluido!
    echo [OK] Executavel: dist/FaceSwapStudio.exe
    echo.
    echo ========================================
    pause
) else (
    echo [ERRO] Build falhou!
    pause
)
