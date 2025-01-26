from pytube import YouTube
from utils import generate_unique_filename, create_download_directory

class YouTubeService:
    def __init__(self, download_dir='./downloads'):
        self.download_dir = download_dir

    def download_video(self, url, resolution):
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=resolution).first()
            if not stream:
                return False, "ResolutionNotFound", "Video with the specified resolution not found."

            create_download_directory(self.download_dir)
            filename = generate_unique_filename(yt.title)
            filepath = os.path.join(self.download_dir, filename)
            stream.download(output_path=self.download_dir, filename=filename)
            return True, "DownloadSuccess", filepath
        
        except Exception as e:
            return False, "DownloadFailed", str(e)

    def get_video_info(self, url):
         try:
            yt = YouTube(url)
            video_info = {
                "title": yt.title,
                "author": yt.author,
                "length": yt.length,
                "views": yt.views,
                "description": yt.description,
                "publish_date": yt.publish_date,
            }
            return video_info, None
         except Exception as e:
            return None, str(e)