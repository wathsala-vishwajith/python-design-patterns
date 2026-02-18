# Python code​​​​​​‌‌‌‌​​‌​‌‌​​​‌‌‌​​​‌‌‌‌​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = True

import types #Import the types module

class Strategy:
    """The Strategy Pattern class"""
    
    def __init__(self, function=None):
        self.name = "Passcode"
        
        #If a reference to a function is provided, replace the execute() method with the given function
        if function:
        	self.execute = types.MethodType(function, self)
                
    def execute(self): #This gets replaced by another version if another strategy is provided.
        """The defaut method that prints the name of the strategy being used"""
        return self.name
        #print("{} is used!".format(self.name))

#Replacement method 1
def strategy_finger(self):
    return self.name

#Replacement method 2    
def strategy_face(self):
    return self.name
    
#Let's create our default strategy
s0 = Strategy()


#Your code to create the first varition of our default strategy (i.e., using fingerprints) goes here
s1 = Strategy(strategy_finger)
s1.name ="Strategy Finger"

#Your code to create the second varition of our default strategy (i.e., using faces) goes here
s2 = Strategy(strategy_face)
s2.name ="Strategy Face"

dic = {"finger": s1, "face": s2, "passcode": s0 }


def apply_authentication(preference):
    # Your code goes here
    return dic[preference].execute()

