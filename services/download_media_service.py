from pytube import YouTube, StreamQuery


def get_stream_orderBy_resolution(url:str) -> StreamQuery:
    yt = YouTube(url)
    return yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc()


def list_qualities(url: str) -> list[str]:
    return list(map(lambda x: f"{x.resolution}: {x.fps}FPS", get_stream_orderBy_resolution(url)))


def download_video(url: str, resolution: str, fps: int):
    stream = get_stream_orderBy_resolution(url);
    video = filter(lambda x: (x.resolution == resolution and x.fps == fps), stream)
    
    try:
        video.download(output_path="../downloads/")
    except Exception as e:
        raise Exception("Error on download video") from e
