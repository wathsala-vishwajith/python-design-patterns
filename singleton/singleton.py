# The real reason that borg is different comes down to subclassing.
# If you subclass a borg, the subclass' objects have the same state as their parents classes objects, unless you explicitly override the shared state in that subclass. Each subclass of the singleton pattern has its own state and therefore will produce different objects.
# Also in the singleton pattern the objects are actually the same, not just the state (even though the state is the only thing that really matters).
# https://stackoverflow.com/questions/1318406/why-is-the-borg-pattern-better-than-the-singleton-pattern-in-python
class Borg:
    
    """The Borg design pattern"""
    """Borg pattern making the class attributes global"""
    _shared_data = {} # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data # Make it an attribute dictionary

    def __eq__(self, other):
        if isinstance(other, Borg):
            return (self._shared_data) == (other._shared_data)
        return NotImplemented

        

class Singleton(Borg): 
    
    """The singleton class"""
    """This class now shares all its attributes among its various instances"""
    #This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs) # Update the attribute dictionary by inserting a new key-value pair 

    def __str__(self):
        return str(self._shared_data) # Returns the attribute dictionary for printing

def prove_singleton():
    # Your code to create the first singleton object and add the first acronym/definition pair (UX="User Experience") goes here
    x= Singleton(UX="User Experience")
    # Your code to create the second singleton object and add the second acronym/definition pair (API="Application Programming Interface") goes here
    y = Singleton(API="Application Programming Interface")
    # Your code to return the singleton object of your choice
    return x
   

