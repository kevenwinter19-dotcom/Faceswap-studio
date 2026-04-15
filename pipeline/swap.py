import torch
import cv2
import numpy as np
from detect import FaceDetector
from utils import create_gaussian_mask

class SimSwapFaceSwapper:
    def __init__(self, device: str):
        self.device = device
        self.detector = FaceDetector(device)
    
    def swap_faces(self, source_frame: np.ndarray, target_frame: np.ndarray, source_embedding: np.ndarray):
        source_faces = self.detector.detect_faces(source_frame)
        target_faces = self.detector.detect_faces(target_frame)
        
        if not source_faces or not target_faces:
            return target_frame
        
        source_face = source_faces[0]
        target_face = target_faces[0]
        
        target_aligned, target_M = self.detector.align_face(target_frame, target_face)
        
        # Simulação do swap (implementar modelo real)
        swapped = target_aligned.copy()  # Placeholder
        
        result = self._blend_face(swapped, target_frame, target_M, target_face['bbox'])
        return result
    
    def _blend_face(self, swapped_face: np.ndarray, original_frame: np.ndarray, 
                   M: np.ndarray, bbox: np.ndarray):
        h, w = original_frame.shape[:2]
        warped_swapped = cv2.warpAffine(swapped_face, M, (w, h))
        
        mask = create_gaussian_mask((h, w), blur_sigma=25)
        mask = cv2.warpAffine(mask, M, (w, h))
        
        mask_3ch = np.stack([mask]*3, axis=2)
        blended = (mask_3ch * warped_swapped + (1 - mask_3ch) * original_frame)
        return blended.astype(np.uint8)
