# This program allows someone to play hangman
# Author: Yiping (Allison)
# December 2017

def get_secret_word() -> str:
    """
    Gets player 1's secret word
    :return: the secret word
    """
    # getting secret word from player 1
    word = input('Please enter a word to be guessed that does not contain'
                 ' ? or white space: ')
    while ' ' in word or '?' in word or len(word) == 0:
        word = input('Please enter a word to be guessed that does not contain'
                     ' ? or white space: ')
    return word

def secret_word(word_funct) -> tuple:
    """
    turns secret word into question marks
    :param word_funct: secret word from input definition
    :return: original word and word w/ ?
    """
    word = word_funct
    secret_length = len(word)  # get the secret word in form of ?
    secret = secret_length * '?'
    return word, secret

def get_guess(guess_list: list) -> str:
    """
    checks if guess is valid
    :param guess_list: is guess the same as previous guess
    :return: a valid guess
    """
    guess = input('Please enter your next guess: ')
    guess = guess.strip()
    while len(guess) != 1 or guess in guess_list:  # if guess does not = 1
        if len(guess) > 1:
            print('You can only guess a single character.')
            guess = input('Please enter your next guess: ')
            guess = guess.strip()
        elif len(guess) == 0 or guess == ' ':
            print('You must enter a guess.')
            guess = input('Please enter your next guess: ')
            guess = guess.strip()
        elif guess in guess_list:  # if guess is the same as previous guess
            print('You already guessed the character:', guess)
            guess = input('Please enter your next guess: ')
            guess = guess.strip()
    return guess

def display_word_mod(guess_list: list, word: str) -> None:
    """
    prints modifications to ? revealing secret word
    :param guess_list: player 2 guesses
    :param word: secret word
    :return: prints out secret word
    """
    for character in word:
        if character in guess_list:
            print(character, end='')
        else:
            print('?', end='')

def display_hangman(i: int) -> None:
    """
    based on the # of wrong guesses
    :param i: # of incorrect guesses
    :return: prints out the hangman
    """
    if i == 7:
        print(' |')
        print(' 0')
        print('/|\\')
        print('/ \\')
    elif i == 6:
        print(' |')
        print(' 0')
        print('/|\\')
        print('/')
    elif i == 5:
        print(' |')
        print(' 0')
        print('/|\\')
    elif i == 4:
        print(' |')
        print(' 0')
        print('/|')
    elif i == 3:
        print('|')
        print('0')
        print('|')
    elif i == 2:
        print('|')
        print('0')
    elif i == 1:
        print('|')

def is_game_over(word: str, guess_list: list) -> bool:
    """
    checks if the game is over by winning
    :param word: the word player 1 chose
    :param guess_list: the letters player 2 has guessed so far
    :return: True if player 2 guesses the word
    """
    i = 0
    for letter in word:
        if letter in guess_list:
            i += 1
    if i == len(word):
        return True

def main() -> None:
    """
    main function that calls all other functions
    :return: nothing
    """
    # collects secret word and returns as question marks
    secret = secret_word(get_secret_word())
    print('\n' * 30)

    # keeps track of user guesses
    guess_list = []
    i = 0
    while i != 7:
        word, secret_w = secret
        # displaying hangman
        display_hangman(i)
        # secret word display
        display_word_mod(guess_list, word)
        # which characters that were guessed
        guess_list.sort()
        print_guess = ', '.join(guess_list)
        print()
        print('So far you have guessed:', print_guess)
        guess_list.append(get_guess(guess_list))
        for letter in guess_list:
            if letter not in word:
                i += 1
        # checking if game is over
        if is_game_over(word, guess_list):
            print('You correctly guessed the secret word:', word)
            break
        if i == 7:
            display_hangman(i)
            print('You failed to guess the secret word:', word)
            break
        display_hangman(i)
        i = 0

main()
