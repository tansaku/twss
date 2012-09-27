import unittest
import os
from extractor import *

class TestExtractor(unittest.TestCase):

  def checkExtraction(sentence,type,name):
    pass

  def testSource(self):
    sentence = "There is a game engine Source"
    s, match = extract(sentence)
    self.assertNotEqual(len(match),0,"no match found: '" + str(s)+"' against '"+ MATCH_STRING + "' or '"+ MATCH_STRING_EXT + "'") 
    self.assertEqual(match[0].group(1).string,"game engine","from '" + str(s)+"'")
    self.assertEqual(match[0].group(2).string,"Source","from '" + str(s)+"'")
    
  def testUnrealEngine(self):
    sentence = "There is a game engine Unreal Engine"
    s, match = extract(sentence)
    self.assertNotEqual(len(match),0,"no match found: '" + str(s)+"' against '"+ MATCH_STRING + "' or '"+ MATCH_STRING_EXT + "'")
    self.assertEqual(match[0].group(1).string,"game engine","game engine is not "+match[0].group(1).string+" from'" + str(s)+"'")
    self.assertEqual(match[0].group(2).string,"Unreal Engine","Unreal Engine is not "+match[0].group(2).string+" from '" + str(s)+"'")
  # not sure how we make sure we greedy grab two NNPs here ...
  
  def testUnity3D(self):
    sentence = "There is a game engine Unity3D called Unity3D"
    s, match = extract(sentence)
    self.assertNotEqual(len(match),0,"no match found: '" + str(s)+"' against '"+ MATCH_STRING + "' or '"+ MATCH_STRING_EXT + "'")
    firstHit = match[0].group(1).string
    self.assertEqual(len(match[0].pattern.groups),3, "incorrect number of groups: '" +str(len(match[0].pattern.groups))+"; "+ str(s)+"' against '"+ "' or '"+ MATCH_STRING_EXT + "'")
    self.assertEqual(match[0].group(1).string,"game engine", "found '" +firstHit+ "' instead of 'game engine' in '" + sentence+"'")
    self.assertEqual(match[0].group(2).string,"Unity3D","'" + str(s)+"'") 
    #raise Exception(str(s))
    # annoying - no way to get the number of groups ... aha ... match[0].pattern.groups
    #seems like () and {} do not play well together ...
    self.assertEqual(match[0].group(3).string,"Unity3D","Unity3D is not '" + match[0].group(3).string+"' from " + str(s))    

  def testMachineLearning(self):
    sentence = "There is a course Machine Learning called ML"
    s, match = extract(sentence)
    self.assertNotEqual(len(match),0,"no match found: '" + str(s)+"' against '"+ MATCH_STRING + "' or '"+ MATCH_STRING_EXT + "'") 
    firstHit = match[0].group(1).string
    self.assertEqual(len(match[0].pattern.groups),3, "incorrect number of groups: '" +str(len(match[0].pattern.groups))+"; "+ str(s)+"' against '"+ "' or '"+ MATCH_STRING_EXT + "'")
    self.assertEqual(match[0].group(1).string,"course", "found '" +firstHit+ "' instead of 'course' in '" + sentence+"'")
    self.assertEqual(match[0].group(2).string,"Machine Learning","'" + str(s)+"'") 

    self.assertEqual(match[0].group(3).string,"ML","ML is not '" + match[0].group(3).string+"' from " + str(s))
 


  def testBasicExtract(self):
    match = basicExtract('There is a red ball')
    self.assertNotEqual(len(match),0,"no match found")
    
  def testMyExtract(self):
    match = myExtract("There is a game engine")
    self.assertNotEqual(len(match),0,"no match found")
    
'''  #never could get constraint based searches to work
  def testBasicConstraintSequenceExtract(self):
    sentence = 'tasty cat food'
    match = basicConstraintSequenceExtract(sentence)
    self.assertNotEqual(len(match),0,"no match found: '" + sentence +"'")
'''


    
''' #never could get constraint based searches to work
  def testConstraintSequenceExtract(self):
    sentence = "There is a game engine"
    match = constraintSequenceExtract(sentence)
    self.assertNotEqual(len(match),0,"no match found: '" + sentence +"'")
'''

    #Crysis - said no to use in an online class
    #Unity3d - http://www.studica.com/unity
    #Source http://source.valvesoftware.com/sourcesdk/sourceu.php
    #Unreal engine
    #Game Maker
    #Game Salad
    #Scirra
    #Torque 3d