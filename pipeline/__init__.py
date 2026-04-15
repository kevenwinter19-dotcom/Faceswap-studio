from .extract import FrameExtractor
from .detect import FaceDetector
from .swap import SimSwapFaceSwapper
from .enhance import FaceEnhancer
from .smooth import TemporalSmoother
from .lipsync import LipSyncer
from .render import VideoRenderer
import torch

class FaceSwapPipeline:
    def __init__(self, device: str = None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.extractor = FrameExtractor()
        self.detector = FaceDetector(self.device)
        self.swapper = SimSwapFaceSwapper(self.device)
        self.enhancer = FaceEnhancer(self.device)
        self.smoother = TemporalSmoother()
        self.lipsyncer = LipSyncer(self.device)
        self.renderer = VideoRenderer()
    
    def process_video(self, video_path: Path, face_image_path: Path, output_path: Path):
        """Pipeline principal de face swap"""
        # Implementação simplificada para estrutura
        print(f"Processing {video_path} -> {output_path}")
        return str(output_path)
