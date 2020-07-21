from animal import Animal
from monkey import Monkey

def main():
	# testing base class - Animal
	animal = Animal("Luigi", 10)
	print(animal)

	# testing dereived class - Monkey
	mon = Monkey("Lily", 3)
	print(mon)
	print(mon.getNoise())


if __name__ == "__main__":
	main()

