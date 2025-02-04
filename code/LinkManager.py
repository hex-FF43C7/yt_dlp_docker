import re
import yt_dlp

class link:
  def __init__(self, line, in_path, out_path):
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

    self.in_path = in_path
    self.out_path = out_path

    def download(self):
      yt_opts = {
          'outtmpl': self.out_path,
          'recode-video': 'mp4',
          'nocheckcertificate': True,
          'postprocessors': [{
              'key': 'FFmpegVideoConvertor',
              'preferedformat': 'mp4'
          }]
      }
      with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download(self.link)
      


    
    
