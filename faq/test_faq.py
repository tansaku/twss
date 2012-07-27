from faq import *
import unittest
import os
from test_db import TEST_DATABASE

class TestFaq(unittest.TestCase):
  def setUp(self):
    try:
       with open(TEST_DATABASE) as f: 
         os.remove(TEST_DATABASE)
         pass
    except IOError as e:
       None
       
  def checkEntity(self, table, ident, attributeValues, database):
    entity = grabEntity(table, ident, database)
    for key, value in attributeValues.items():
      self.assertEquals(entity[key],value)
      
  def sayAndCheckEntity(self,sentence, response, table, ident, attributeValues, database = TEST_DATABASE):
    self.assertEquals(query(sentence, database_name = database), response) 
    self.checkEntity(table, ident, attributeValues, database)
    
  def sayAndCheck(self,sentence, response, database = TEST_DATABASE):
    self.assertEquals(query(sentence, database_name = database), response) 
    
  def testCreateGameEngine(self):
    self.sayAndCheckEntity("There is a game engine Unreal Engine", "OK", "game_engines", "Unreal Engine", {"name":"Unreal Engine","ident":"Unreal Engine"})
    self.sayAndCheckEntity("There is a game engine Unity3D called Unity3D", "OK", "game_engines", "Unity3D", {"name":"Unity3D","ident":"Unity3D"})
    self.sayAndCheckEntity("Unity3D has a URL of http://www.studica.com/unity", "OK", "game_engines", "Unity3D", {"url":"http://www.studica.com/unity"})
    self.sayAndCheckEntity("Unity3D has a type of integrated","OK","game_engines", "Unity3D", {"type":"integrated"})
    self.sayAndCheckEntity("Unity3D has a type of 3D","OK","game_engines", "Unity3D", {"type":"3D"})
    self.sayAndCheck("What type of game engine is Unity3D?","The type for Unity3D is '3D'")

    #Crysis - said no to use in an online class
    #Unity3d - http://www.studica.com/unity
    #Source http://source.valvesoftware.com/sourcesdk/sourceu.php
    #Unreal engine
    #Game Maker
    #Game Salad
    #Scirra
    #Torque 3d  
    
  def testActions(self):
    ''' test we can handle actions '''
    self.sayAndCheckEntity("There is a person evil wizard called Sam", "OK", "people", "evil wizard", {"name":"Sam","ident":"evil wizard"})
    self.sayAndCheckEntity("There is an animal cat called Puss", "OK", "animals", "cat", {"name":"Puss","ident":"cat"})
    self.sayAndCheckEntity("There is an action soak called get wet", "OK", "actions", "soak", {"name":"get wet","ident":"soak"})
    self.sayAndCheckEntity("soak has a target of cat", "OK", "actions", "soak", {"name":"get wet","ident":"soak","target":"cat"})
    self.sayAndCheckEntity("soak has an origin of evil wizard", "OK", "actions", "soak", {"name":"get wet","ident":"soak","target":"cat","origin":"evil wizard"})
    self.sayAndCheckEntity("There is a reaction meow called Meow", "OK", "reactions", "meow", {"name":"Meow","ident":"meow"})
    self.sayAndCheckEntity("meow has an origin of cat", "OK", "reactions", "meow", {"name":"Meow","ident":"meow", "origin":"cat"})
    self.sayAndCheckEntity("meow has an action of soak", "OK", "reactions", "meow", {"name":"Meow","ident":"meow", "origin":"cat", "action":"soak"})

    self.sayAndCheck("what happens if the evil wizard soaks cat?", "Puss says Meow")

  def testStrippingTag(self):
    ''' test we can strip tag '''
    self.sayAndCheckEntity("@bot There is a course CSCI3651 called Games Programming", "OK", "courses", "CSCI3651", {"name":"Games Programming","ident":"CSCI3651"})
    self.sayAndCheckEntity("@chatbot There is a course CSCI3651 called Games Programming", "OK", "courses", "CSCI3651", {"name":"Games Programming","ident":"CSCI3651"})
    self.sayAndCheckEntity("@hpuchatbot There is a course CSCI3651 called Games Programming", "OK", "courses", "CSCI3651", {"name":"Games Programming","ident":"CSCI3651"})

  # these are all starting to look a lot like behavioural tests rather than unit tests
  # not sure if that's something we should be making changes for ...
  # would be nice to be able to specify expected behaviour precisely in terms
  # of a conversation ...
  def testAnotherCreation(self):
    ''' test we can create and modify arbitrary entities '''
    self.sayAndCheckEntity("There is a course CSCI3651 called Games Programming", "OK", "courses", "CSCI3651", {"name":"Games Programming","ident":"CSCI3651"})

    self.sayAndCheckEntity("CSCI3651 has a CRN of 3335", "OK", "courses", "CSCI3651", {"crn":"3335","name":"Games Programming","ident":"CSCI3651"})
    self.sayAndCheckEntity("CSCI3651 has a CRN of 3335", "OK", "courses", "CSCI3651", {"crn":"3335","name":"Games Programming","ident":"CSCI3651"})

    self.sayAndCheck("What's the start date of CSCI3651?", "All I know about CSCI3651 is that its name is Games Programming, and its crn is 3335")
    self.sayAndCheck("What's the CRN of CSCI3651?", "The crn for CSCI3651 is '3335'")

    self.sayAndCheckEntity("CSCI3651 has a textbook of Artificial Intelligence for Games", "OK", "courses", "CSCI3651", {"crn":"3335","name":"Games Programming","ident":"CSCI3651", "textbook":"Artificial Intelligence for Games"})
    self.sayAndCheckEntity("CSCI3651's textbook is called Artificial Intelligence for Games", "OK", "courses", "CSCI3651", {"crn":"3335","name":"Games Programming","ident":"CSCI3651", "textbook":"Artificial Intelligence for Games"})
    self.sayAndCheck("what is the textbook of CSCI3651", "The textbook for CSCI3651 is 'Artificial Intelligence for Games'")
    # this query above used to take an awful long time since we had regex with (\s|\w)+ which apparently sux...

    # handling all the different possible ways of saying these things ... hmmm ....

    # would love to have history in the command prompt as well as other arrow key features, but can get that from skype?

    # testing that situation when we ask about an ident that doesn't exist yet ...
    self.sayAndCheck("CSCI9999 has a CRN of 9999", "Sorry, I don't know about CSCI9999")

    self.sayAndCheckEntity("CSCI3651 has a URL of https://sites.google.com/site/gameprogrammingfall2012/", "OK", "courses", "CSCI3651", {"url":"https://sites.google.com/site/gameprogrammingfall2012/"})
    self.sayAndCheck("what is the URL of CSCI3651", "The url for CSCI3651 is 'https://sites.google.com/site/gameprogrammingfall2012/'")
    # would really like to use wordnet to allow user to ask about "webpage", "homepage", "page" etc. for this attribute

    # need something to test null entries
    self.sayAndCheck("There is a course CSCI3771 called Python", "OK")
    self.sayAndCheck("what is the enrollment for CSCI3771", "All I know about CSCI3771 is that its name is Python")
    self.sayAndCheck("what is the URL of CSCI3771", "All I know about CSCI3771 is that its name is Python")

  # was also thinking to have something that listed all the London Stanford guys courses - something they could enter if I can
  # get this all live ...


  def testCreateGame(self):
    self.sayAndCheckEntity("There is a game The Graveyard called The Graveyard", "OK", "games", "The Graveyard", {"name":"The Graveyard","ident":"The Graveyard"})
    self.sayAndCheckEntity("The Graveyard has a URL of http://store.steampowered.com/app/27020", "OK", "games", "The Graveyard", {"url":"http://store.steampowered.com/app/27020"})
    self.sayAndCheckEntity("The Graveyard has a type of weird","OK","games", "The Graveyard", {"type":"weird"})
    self.sayAndCheckEntity("The Graveyard has a type of existential","OK","games", "The Graveyard", {"type":"existential"})
    self.sayAndCheck("What type of game is The Graveyard?","The type for The Graveyard is 'existential'")
    # TODO self.sayAndCheck("do you know about an existential game?","All I know about The Graveyard is that its name is The Graveyard, and its url is http://store.steampowered.com/app/27020, and its type is existential")
    # to fix this, after searching idents we'd need to search on types ...
    # TODO self.sayAndCheck("do you know any games?","I know about The Graveyard")
    # this would require further work still?

  
  def testCreateCourseraCourses(self):
    self.sayAndCheckEntity("There is a course Probabilistic Graphical Models called PGM", "OK", "courses", "Probabilistic Graphical Models", {"name":"PGM","ident":"Probabilistic Graphical Models"})
    self.sayAndCheckEntity("There is a course Machine Learning called ML", "OK", "courses", "Machine Learning", {"name":"ML","ident":"Machine Learning"})
    self.sayAndCheckEntity("Probabilistic Graphical Models's instructor is Daphne Koller", "OK", "courses", "Probabilistic Graphical Models", {"instructor":"Daphne Koller"})
    self.sayAndCheckEntity("Machine Learning's instructor is Andrew Ng", "OK", "courses", "Machine Learning", {"instructor":"Andrew Ng"})
    self.sayAndCheck("Who is the instructor for Machine Learning?","The instructor for Machine Learning is 'Andrew Ng'")
    self.sayAndCheck("Which instructor teaches Probabilistic Graphical Models?","The instructor for Probabilistic Graphical Models is 'Daphne Koller'")
    # TODO self.sayAndCheck("do you know about an existential game?","All I know about The Graveyard is that its name is The Graveyard, and its url is http://store.steampowered.com/app/27020, and its type is existential")
    # to fix this, after searching idents we'd need to search on types ...
    # TODO self.sayAndCheck("do you know any games?","I know about The Graveyard")
    # this would require further work still?

  def testCreatePerson(self):
    self.sayAndCheckEntity("There is a person Henry Garner called Henry", "OK", "people", "Henry Garner", {"name":"Henry","ident":"Henry Garner"})
    self.sayAndCheckEntity("Henry Garner has a favourite colour of red","OK","people", "Henry Garner", {"favourite_colour":"red"})
    self.sayAndCheckEntity("Henry Garner has a favourite colour of teal","OK","people", "Henry Garner", {"favourite_colour":"teal"})
    self.sayAndCheck("do you know about Henry Garner?","All I know about Henry Garner is that his name is Henry, and his favourite colour is teal")

  def testCreateCTO(self):
    self.sayAndCheckEntity("There is a CTO Henry Garner called Henry", "OK", "CTOs", "Henry Garner", {"name":"Henry","ident":"Henry Garner"})
    self.sayAndCheckEntity("Henry Garner has a favourite colour of red","OK","CTOs", "Henry Garner", {"favourite_colour":"red"})
    self.sayAndCheckEntity("Henry Garner has a favourite colour of teal","OK","CTOs", "Henry Garner", {"favourite_colour":"teal"})
    self.sayAndCheck("do you know about Henry Garner?","All I know about Henry Garner is that its name is Henry, and its favourite colour is teal")

  def testCreation(self):
    ''' test we can create and modify arbitrary entities '''
    self.sayAndCheckEntity("There is a course CSCI4702 called Mobile Programming", "OK","courses", "CSCI4702", {"name":"Mobile Programming","ident":"CSCI4702"})
    self.sayAndCheckEntity("CSCI4702 has a start date of Jan 31st 2013", "OK","courses", "CSCI4702", {"name":"Mobile Programming","ident":"CSCI4702","start_date":"Jan 31st 2013"})
    self.sayAndCheck("What's the start date of CSCI4702?","The start date for CSCI4702 is 'Jan 31st 2013'")
    self.sayAndCheck("What's the CRN of CSCI4702?","All I know about CSCI4702 is that its name is Mobile Programming, and its start date is Jan 31st 2013")

  def testOtherCreation(self):
    ''' test we can create and modify arbitrary entities '''
    self.sayAndCheckEntity("There is a professor Sam Joseph called Sam","OK", "professors", "Sam Joseph", {"name":"Sam","ident":"Sam Joseph"})
    self.sayAndCheckEntity("Sam Joseph has a birth date of May 13th 1972","OK", "professors", "Sam Joseph", {"name":"Sam","ident":"Sam Joseph",'birth_date':"May 13th 1972"})
    self.sayAndCheck("What's Sam Joseph's birth date?","The birth date for Sam Joseph is 'May 13th 1972'")
