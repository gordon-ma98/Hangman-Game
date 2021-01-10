# Hangman game
#

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


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    letters = list(secretWord)
    result = all(i in lettersGuessed for i in letters)
    return result

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
   
    ans = []
    for i in secretWord:
        if i in lettersGuessed:
            ans.append(i)
        else:
            ans.append("_ ")   
    return "".join(ans)
                    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    longss = string.ascii_lowercase
    available = ""
    
    for i in longss:
        if i in lettersGuessed:
            available == available
        else:
            available += i
    return available
        
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
    
    #Intro
    print("Welcome to the game, Hangman!")
    length_of_word = str(len(secretWord))
    print("I am thinking of a word that is", length_of_word, "letters long.")
    print("-------------")
    
    #Variables
    guesses = 8
    lettersGuessed = []
    guessInLowerCase = str
    
    while guesses >= 0:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            return 'Congratulations, you won!'
            break
        print("You have", guesses, "guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        guessInLowerCase = input(str("Please guess a letter: ")).lower()
        if guessInLowerCase in secretWord:
            if guessInLowerCase in lettersGuessed:
                print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guessInLowerCase)
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
        else:
            if guessInLowerCase in lettersGuessed:
                print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guessInLowerCase)
                guesses -= 1
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            
        if guesses == 0:
             print ('Sorry, you ran out of guesses. The word was ' + secretWord)
             break

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
