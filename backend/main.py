from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import router
from websocket import router as ws_router
from config import OUTPUT_DIR, INPUT_DIR

app = FastAPI(title="FaceSwap Studio", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="../frontend"), name="static")
app.include_router(router)
app.include_router(ws_router)

@app.get("/")
async def root():
    return {"message": "FaceSwap Studio API - Visit /static/index.html"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
