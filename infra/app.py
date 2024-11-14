import yt_dlp
from time import time

DEFAULT_OPTS =  {
    'writeautomaticsub': True,
    'subtitlesformat': 'ttml',
    'skip_download': True,
    'restrictfilenames': True,
    'outtmpl': {
        'subtitle': '%(upload_date)s_%(title)s.%(ext)s'
    }
}

def download_subs(url, filename=None, yt_opts=None):

    yt_opts = yt_opts or {}
    opts = {**DEFAULT_OPTS, **yt_opts}

    filename = filename or f'{time():.0f}'
    opts['outtmpl']['subtitle'] = f'{filename}.%(ext)s'

    ydl = yt_dlp.YoutubeDL(opts)

    ydl.download(url)
    
    filename_with_ext = f'{filename}.en.ttml'

    with open(filename_with_ext, 'r', encoding='utf-8') as file:
        content = file.read()

    return content

def lambda_handler(event, lambda_context):
    try:
        id = event['queryStringParameters']['videoId']
        subtitle_text = download_subs(f'https://www.youtube.com/watch?v={id}')
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "plain/text"
            },
            "body": subtitle_text
        }
    except Exception:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "plain/text"
            },
            "body": 'Internal Server Error'
        }