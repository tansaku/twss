from faq import *
import unittest
from test_db import *

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
       
  # these are all starting to look a lot like behavioural tests rather than unit tests
  # not sure if that's something we should be making changes for ...
  # would be nice to be able to specify expected behaviour precisely in terms
  # of a conversation ...
  def testAnotherCreation(self):
    ''' test we can create and modify arbitrary entities '''
    query("There is a course CSCI3651 called Games Programming", database_name = TEST_DATABASE)
    self.checkEntity("courses", "CSCI3651", {"name":"Games Programming","ident":"CSCI3651"},TEST_DATABASE)

    query("CSCI3651 has a CRN of 3335", database_name = TEST_DATABASE)
    query("CSCI3651 has a CRN of 3335", database_name = TEST_DATABASE)

    self.checkEntity("courses", "CSCI3651", {"crn":"3335","name":"Games Programming","ident":"CSCI3651"},TEST_DATABASE)

    #self.assertEquals(query("What's the start date of CSCI3651?",database_name = TEST_DATABASE),u"I'm not sure about that aspect of CSCI3651")
    #self.assertEquals(query("What's the CRN of CSCI3651?",database_name = TEST_DATABASE),u"The crn for CSCI3651 is '3335'")

    # would love 'of' to be replaced with 'called' in the line below
    
    self.assertEquals(query("CSCI3651 has a textbook of Artificial Intelligence for Games",database_name = TEST_DATABASE),u"OK") 
    self.assertEquals(grabColumnNames("courses", TEST_DATABASE),[u"name",u"ident",u"crn",u"textbook"])
    # this query above used to take an awful long time since we had regex with (\s|\w)+ which apparently sux...
    self.assertEquals(query("what is the textbook of CSCI3651",database_name = TEST_DATABASE),u"The textbook for CSCI3651 is 'Artificial Intelligence for Games'")
    # handling all the different possible ways of saying these things ... hmmm ....
    
    # would love to have history in the command prompt as well as other arrow key features, but can get that from skype?
    
    # should be testing that situation when we ask about an ident that doesn't exist yet ...
    self.assertEquals(query("CSCI9999 has a CRN of 9999",database_name = TEST_DATABASE),u"Sorry, I don't know about CSCI9999")

    query("CSCI3651 has a URL of https://sites.google.com/site/gameprogrammingfall2012/", database_name = TEST_DATABASE)
    self.checkEntity("courses", "CSCI3651", {"url":"https://sites.google.com/site/gameprogrammingfall2012/"},TEST_DATABASE)

 

  def testCreation(self):
    ''' test we can create and modify arbitrary entities '''
    query("There is a course CSCI4702 called Mobile Programming", database_name = TEST_DATABASE)
    entity = grabEntity("courses", "CSCI4702", TEST_DATABASE)
    self.assertEquals(entity['name'],"Mobile Programming")
    self.assertEquals(entity['ident'],"CSCI4702")
    query("CSCI4702 has a start date of Jan 31st 2013", database_name = TEST_DATABASE)
    query("CSCI4702 has a start date of Jan 31st 2013", database_name = TEST_DATABASE)
    entity = grabEntity("courses", "CSCI4702", TEST_DATABASE)
    self.assertEquals(entity['start_date'],"Jan 31st 2013")
    self.assertEquals(entity['name'],"Mobile Programming")
    self.assertEquals(entity['ident'],"CSCI4702")
    self.assertEquals(query("What's the start date of CSCI4702?",database_name = TEST_DATABASE),u"The start date for CSCI4702 is 'Jan 31st 2013'")
    self.assertEquals(query("What's the CRN of CSCI4702?",database_name = TEST_DATABASE),u"I'm not sure about that aspect of CSCI4702")

  def testOtherCreation(self):
    ''' test we can create and modify arbitrary entities '''
    query("There is a professor Sam Joseph called Sam", database_name = TEST_DATABASE)
    entity = grabEntity("professors", "Sam Joseph", TEST_DATABASE)
    self.assertEquals(entity['name'],"Sam")
    self.assertEquals(entity['ident'],"Sam Joseph")
    query("Sam Joseph has a birth date of May 13th 1972", database_name = TEST_DATABASE)
    query("Sam Joseph has a birth date of May 13th 1972", database_name = TEST_DATABASE)
    entity = grabEntity("professors", "Sam Joseph", TEST_DATABASE)
    self.assertEquals(entity['birth_date'],"May 13th 1972")
    self.assertEquals(entity['name'],"Sam")
    self.assertEquals(entity['ident'],"Sam Joseph")
    self.assertEquals(query("What's Sam Joseph's birth date?",database_name = TEST_DATABASE),u"The birth date for Sam Joseph is 'May 13th 1972'")
