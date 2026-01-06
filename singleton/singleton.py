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
   

