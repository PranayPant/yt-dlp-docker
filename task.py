import yt_dlp
from time import time
import logging

logger = logging.getLogger()

DEFAULT_OPTS =  {
    'writeautomaticsub': True,
    'subtitlesformat': 'ttml',
    'skip_download': True,
    'restrictfilenames': True,
    'outtmpl': {
        'subtitle': '%(upload_date)s_%(title)s.%(ext)s'
    }
}

def download_subs(url: str, filename: str | None = None, yt_opts=None):
    print('DOWNLOAD METHOD')
    yt_opts = yt_opts or {}
    opts = {**DEFAULT_OPTS, **yt_opts}

    filename = filename or f'{time():.0f}'
    opts['outtmpl']['subtitle'] = f'{filename}.%(ext)s'

    ydl = yt_dlp.YoutubeDL(opts)
    
    logger.info('DOWNLOAD_SUBS', url, opts)
    
    ydl.download(url)
    
    filename_with_ext = f'{filename}.en.ttml'

    with open(filename_with_ext, 'r', encoding='utf-8') as file:
        content = file.read()

    return content