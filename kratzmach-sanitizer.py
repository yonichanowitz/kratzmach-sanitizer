class KratzmachSanitizer:
  """takes a string and returns the string
  sans any not chanukadikeh words, converted to 
  appropriate words"""
  import re
  chapper = re.compile('/(kratz|christ|x)ma(s|ch)|noel|yule/i')
  gut_vort = "Chanukah"
  def sanitize(self, shmutzy_string):
    return shmutzy_string.replace(chapper, gut_vort)
