import re
class link:
  def __init__(line):
    key = r"^(?P<link>(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-]))( \(((?P<start>(\d\d:\d\d:\d\d)|[B,b]), ?(?P<stop>(\d\d:\d\d:\d\d)|[E,e]))\))?$"gm
    # goups link, start, stop
    
    
