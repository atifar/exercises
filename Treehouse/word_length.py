import re

def find_words(count, string):
  outwords = re.findall(r'\w{%d,}' % count, string)
  print("Count: {} ({})".format(count, type(count)))
  print(outwords)

inwords = 'dog, cat, baby, raccoon, browls'
find_words(6, inwords)
