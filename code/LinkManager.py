import re
import yt_dlp
from yt_dlp.utils import download_range_func
from yt_dlp.postprocessor import FFmpegPostProcessor
import requests
from bs4 import BeautifulSoup
import os

class link:
  def __init__(self, line, out_path):
    key = r"^(?P<link>(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]))( \(((?P<start>(\d\d:\d\d:\d\d)|[B,b]), ?(?P<stop>(\d\d:\d\d:\d\d)|[E,e]))\))?$"
    # goups link, start, stop
    
    match = re.match(key, line.strip())
    try:
      self.link = match.group('link')
    except AttributeError:
      raise ValueError(f"Invalid Syntax: {line}")
    
    try:
      self.start = match.group('start')
    except AttributeError:
      self.start = 'B'
    
    try:
      self.stop = match.group('stop')
    except AttributeError:
      self.stop = 'E'

    self.out_path = out_path
    self.name = self.get_name()

  def get_name(self):
    r = requests.get(self.link)
    soup = BeautifulSoup(r.text)

    link = soup.find_all(name="title")[0]
    title = str(link)
    title = re.sub(r"</?title>", "")
    title = title.replace(" - YouTube", "")
    title = re.sub(r'^\(\d*\) ?', '', title)
    title = title.replace(" ", "_")
    title = re.sub(r'[<>:"/\\|?*\.]', '', title)

    return title

  def download(self):
    if self.start == 'B':
      start_time = 0
    else:
      start_time = self.start
    
    if self.stop == 'E':
      end_time = None
    else: 
      end_time = self.stop
    
    ffmpeg_path = '/bin/ffmpeg'
    FFmpegPostProcessor._ffmpeg_location.set(ffmpeg_path)

    yt_opts = {
        'outtmpl': os.path.normpath(self.out_path, f'{self.name}.%(ext)s'),
        'recode-video': 'mp4',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
        'download_ranges': download_range_func(None, [(start_time, end_time)]),
        'force_keyframes_at_cuts': True,
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
      ydl.download(self.link)
      


    
    
