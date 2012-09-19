from pattern.search import search, Pattern, Constraint
from pattern.en import Sentence, parse
#from patten.en.tree import Word

MATCH_STRING = "There be DT {JJ? NN+} {NNP+} (call DT? {JJ? NNP+})"

def extract(statement):

  s = Sentence(parse(statement, lemmata=True))

  '''c1 = Constraint.fromstring("There be DT")
  c2 = Constraint.fromstring("NN+")
  c3 = Constraint.fromstring("(DT)")
  c4 = Constraint.fromstring("(RB) (JJ) NNP+")
  c5 = Constraint.fromstring("(call) (DT)")
  c6 = Constraint.fromstring("(RB) (JJ) (NNPS|NNP)+")
  p = Pattern(sequence=[c1, c2, c3, c4, c5, c6]) 
 
  match = p.search(s)
   '''
  s = find_entities(s)
   
   # not sure about this "be" thing - happy to match plural (is/are) but not sure about past tense ...
  match = search(MATCH_STRING, s)
  #raise Exception(match)
  return s, match
  
def find_entities(sentence):
  """ Returns a copy of the given Sentence,
  where capitalized nouns are tagged as NNP (except first word of sentence).
  """
  #sentence = sentence.copy()
  for word in sentence.words:
    if word.string[0].isupper() and word.tag == "NN" and word.index > 0:
      word.type = "NNP"
    if word.string[0].islower() and word.tag == "NNP" and word.index > 0:
      # okay, so this was really weird - there were two versions of the word Class with 
      # word.tag being for the one that isn't
      # used here and word.type being the one that worked ...
      word.type = "NN" #= Word(sentence,word.string,tag="NN",index = word.index)
      #raise Exception(word.string +", " +str(word))
  return sentence  
  # so without the above whether we treat "engine" as an NNP or an NN seems to depend on the name that follows
  # which seems very odd - I want capital letters to indicate NNPs consistently
  # failing that I want to have any database table match indicate a pure NN ...., e.g. "game engine"
  # TODO implement this latter as it will be more stable in the long run I think?
  
  
def basicExtract(statement):

  #s = Sentence(parse(statement, relations=True, lemmata=True, light=True))
  #p = Pattern.fromstring('(DT) (RB) (JJ) NN+')
  s = Sentence(parse(statement, lemmata=True))
  m = search("There be DT {JJ? NN}", s)
  return m
''' #never could get constraint based searches to work
def basicConstraintSequenceExtract(statement):

  s = Sentence(parse(statement, lemmata=True))
  c1 = Constraint.fromstring("(DT) (RB)")
  c2 = Constraint.fromstring("(JJ) NN+")
  p = Pattern(sequence=[c1, c2])
  match = p.search(s)
  return match
'''

def myExtract(statement):

  s = Sentence(parse(statement, relations=True, lemmata=True, light=True))
  p = Pattern.fromstring('There be DT NN+')
  match = p.search(s)
  #raise Exception(match)
  return match
  
''' #never could get constraint based searches to work
def constraintSequenceExtract(statement):

  s = Sentence(parse(statement, lemmata=True))

  c1 = Constraint.fromstring("There be DT")
  c2 = Constraint.fromstring("JJ? NN+")
  p = Pattern(sequence=[c1, c2])
  match = p.search(s)
  return match
  #raise Exception(match)
'''

