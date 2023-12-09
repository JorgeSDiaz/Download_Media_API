import services.download_media_service as download_service
from fastapi import FastAPI

app = FastAPI(
    title="Download Media API",
    description="An api to download videos and audios from youtube",
    version="0.1.0"
    )

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok"}

@app.get("/qualities", tags=["Download"])
def get_qualities(url: str) -> dict:
    return {"qualities": download_service.list_qualities(url)}

@app.post("/download/video", tags=["Download"])
def download_video(url: str, resolution: str, fps: int):
    download_service.download_video(url, resolution, fps)
