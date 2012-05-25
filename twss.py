import sys
import getopt
from processSentence import *
from svmutil import *
import pickle
import random

def twss(sentence,vocabList,model):
    #print "you said: '"+sentence+"'\n"
    # these should be moved to file
    responses = ['Whatever ...','Okay','Yawn','What makes you think I care?','Yada yada','Uhuh','Yeah, yeah','figures',"I'm hungry",'give me a break','so ...']
    x  = processSentence(sentence, vocabList)
    #print [x]
    p_label, p_acc, p_val = svm_predict([1], [x], model, '-b 1 -q')
    #print p_label, p_acc, p_val
    if p_label[0] == 1:
        print "That's what she said!\n"
    else:
        print random.choice(responses) +'\n'   

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
        input = open('data/vocab.pk')
        vocabList = pickle.load(input)
        input.close()
        model = svm_load_model("data/svm_model.pk")
        if not args:
            raise Usage('python twss.py "<your sentence>"')
        twss(args[0],vocabList,model)
        
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())