def getVocabList():
  '''reads the fixed vocabulary list in vocab.txt and returns a dictionary mapping strings to integers'''

  # Read the fixed vocabulary list
  fid = open('data/vocab.txt')
  vocabArray = fid.readlines()

  # use dictionary to map the strings => integers

  vocabList = {}
  for i,vocab in enumerate(vocabArray):
      vocabList[vocab.rstrip()]=i;

  fid.close();

  return vocabList, vocabArray