class Command:
	def execute(self):
		pass


class Copy(Command):
	def execute(self):
		print("Copying ...")

#Concrete Command
class Paste(Command):
	def execute(self):
		print("Pasting ...")

class Save(Command):
	def execute(self):
		print("Saving ...")

#Invoker
class Macro:
	def __init__(self):
		self.commands = []

	def add(self, command):
		self.commands.append(command)

	def run(self):
		for command in self.commands:
			command.execute()

def main():
	m = Macro()
	m.add(Copy())
	m.add(Paste())
	m.add(Save())
	m.run()

if __name__ == "__main__":
	main()
