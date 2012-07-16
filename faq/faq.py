from test_faq import *
from db import *
import re
from urllib import FancyURLopener
import pdb
import random
import inflect
import nltk
from nltk.corpus import stopwords
p = inflect.engine()
import time

CSCI3651_PREREQ = "CSCI 2911, CSCI 2912"
CSCI3651_TEXT = "Artificial Intelligence for Games"
CSCI3651_CRN = "3335"
CSCI3211_TEXT = "Engineering Long Lasting Software"
CSCI3211_CRN = "2802"
START = "Tuesday, September 4th, 2012"
END= "Sunday, December 16th, 2012"

courseCache = {"CSCI3651":
                {"textbook":CSCI3651_TEXT,
                 "CRN":CSCI3651_CRN,
                 "start date":START,
                 "end date":END},
                "CSCI3211": 
                {"textbook":CSCI3211_TEXT,
                  "CRN":CSCI3211_CRN,
                  "start date":START,
                  "end date":END}
              }

aspectList = { "textbook":set(["textbook","book","text","reading"]), # could be doing wordnet lookup here ...
               "CRN":set(["crn","reference","CRN"]),
               "start date":set(["begin","start"]),
               "end date":set(["end","finish","over","stop"]) }
               
courseList = {"CSCI3651":["3651","game programming","game"],
              "CSCI3211":["3211","systems analysis","software engineering"]
              }  
courses = courseList.keys() 

DATABASE_NAME = "faq.db" 

def query(userSaid,conversationTitle=None,talking=None,database_name = DATABASE_NAME):
  '''natural language (hopefully) interface to store information and query it too'''
  userSaid = userSaid.strip()
  raw = userSaid.lower()
  if raw.startswith('@bot'):
    userSaid = userSaid[len('@bot'):]
  if raw.startswith('@chatbot'):
    userSaid = userSaid[len('@chatbot'):]
  if raw.startswith('@hpuchatbot'):
    userSaid = userSaid[len('@hpuchatbot'):]

  userSaid = userSaid.strip()
  if not userSaid.lower().startswith("what"):
    statementCheck = process(userSaid,database_name)
    if statementCheck:
      return statementCheck
  userSplit = re.split(r'\W+',userSaid)
  stoppedUserSplit = [w for w in userSplit if not w in stopwords.words('english')]
  #print userSplit
  #courseMatches = list(set(courses).intersection(set(userSplit))) # we could avoid splitting and be doing lookup on the sentence ...
  
  lowerUserSaid = userSaid.lower()
  courseMatch = None
  aspect = None
  tableMatch = None
  bigrams = nltk.bigrams(stoppedUserSplit)
  searchList = stoppedUserSplit + [bigram[0]+" "+bigram[1] for bigram in bigrams]
  searchList = list(set(searchList))
  searchList = [item for item in searchList if item != '']
  
  for ident in searchList:
    (table,result) = findTableContainingEntityWithIdent(ident, database_name, True)
    if table:
      column_names = grabColumnNames(table, database_name)
      humanized_column_names = [col_name.replace('_',' ') for col_name in column_names]
      for index,name in enumerate(humanized_column_names):
        #raise Exception(lowerUserSaid + "::" + str(humanized_column_names))
        if lowerUserSaid.find(name)>0: # would love to get syn sets for names from wordnet 
          if result[index] == None:
            break
          return humanizedQuestion(ident,name,result[index])
          break
      return  allIKnow(table, ident, result, humanized_column_names)#"I'm not sure about that aspect of " + ident # here we could return what we know wbout that thing
  final = "not sure what you mean ..."
  
  if database_name != "test.db":
    myopener = MyOpener()
    page = myopener.open('http://google.com/search?btnI=1&q='+userSaid)
    page.read()
    time.sleep(1)
    response = page.geturl()
    final = "Does this help? "+ response
  
  #pdb.set_trace()
  return final

        
  # working with the conversations title might allow us to answer things like "what's the textbook for this course", 
  # but we should check for presence of column name, and things like "this course" 
   
  #lowerConversationTitle = conversationTitle.lower()
  #if not courseMatch
    #for synonym in courseList[course]:
      #if lowerConversationTitle.find(synonym)>0:
        #courseMatch = course
        #break

def allIKnow(table, ident, result, humanized_column_names):   
  possessive = "his" if table == "people" else "its" # would be nice to switch on gender here, or is that something we could learn?
  allIKnow = "All I know about %s is that %s " % (ident, possessive)
  return allIKnow+(", and %s "%possessive).join([name + " is " + result[index] for index,name in enumerate(humanized_column_names)if name != "ident" and result[index] != None] )
              
def getAspect(userSplitSet):
  for aspect, aspectSet in aspectList.items():
    if userSplitSet.intersection(aspectSet):
       return aspect              

def question(course, aspect):
  if not courseCache.get(course):
    return "duh ..."
    #countryCache[course] = json.loads(urlopen(url+country+api_id).read())['geonames'][0]
  return courseCache[course][aspect]

def humanize(camelCase):
    return re.sub("([a-z])([A-Z])","\g<1> \g<2>",camelCase).lower()

def humanizedQuestion(course, aspect, answer="Unknown"):
  if not answer: 
    question(course,aspect)
  return "The " + aspect + " for " + course + " is '" + answer + "'"

def greetings():
  return random.choice(["sup, dog!","hello","hi there","dude","zaapp?"])
  
class MyOpener(FancyURLopener):
  version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

def process(statement,database_name = DATABASE_NAME):
  ''' Allows us to create entities via statements like "There is a course CSCI4702 called Mobile Programming" 
      and modify entities with statements like "CSCI4702 has a start date of Jan 31st 2013"'''
  match = re.search(r'There is a (\w+) ([\s\w]+) called ([\s\w]+)\.?',statement)
  if match:
    table = p.plural(match.group(1))
    try:
      createTable(table, ["ident"], database_name)
    except sqlite3.OperationalError as e:
      if str(e) == "table "+table+" already exists":
        pass
      else:
        raise(e)
    addEntity(table, {"ident":match.group(2),"name":match.group(3)},database_name)
    return "OK"
    
  return processNewAspect(statement,database_name)
  
def processNewAspect(statement,database_name = DATABASE_NAME):
  #raise Exception(statement)
  match = re.search(r"([\s\w]+?)(?:(?: has a)|(?:\'s)) ([\s\w]+) (?:(?:of)|(?:called)|(?:is(?: called)?)) ([\s\w:/\.]+)\.?",statement)
  #raise Exception(match.group(0))
  if match:
    # need to search all tables
    ident = match.group(1)
    (table,result) = findTableContainingEntityWithIdent(ident, database_name)
    if table == None: 
      return "Sorry, I don't know about " + ident
    new_column = match.group(2).lower()
    try:
      modifyTable(table, new_column, database_name)
    except sqlite3.OperationalError as e:
      if str(e).startswith("duplicate column name: "):
        pass
      else:
        raise e
    updateEntity(table, {"ident":ident,new_column:match.group(3)},database_name)
    return "OK"
  return None
    
if __name__ == "__main__":
  n = ""
  print greetings()
  while True:
    n = raw_input("> ")
    if n == "quit":
      break;
    print query(n)
  
  
  
  
  