import os
import subprocess
import sys
from pathlib import Path
import PyInstaller.__main__

def build_desktop_app():
    """Build standalone desktop application"""
    
    # PyInstaller spec
    spec = """
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['backend/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('frontend', 'frontend'),
        ('pipeline', 'pipeline'),
        ('models', 'models'),
        ('config.py', '.')
    ],
    hiddenimports=[
        'torch', 'cv2', 'insightface', 'onnxruntime', 
        'gfpgan', 'realesrgan', 'ffmpeg', 'pydub'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='FaceSwapStudio',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
"""
    
    with open('faceswap.spec', 'w') as f:
        f.write(spec)
    
    PyInstaller.__main__.run([
        'faceswap.spec',
        '--onefile',
        '--windowed',
        '--name', 'FaceSwapStudio',
        '--icon', 'icon.ico'  # Add your icon
    ])

if __name__ == "__main__":
    build_desktop_app()
    print("✅ Desktop app built successfully!")
    print("Run: dist/FaceSwapStudio.exe")
