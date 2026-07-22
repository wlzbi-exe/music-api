from pathlib import Path
from yt_dlp import YoutubeDL

DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)


class Downloader:

    def __init__(self):

        self.options = {
            "format": "bestaudio/best",
            "outtmpl": str(DOWNLOAD_DIR / "%(id)s.%(ext)s"),
            "quiet": True,
            "noplaylist": True
        }

    async def download(self, video_id: str):

        url = f"https://www.youtube.com/watch?v={video_id}"

        with YoutubeDL(self.options) as ydl:

            info = ydl.extract_info(url, download=True)

            filename = ydl.prepare_filename(info)

        return {
            "id": info.get("id"),
            "title": info.get("title"),
            "filename": filename
        }


downloader = Downloader()