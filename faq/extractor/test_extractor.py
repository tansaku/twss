import unittest
import os
from extractor import *

class TestExtractor(unittest.TestCase):
    
  def testUnrealEngine(self):
    match = extract("There is a game engine Unreal Engine")
    self.assertNotEqual(len(match),0,"no match found") # "game_engines", "Unreal Engine", {"name":"Unreal Engine","ident":"Unreal Engine"})
  
  def testUnity3D(self):
    match = extract("There is a game engine Unity3D called Unity3D")
    self.assertNotEqual(len(match),0,"no match found") # "game_engines", "Unity3D", {"name":"Unity3D","ident":"Unity3D"})

  def testBasicExtract(self):
    match = basicExtract('tasty cat food')
    self.assertNotEqual(len(match),0,"no match found")

  def testMyExtract(self):
    match = myExtract("There is a game engine")
    self.assertNotEqual(len(match),0,"no match found")

  def testConstraintSequenceExtract(self):
    match = constraintSequenceExtract("There is a game engine")
    self.assertNotEqual(len(match),0,"no match found")

    #Crysis - said no to use in an online class
    #Unity3d - http://www.studica.com/unity
    #Source http://source.valvesoftware.com/sourcesdk/sourceu.php
    #Unreal engine
    #Game Maker
    #Game Salad
    #Scirra
    #Torque 3d