import cv2
import numpy as np
from insightface.app import FaceAnalysis

class FaceDetector:
    def __init__(self, device: str = "cpu"):
        self.device = device
        self.app = FaceAnalysis(name='buffalo_l', providers=['CUDAExecutionProvider' if device == 'cuda' else 'CPUExecutionProvider'])
        self.app.prepare(ctx_id=0, det_size=(640, 640))
    
    def detect_faces(self, frame: np.ndarray):
        faces = self.app.get(frame)
        return [{'bbox': f.bbox, 'kps': f.kps, 'embedding': f.normed_embedding} for f in faces]
    
    def align_face(self, frame: np.ndarray, face_info: dict, size: int = 512):
        kps = face_info['kps'].astype(np.float32)
        src_pts = kps
        dst_pts = np.float32([[size//2, size//4], [size//2, size//2], [size//2, 3*size//4],
                             [size//4, size//2], [3*size//4, size//2]])
        
        M = cv2.estimateAffinePartial2D(src_pts, dst_pts)[0]
        aligned = cv2.warpAffine(frame, M, (size, size), flags=cv2.INTER_LANCZOS4)
        return aligned, M
