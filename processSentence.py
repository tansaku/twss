from tokeniseContents import *
import pdb

def processSentence(sentence,vocabList):
  #PROCESSSENTENCE preprocesses a sentence and
  #returns a list of word_indices 
  #   word_indices = PROCESSSENTENCE(sentence,vocabList) preprocesses 
  #   a sentence and returns a list of indices of the 
  #   words contained in the sentence, based on the vocabList. 
  #

  # Init return value
  word_indices = {}

  # ========================== Tokenize Sentence ===========================

  tokens = tokeniseContents(sentence)

  # Process file
  l = 0

  for token in tokens:

      # Skip the word if it is too short
      if len(token) < 1:
         continue

      # Look up the word in the dictionary and add to word_indices if
      # found
      # ====================== YOUR CODE HERE ======================
      # Instructions: Fill in this function to add the index of str to
      #               word_indices if it is in the vocabulary. At this point
      #               of the code, you have a stemmed word from the email in
      #               the variable str. You should look up str in the
      #               vocabulary list (vocabList). If a match exists, you
      #               should add the index of the word to the word_indices
      #               vector. Concretely, if str = 'action', then you should
      #               look up the vocabulary list to find where in vocabList
      #               'action' appears. For example, if vocabList{18} =
      #               'action', then, you should add 18 to the word_indices 
      #               vector (e.g., word_indices = [word_indices ; 18]; ).
      # 
      # Note: vocabList{idx} returns a the word with index idx in the
      #       vocabulary list.
      # 
      # Note: You can use strcmp(str1, str2) to compare two strings (str1 and
      #       str2). It will return 1 only if the two strings are equivalent.
      #



  #keyboard
      #pdb.set_trace()
      index = vocabList.get(token)
      if index is not None:
        word_indices.update({index:1})


      # =============================================================


      # Print to screen, ensuring that the output lines are not too long
      #if l + len(token) + 1 > 78:
          #print '\n'
          #l = 0
      #print token
      #l = l + len(token) + 1

  # Print footer
  #fprintf('\n\n=========================\n');

  return word_indices
