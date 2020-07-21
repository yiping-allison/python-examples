class Animal:

	# constructor
	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	# returns a string representing the animal's name
	def getName(self) -> str:
		return self.__name


	# returns an integer representing the animal's age in years
	def getAge(self) -> int:
		return self.__age


	# Dunder method - Python's version of operator overloading
	# __str__ specifically overrides print() behavior on Animal objects
	# returns a string to print the object
	def __str__(self) -> str:
		return self.__name + " is currently " + str(self.__age) + " years old!"

