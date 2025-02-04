import yt_dlp
import os
from colorama import Fore
from yt_dlp.postprocessor import FFmpegPostProcessor
import time

def rel_path(rel):
    return os.path.normpath(os.path.join(os.path.dirname(__file__), rel))

IN_PATH = rel_path('../input/catalog.txt')
# OUT_PATH = rel_path('../output')
ffmpeg_path = '/bin/ffmpeg'
FFmpegPostProcessor._ffmpeg_location.set(ffmpeg_path)

yt_opts = {
    'outtmpl': rel_path('../output/%(title)s.%(ext)s'),
    'recode-video': 'mp4',
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4'
    }]
}

with open(IN_PATH, 'r') as file:
    cat = [i.strip('\n') for i in file.readlines()]

print(cat)

with yt_dlp.YoutubeDL(yt_opts) as ydl:
    count = 1
    for link in cat:
        print(f'{Fore.MAGENTA}{count}/{len(cat)}')
        print(Fore.RESET)
        ydl.download(link)
        count += 1
        # pass