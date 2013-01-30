import nltk
from nltk.corpus import stopwords
from faq import query, greetings
from twss import *
from joke import grabJoke

if __name__ == "__main__":
  input = open('data/vocab.pk')
  vocabList = pickle.load(input)
  input.close()
  model = svm_load_model("data/svm_model.pk")
  n = ""
  print greetings()
  while True:
    n = raw_input("> ")
    if n in ["quit","exit","stop"]:
      break;
      # ideally we'd offer the faq the chance to answer with TWSS after we have checked all the database things
      # as a way to avoid going straight to a google query - again we want to avoid repeating a TWSS too soon 
      # in a row - need a conversation history ...
    if twss_lite(n,vocabList,model) == 1:
      print "That's what she said!" 
    elif "joke" in n:
      userSplit = re.split(r'\W+',n)
      stoppedUserSplit = [w for w in userSplit if not w in stopwords.words('english')]
      #print stoppedUserSplit[-1]
      joke = grabJoke('clean',stoppedUserSplit[-1])
      if "ERROR" in joke:
        print "Sorry, I don't know any"
      else:
        print joke
    else:
      print query(n)
  
