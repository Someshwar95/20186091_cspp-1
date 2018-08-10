'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
@author: Someshwar95
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def is_word_guessed(secretWord, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
        if i in letters_guessed:
            return True
    return False

def get_guessed_word(secretWord, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    str_var = ""
    for char in secretWord:
        if char not in letters_guessed:
            str_var += '_'
        else:
            str_var += char

    return str_var
def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    str_al = ""
    str_alp = "abcdefghijklmnopqrstuvwxyz"
    for i in str_alp:
        if i not in letters_guessed:
            str_al += i
    return str_al


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    wrong_guess_count = 8
    entered_string_by_user = ""
    l_em = []
    print(secretWord)
    while True:
        print("-----------")
        print("You have " +  str(wrong_guess_count) +" guesses left.")
        print("Available letters: " + get_available_letters(entered_string_by_user.split()))
        char_entered = input("Please guess a letter: ")
        entered_string_by_user = entered_string_by_user + " " + char_entered
        if char_entered not in l_em:
            if is_word_guessed(secretWord, entered_string_by_user.split()):
                print("Good guess: " + get_guessed_word(secretWord, entered_string_by_user.split()))
            else:
                print("Oops! That letter is not in my word: " + \
                    get_guessed_word(secretWord, entered_string_by_user.split()))
                wrong_guess_count -= 1
        else:
            print('Oops! Youve already guessed that letter:' + \
                get_guessed_word(secretWord, entered_string_by_user.split()))
        l_em = l_em + char_entered.split()
        if get_guessed_word(secretWord, entered_string_by_user.split()) == secretWord:
            print("Congratulations, you won!")
            break
        elif wrong_guess_count == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            break


def main():
    '''
    Main function for the given program

    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)




if __name__ == "__main__":
    main()
