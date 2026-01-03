
class Pet:

	"""A simple pet class"""

	def __init__(self, name):
		self._name = name
		self._sound = "Silence"

	def __eq__(self, other):
		if isinstance(other, Pet):
			return (self._sound) == (other._sound)
		return NotImplemented

	def __str__(self):
		return '{} | {}'.format(self._name, self._sound)

	def speak(self):
		return self._sound

class Dog(Pet):

	"""A simple dog class"""

	def __init__(self, name):
		Pet.__init__(self, name)
		self._sound = "Woof!"

class Cat (Pet):

	"""A simple cat class"""

	def __init__(self, name):
		Pet.__init__(self, name)
		self._sound = "Meow!"

class Pig (Pet):

	"""A simple Pig class"""

	def __init__(self, name):
		Pet.__init__(self, name)
		self._sound = "Oink!"



def get_pet(pet="dog"):

	"""The factory method"""

	pets = dict(dog=Dog("Hope"), cat=Cat("Peace"),pig=Pig("Sam"))

	return pets[pet]

def get_pig():
    # Your code goes here
    return get_pet("pig")
