from pytube import YouTube

def list_qualities(url: str) -> list:
    yt = YouTube(url)
    return list(map(lambda x: f"{x.resolution}: {x.fps}FPS", yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc()))