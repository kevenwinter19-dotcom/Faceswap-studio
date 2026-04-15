import os
import uuid
import torch
import cv2
import numpy as np
from pathlib import Path
from config import TEMP_DIR

def generate_temp_path(suffix: str) -> Path:
    session_id = str(uuid.uuid4())[:8]
    return TEMP_DIR / f"{session_id}_{suffix}"

def load_model_safely(model_path: Path, map_location=None):
    if not model_path.exists():
        print(f"Model missing: {model_path}")
        return None
    return torch.load(model_path, map_location=map_location)

def preprocess_frame(frame: np.ndarray, size=512) -> np.ndarray:
    h, w = frame.shape[:2]
    scale = size / min(h, w)
    new_w, new_h = int(w * scale), int(h * scale)
    
    frame_resized = cv2.resize(frame, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
    start_x = (new_w - size) // 2
    start_y = (new_h - size) // 2
    cropped = frame_resized[start_y:start_y+size, start_x:start_x+size]
    
    return cropped

def create_gaussian_mask(size: tuple, blur_sigma: float = 20) -> np.ndarray:
    h, w = size[:2]
    center = (w // 2, h // 2)
    y, x = np.ogrid[:h, :w]
    mask = np.exp(-((x - center[0])**2 + (y - center[1])**2) / (2.0 * blur_sigma**2))
    mask = mask / np.max(mask)
    return mask.astype(np.float32)
