from actions import *

#Create some more specific Objects
class Animal(Object):
  def __init__(self, name="unknown"):
    Object.__init__(self, name)

class Person(Animal):
  def __init__(self, name="unknown"):
    Animal.__init__(self, name)

#Create instances of objects    
cat=Animal("Puss")
evil_wizard=Person("Sam")

#Set up an action for man 
soak=Action("get wet")
soak.target=cat
soak.origin=evil_wizard

getWet=Reaction("wetify")
def make_wet(self, action):
  action.target.params.update([('wet',True)])
getWet.change_do(make_wet)

meow=Reaction("meow")
meow.params.update([('from',cat),('what','meow')])
meow.change_do(say)

evil_wizard.add_action(soak)
cat.set_reaction(soak,[meow,getWet])


evil_wizard.do_action(soak)
