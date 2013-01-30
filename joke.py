from urllib import FancyURLopener
from random import random
import pdb
import re

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

class MyOpener(FancyURLopener):
  version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


def grabJoke(cleanliness, keyword):
  myopener = MyOpener()
  seed = random() * 100
  try:
    page = myopener.open('http://www.joke-db.com/widgets/src/wp/%s/%s/%s'%(cleanliness,keyword,seed))
    result = page.read()
    #print result
    match = re.search(r'document\.getElementById\("jotda-output"\)\.innerHTML = "(.*)";',result)
    final = strip_tags(match.group(1))
  except IOError as e:
    final = "I'm sorry I currently rely on my internet subconcious to generate jokes and all I'm getting is: '%s'" % e
  return final

if __name__ == "__main__":
  cleanliness = 'clean'
  keyword = 'apple'
  print grabJoke(cleanliness, keyword)

