@echo off
title FaceSwap Studio - Download Models
color 0E

echo ========================================
echo     📥 Download Models
echo ========================================
echo.

REM Criar diretorio models
if not exist "models" mkdir models

echo [INFO] InsightFace models (automatico)...
python -c "from insightface.app import FaceAnalysis; print('InsightFace OK')"

echo [INFO] SimSwap model...
REM wget nao nativo no Windows, usar PowerShell
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/neuralchen/SimSwap/releases/download/1.0.0/simswap_512.pth' -OutFile 'models\simswap_512.pth'"

echo [INFO] CodeFormer...
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/codeformer.pth' -OutFile 'models\codeformer.pth'"

echo.
echo [OK] Models baixados!
echo [INFO] Alguns downloads podem precisar de confirmacao manual
pause
