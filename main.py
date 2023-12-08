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
def get_qualities(url: str) -> list:
    return download_service.list_qualities(url)