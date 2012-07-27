from pattern.search import *
from pattern.en import *

def extract(statement):

  s = Sentence(parse(statement, relations=True, lemmata=True, light=True))

  c1 = Constraint.fromstring("There be DT")
  c2 = Constraint.fromstring("NN+")
  c3 = Constraint.fromstring("(DT)")
  c4 = Constraint.fromstring("(RB) (JJ) NNP+")
  c5 = Constraint.fromstring("(call) (DT)")
  c6 = Constraint.fromstring("(RB) (JJ) (NNPS|NNP)+")
  p = Pattern(sequence=[c1, c2, c3, c4, c5, c6]) 
  result = p.search(statement)
  #raise Exception(result)
  return result
  
  
def basicExtract(statement):

  s = Sentence(parse(statement, relations=True, lemmata=True, light=True))
  p = Pattern.fromstring('(DT) (RB) (JJ) NN+')
  result = p.search(s)
  return result
  
def myExtract(statement):

  s = Sentence(parse(statement, relations=True, lemmata=True, light=True))
  p = Pattern.fromstring('There be DT NN+')
  result = p.search(s)
  #raise Exception(result)
  return result
  

def constraintSequenceExtract(statement):

  s = Sentence(parse(statement, relations=True, lemmata=True, light=True))

  c1 = Constraint.fromstring("There be DT")
  c2 = Constraint.fromstring("NN+")
  p = Pattern(sequence=[c1, c2])
  result = p.search(s)
  return result
  #raise Exception(result)

