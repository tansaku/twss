import sys
import getopt
import pickle
from tokeniseContents import *
from getVocabList import *
import pdb

def processFile(filename):
  file = open(filename)
  sentences = file.readlines()
  text = " ".join(sentences)
  tokens = tokeniseContents(text)
  output = open(filename+".pk","wb")
  pickle.dump(sentences, output)
  output.close()
  return tokens

def preprocessData():
  fml_tokens = processFile('data/fml.txt')
  tfln_tokens = processFile('data/tfln.onesent.txt')
  twss_tokens = processFile('data/twssstories.txt')
  usa_tokens = processFile('data/usaquotes.txt')
  
  vocab = set(fml_tokens+tfln_tokens+twss_tokens+usa_tokens)
  v = sorted(list(vocab))

  f = open('data/vocab.txt', 'w')
  for item in v:
    f.write("%s\n" % item)
  f.close()

  vocabList, vocabArray = getVocabList();
  output = open("data/vocab.pk","wb")
  #pdb.set_trace()
  pickle.dump(vocabList, output)
  pickle.dump(vocabArray, output)
  output.close()
  
class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg
        
# based on Guido's post: http://www.artima.com/weblogs/viewpost.jsp?thread=4829
# might be out of date for 2.7 ...
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
             raise Usage(msg)
        if args:
            raise Usage('python preprocessData.py')
        preprocessData()
        
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())