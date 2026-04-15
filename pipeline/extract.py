import cv2
import ffmpeg
from pathlib import Path
import numpy as np

class FrameExtractor:
    def extract_frames(self, video_path: Path, output_dir: Path, progress_callback=None):
        """Extrai frames do vídeo usando FFmpeg"""
        output_dir.mkdir(exist_ok=True)
        
        stream = ffmpeg.input(str(video_path))
        stream = ffmpeg.output(stream, str(output_dir / '%06d.png'), 
                             vf='fps=30', format='image2', **{'loglevel': 'quiet'})
        ffmpeg.run(stream)
