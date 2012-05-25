def sentenceFeatures(word_indices,vocabList):
  #SENTENCEFEATURES takes in a word_indices vector and produces a feature vector
  #from the word indices
  #   x = SENTENCEFEATURES(word_indices,number_words) takes in a word_indices vector and 
  #   produces a feature vector from the word indices. 

  # Total number of words in the dictionary
  n = len(vocabList)

  # You need to return the following variables correctly.
  x = [0]*n

  # ====================== YOUR CODE HERE ======================
  # Instructions: Fill in this function to return a feature vector for the
  #               given sentence (word_indices). To help make it easier to 
  #               process the sentences, we have have already pre-processed each
  #               sentence and converted each word in the sentence into an index in
  #               a fixed dictionary (of 1899 words). The variable
  #               word_indices contains the list of indices of the words
  #               which occur in one sentence.
  # 
  #               Concretely, if an sentence has the text:
  #
  #                  The quick brown fox jumped over the lazy dog.
  #
  #               Then, the word_indices vector for this text might look 
  #               like:
  #               
  #                   60  100   33   44   10     53  60  58   5
  #
  #               where, we have mapped each word onto a number, for example:
  #
  #                   the   -- 60
  #                   quick -- 100
  #                   ...
  #
  #              (note: the above numbers are just an example and are not the
  #               actual mappings).
  #
  #              Your task is take one such word_indices vector and construct
  #              a binary feature vector that indicates whether a particular
  #              word occurs in the sentence. That is, x(i) = 1 when word i
  #              is present in the sentence. Concretely, if the word 'the' (say,
  #              index 60) appears in the sentence, then x(60) = 1. The feature
  #              vector should look like:
  #
  #              x = [ 0 0 0 0 1 0 0 0 ... 0 0 0 0 1 ... 0 0 0 1 0 ..];
  #
  #


  for word_index in word_indices:
  	x[word_index]=1





# =========================================================================
    

  return x
