import os
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
TEMP_DIR = BASE_DIR / "temp"

for directory in [MODELS_DIR, INPUT_DIR, OUTPUT_DIR, TEMP_DIR]:
    directory.mkdir(exist_ok=True)

class Config:
    INSIGHTFACE_MODEL = MODELS_DIR / "buffalo_l"
    SIMSWAP_MODEL = MODELS_DIR / "simswap_512.pth"
    CODEFORMER_MODEL = MODELS_DIR / "codeformer"
    WAV2LIP_MODEL = MODELS_DIR / "wav2lip_gan.pth"
    
    FPS = 30
    BATCH_SIZE = 8
    FACE_UPSAMPLE = 512
    FIDELITY = 0.75
    
    EMA_ALPHA = 0.7
    FLOW_ALPHA = 0.3
    
    @classmethod
    def get_device(cls):
        import torch
        return "cuda" if torch.cuda.is_available() else "cpu"
