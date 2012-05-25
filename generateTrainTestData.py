import sys
import getopt
import pickle
from processSentence import * 
from sentenceFeatures import * 

def generateFeatures(filename,label,vocabList,X,y,Xtest,ytest):
    input = open(filename);
    sentences = pickle.load(input)
    input.close()
    # leave last 100 for test set
    top = len(sentences)-100
    for i in range(top):
        wi = processSentence(sentences[i],vocabList)
        X = X+[wi]
        y = y+[label]
    bottom = top
    top = len(sentences)
    for i in range(bottom,top):
        wi = processSentence(sentences[i],vocabList)
        Xtest = Xtest + [wi]
        ytest = ytest + [label]
    return X,y,Xtest,ytest
        
def generateTrainTestData():
    # need to get all sentences into X y form ...
    input = open('data/vocab.pk');
    vocabList = pickle.load(input)
    input.close()
    Xtest = []
    ytest = []
    X = []
    y = []
    X,y,Xtest,ytest = generateFeatures('data/fml.txt.pk',-1,vocabList,X,y,Xtest,ytest)
    X,y,Xtest,ytest = generateFeatures('data/tfln.onesent.txt.pk',-1,vocabList,X,y,Xtest,ytest)
    X,y,Xtest,ytest = generateFeatures('data/twssstories.txt.pk',1,vocabList,X,y,Xtest,ytest)
    X,y,Xtest,ytest = generateFeatures('data/usaquotes.txt.pk',-1,vocabList,X,y,Xtest,ytest)
    output = open('data/train.pk',"wb")
    pickle.dump(X, output)
    pickle.dump(y, output)
    output.close()
    output = open('data/test.pk',"wb")
    pickle.dump(Xtest, output)
    pickle.dump(ytest, output)
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
            raise Usage('python generateTrainTestData.py')
        generateTrainTestData()
        
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())