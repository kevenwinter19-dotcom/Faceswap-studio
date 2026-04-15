from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
import shutil
from pathlib import Path
import uuid
import asyncio
from pipeline import FaceSwapPipeline
from config import INPUT_DIR, OUTPUT_DIR

router = APIRouter(prefix="/api", tags=["faceswap"])

@router.post("/upload")
async def upload_files(video: UploadFile = File(...), face_image: UploadFile = File(...)):
    session_id = str(uuid.uuid4())
    video_path = INPUT_DIR / f"{session_id}_video.mp4"
    face_path = INPUT_DIR / f"{session_id}_face.jpg"
    
    with open(video_path, "wb") as f:
        shutil.copyfileobj(video.file, f)
    with open(face_path, "wb") as f:
        shutil.copyfileobj(face_image.file, f)
    
    return {"session_id": session_id}

@router.post("/process/{session_id}")
async def process_faceswap(session_id: str):
    video_path = INPUT_DIR / f"{session_id}_video.mp4"
    face_path = INPUT_DIR / f"{session_id}_face.jpg"
    output_path = OUTPUT_DIR / f"{session_id}_result.mp4"
    
    if not video_path.exists() or not face_path.exists():
        raise HTTPException(status_code=400, detail="Files not found")
    
    pipeline = FaceSwapPipeline()
    result = pipeline.process_video(video_path, face_path, output_path)
    
    return {"status": "complete", "output": str(output_path)}

@router.get("/status/{session_id}")
async def get_status(session_id: str):
    output_path = OUTPUT_DIR / f"{session_id}_result.mp4"
    return {"ready": output_path.exists()}

@router.get("/download/{session_id}")
async def download_result(session_id: str):
    output_path = OUTPUT_DIR / f"{session_id}_result.mp4"
    if not output_path.exists():
        raise HTTPException(status_code=404)
    return FileResponse(output_path, filename=f"faceswap_{session_id}.mp4")
