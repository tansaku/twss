"""
This is a work in progress designed to explore how to implement
Object Actions.  I have intentionally re-implememtned a simplified
world model to do this so that it is more accessible to anyone
wanting to help.

The aim is to give Objects a series of allowed actions which they
can perform and which can be performed upon them.  In the later case
the object needs to have one or more reactions which take place.  I
hope that these can become quite sophisticated in future, hence why
I am passing things like the "origin" of the action.

My model is for Objects to pass an Action to other objects.  Any 
parameters should be in the params attribute of the Action instance.
It is then up to the initiating object to confirm that it is able to
create that specific sort of Action and for the receiving Object to
confirm that it can has a Reaction to that type of Action. 

Action objects are currently pretty simple.  They make significant use
of inheritence to decide how the receiving object reacts.  For example,
you might have a "Damage" class which inherits from Action.  Lots of 
objects would understand how to respond to that.  Some People objects
could then have "Poke" Actions which inherit from Damage.

The key bit I am looking for help on is persistance.  I am experimenting
offline on some sort of database.   My aim for this would be to let the
world model scale gracefully without putting limitations on the different
types of Actions, Objects etc which can be created.  I am thinking along
the lines of something like MongoDB or neo4js in tandem with Pickle, but
would appreciate other ideas. 
"""

"""Have a look at "test_actions.py" for trivial examples of how to use this"""

import new

class Object():
  def __init__(self,name):
    self.name=name #Should be something you are willing to publish to the user.  Default to lower case unless it is a proper noun.
    self.reactions={} #Dictionary with Action class types as keys and a list of Reaction instances as values  
    self.actions=set() #A set showing the Action class types which this Object can initiate
    self.params={} #Some object specific parameters which we want to persist
  def __str__(self):
    return self.name #Just for debug, you can change this to be more useful if necessary
  def add_action(self, action):
    """Pass this an Action object (or something which inherits from Action).
    This will add the class type to the list of actions this Object can
    initiate."""
    self.actions.add(action.__class__)
    #TODO: Should really check this is a legal Action style object
  def set_reaction(self, action, reactions=[]):
    """Pass this an Action object (or something which inherits from Action)
    and a list of Reaction objects.  This will add the class type to the list
    of actions which can be performed on this Object"""
    self.reactions.update([(action.__class__, reactions)])
    #TODO: Add a similar function to add a reaction to the reactions list
  def do_action(self, action):
    """Call this method on an initiating Object with an Action.  Make sure that
    the Action has had its target and origin atributes set correctly."""
    self.check_can_do_action(action) #Does basic validation that this Action is allowed
    #TODO: At the moment there is no fallback to Parent Reactions.  For example it would be nice if the recipient object used the "Damage" reaction if it doesn't have a more specific "Poke" reaction.
    for reaction in action.target.reactions[action.__class__]:
      reaction.do(action)
  def check_can_do_action(self, action):
    """Checks that an Action is legal.  At the moment, the only error checking
    is done by the initiating object"""
    #TODO: Add similar function (or split this one) so that the receiving object also checks the Action is "legal".
    if action.target is None:
      raise Exception("There is no target for Action '%s'" % action)
    if action.__class__ not in self.actions:
      raise Exception("Object '%s'cannot perform action '%s' on '%s'" % (self, action, action.target))
    if not(action.origin is self):
      raise Exception("Object '%s' cannot run another object's action '%s'" % (self, action))
    if action.__class__ not in action.target.reactions.keys():
      raise Exception("Action '%s' cannot be performed on Object 's'" % (action, action.target))

class Action():
  """The base Action class.  All Actions should inherit from this; I cannot
  imagine a case where I would want to use a vanila Action instance"""
  def __init__(self, name="unknown"):
    #TODO: I am not sure if there is a way of making sure that child instances have _at least_ the functionality of their parents, but that feels somewhat important.
    self.name = name
    self.params={}
    self.target=None
    self.origin=None
  def __str__(self):
    return self.name

class Reaction(Action):
  def __init__(self, name="unknown"):
    Action.__init__(self, name)
  def do(self, action=None):
    """This is the function which is called to get a Reaction.  This is clearly
    a placehoder which needs to be filled when creating a real Reaction.  All 
    replacement functions should take only an Action object as an arguement and
    pass parameters within the Action params attribute."""
    pass
  def change_do(self, new_do):
    """This is a function to simplify the replacement of the placeholder do 
    function with something more useful."""
    self.do = new.instancemethod(new_do,self,None)


"""Common "do" functions for Reaction objects should be included below"""    
def say(self, action):
  print "%s says: %s" % (self.params['from'], self.params['what'])
