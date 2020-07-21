from animal import Animal

class Monkey(Animal):

	def __init__(self, name, age):
		# in python -- child's constructor method will override parent's constructor
		# if want to keep parent's inheritance:
		# def __init__(self, param1, param2):
		# 	Animal.__init__(self, param1, param2)

		# You can also use a super() method:
		# def __init__(self, param1, param2):
		# 	super().__init__(param1, param2)
		
		super().__init__(name, age)
		# prefixing a variable with double underscores signifies a variable is meant to be
		# private
		self.__noise = "krak-oo krak-oo"


	def __str__(self) -> str:
		return "The monkey is called " + self.getName() + " and is " + str(self.getAge()) + " years old."


	def getNoise(self) -> str:
		return self.__noise

