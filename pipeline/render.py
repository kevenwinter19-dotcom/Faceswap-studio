import cv2
from pathlib import Path
import ffmpeg

class VideoRenderer:
    def frames_to_video(self, frames: list, output_path: Path, reference_video: Path):
        height, width = frames[0].shape[:2]
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(str(output_path), fourcc, 30.0, (width, height))
        for frame in frames:
            out.write(frame)
        out.release()
