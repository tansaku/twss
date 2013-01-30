import sys
import getopt
import pdb

CSCI3651_PREREQ = "CSCI 2911, CSCI 2912"
CSCI3651_TEXT = "Engineering Long Lasting Software"

COURSE_CREATOR = lambda ident: Course(ident)

class Course:
  def __init__(self, ident):
    self.ident = ident

# would be nice if constants above could be reflected in lettuce features

# this hashtable approach is weird
# issues will include
# 1. punctuation
# 2. missed spaces
# 3. close synonyms ...
# 4. ultimately large nested hashtable difficult to maintain?
# 5. variations on sentence structure a pain to handle? will we get any generalization?
# e.g. "what is the textbook for the course?", "does this course have a textbook?"
# these examples make it look like a bag of words appraach is sensible


def ask(question):
  hashtable = {"what": 
                {"are":
                  {"the":
                    {"course":
                      {"requirements?":CSCI3651_PREREQ}
                    }
                  },
                 "is":
                  {"the":
                    {"course":
                      {"textbook?":CSCI3651_TEXT}
                    }
                  }
                },
               "there":
                {"is":
                  {"a":
                    {"course":
                      {"called":
                        {"ANYTHING":COURSE_CREATOR}
                      }
                    }
                  }
                }
              }
  for word in question.lower().split():
    try:
      hashtable = hashtable[word]
    except KeyError as e:
      # issue now is that all errors will trigger KeyError here
      # should every key be a function call? don't think that will work - maybe in js?
      # maybe should handle KeyError based on context ...?
      #pdb.set_trace()
      hashtable = hashtable["ANYTHING"]
      # and then we pickle this object?  store it in a db?
      return hashtable(e[0].upper()).ident
  return hashtable

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
             raise Usage(msg)
        print ask(args[0])
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())