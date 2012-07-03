from test_faq import *
from db import *
import re
from urllib import FancyURLopener
import pdb
import random
import inflect
p = inflect.engine()

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

def query(userSaid,conversationTitle=None,talking=None):
  '''natural language (hopefully) interface to store information and query it too'''
  statementCheck = process(userSaid)
  if statementCheck:
    return statementCheck
  userSplit = re.split(r'\W+',userSaid)
  #print userSplit
  #courseMatches = list(set(courses).intersection(set(userSplit))) # we could avoid splitting and be doing lookup on the sentence ...

  courseMatch = None
  lowerUserSaid = userSaid.lower()
  for course in courses:
    for synonym in courseList[course]:
      if lowerUserSaid.find(synonym)>0:
        courseMatch = course
        break
        
  # this could allow us to answer things like "what's the textbook for this course", but we should check for 
  # presence of aspect, and things like "this course" - really should get set up with sniffer or something
  # to start managing all these things ...
   
  #lowerConversationTitle = conversationTitle.lower()
  #if not courseMatch
    #for synonym in courseList[course]:
      #if lowerConversationTitle.find(synonym)>0:
        #courseMatch = course
        #break
  
  if courseMatch:
    course = courseMatch
    aspect = getAspect(set(userSplit))
    if aspect:
      return humanizedQuestion(course,aspect)
    else:
      return "I'm not sure about that aspect of " + course # could do hpu.edu site specific IFL search here
  else:  
    myopener = MyOpener()
    page = myopener.open('http://google.com/search?btnI=1&q='+userSaid)
    page.read()
    response = page.geturl()
    #pdb.set_trace()
    return "Does this help? "+ response 
              
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

def humanizedQuestion(course, aspect):
  return "The " + aspect + " for " + course + " is '" + question(course,aspect) + "'"

def greetings():
  return random.choice(["sup, dog!","hello","hi there","dude","zaapp?"])
  
class MyOpener(FancyURLopener):
  version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

def process(statement,database_name = "faq.db"):
  ''' Allows us to create entities via statements like "There is a course CSCI4702 called Mobile Programming" 
      and modify entities with statements like "CSCI4702 has a start date of Jan 31st 2013"'''
  match = re.search(r'There is a (\w+) ((?:\s|\w+)+) called ((?:\s|\w+)+)',statement)
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
  match = re.search(r'((?:\s|\w+)+?) has a ((?:\s|\w+)+) of ((?:\s|\w+)+)',statement)
  #raise Exception(statement)
  if match:
    # need to search all tables
    ident = match.group(1)
    table = findTableContainingEntityWithIdent(ident, database_name)
    new_column = match.group(2)
    try:
      modifyTable(table, new_column, database_name)
    except sqlite3.OperationalError as e:
      if str(e) == "table "+table+" already has a column called "+new_column:
        pass
      else:
        raise(e)
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
  
  
  
  
  