import yt_dlp
import os

def download_song(query):
    os.makedirs("downloads", exist_ok=True)
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'writethumbnail': True,
        'embed-thumbnail': True,
        'quiet': True,
        'noprogress': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
        title = info['title']
        artist = info.get('uploader', 'Unknown')
        duration = int(info.get('duration', 0))
        thumb_url = info.get('thumbnail')

        thumb_path = None
        for ext in ['jpg', 'webp']:
            possible = f"downloads/{title}.{ext}"
            if os.path.exists(possible):
                thumb_path = possible
                break

        return {
            'title': title,
            'artist': artist,
            'duration': f"{duration//60}:{duration%60:02d}",
            'filepath': f"downloads/{title}.mp3",
            'thumbnail': thumb_path or 'default.jpg'
        }
