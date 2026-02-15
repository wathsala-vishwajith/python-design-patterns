# Python code​​​​​​‌‌‌‌​​‌​‌​​​‌​​​​​​​​‌​​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

class Subject(object): #Represents what is being 'observed'

	def __init__(self):
		self._observers = [] # This where references to all the observers are being kept
							 # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

	def attach(self, observer):
		if observer not in self._observers: #If the observer is not already in the observers list
			self._observers.append(observer) # append the observer to the list

	def detach(self, observer): #Simply remove the observer
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

	def notify(self, modifier=None):
		for observer in self._observers: # For all the observers in the list
			if modifier != observer: # Don't notify the observer who is actually updating the temperature 
				observer.update(self) # Alert the observers!

class Core(Subject): #Inherits from the Subject class

	def __init__(self, name=""):
		Subject.__init__(self)
		self._name = name #Set the name of the core
		self._temp = 0 #Initialize the temperature of the core

	@property #Getter that gets the core temperature
	def temp(self):
		return self._temp

	@temp.setter #Setter that sets the core temperature
	def temp(self, temp):
		self._temp = temp
		self.notify(self) #Notify the observers whenever somebody changes the core temperature

class TempViewer():

	def __init__(self, name=""):
		self._name = name #Set the name of the observer
		self._notifications = ""	

	def update(self, subject): #Alert method that is invoked when the notify() method in a concrete subject is invoked
		self._notifications = self._notifications + self._name + ": " + subject._name + ": " + str(subject._temp) + "|" 
		#print("Temperature Viewer {}: {} has Temperature {}".format(self._name, subject._name, subject._temp))

	def show_notifications(self):
		return self._notifications

#Let's create our subjects
c = Core("Core")

#Your code to create an observer goes here
v = TempViewer("Viewer")


#Your code to attach the observers to the first core goes here
c.attach(v)


#Your code to change the temperature to 100 goes here.
c.temp = 100


#Your code to detach the observer goes here
c.detach(v)

#Your code to change the temperature to 90 goes here.
c.temp = 90


def display_notifications():
    # Your code goes here
    return v.show_notifications()
