def reverseCap() -> None:
	word = input("Input a word: ")
	res = ""
	for i in range(len(word)):
		res += word[len(word) - i - 1].upper()
	print(res)


if __name__ == "__main__":
	reverseCap()	
