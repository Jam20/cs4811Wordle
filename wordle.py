####
# CS4811 Artificial Intelligence
# Group Calliban
# James Brouckman, Tracy Gaolese, Dasker Masker
# Balaji Mediboin, John Mware, Colin VanDelden
# Week 2 In-Class
# 1/18/2023
#
# The computer can be run with computer()
####
import math
import random
targetWord = ""
guesses = 0
guessedWords = []
results = []
dictionary = []


####
# Setup the game for a match
####
def playWordle():
    global targetWord
    global guesses
    global guessedWords
    global results
    global dictionary
    # Local function to check if a word is 5 letters for the filter
    def isFiveLetterWord(val):
        return len(val) == 5

    # Load in all the possible wordle words.
    dictionary = []
    with open("words_alpha.txt", 'r') as file:
        fileData = file.read()
        dictionary = list(filter(isFiveLetterWord,fileData.split("\n")))

    # Set the target word to a random word in the dictionary.
    targetWord = dictionary[math.floor(random.random() * len(dictionary))]

    # Print out the welcome message.
    print("Welcome To Wordle")
    print("Upper case letters are in the correct location")
    print("Lower case letters are in the word but incorrectly placed")
    print("missing letters are not in the word")
    print("Make a Guess")

####
# End the game and give up
####
def giveUp():
    global guesses
    global guessedWords
    global results
    global targetWord
    print("You Gave Up")
    print("The word was " + targetWord)
    targetWord = ""
    guesses = 0
    guessedWords.clear()

####
# Make another guess
####
def makeGuess(word: str):
    global guesses
    global guessedWords
    global targetWord

    guesses = guesses + 1
    if(guesses>6 or targetWord == ""): giveUp()

    guessedWords.append(word)
    print(f"you guessed {word} this is guess: {guesses}\n")
    textToPrint = ""

    # The word was guessed correctly.
    if(word == targetWord):
        print("You guessed the correct word!!!")
        targetWord = ""
        guesses = 0
        guessedWords.clear()
        return None

    # Transform the word.
    for i in range(len(word)):
        if(word[i] == targetWord[i]):
            textToPrint = textToPrint + word[i].capitalize()
        elif(word[i] in targetWord):
            textToPrint = textToPrint + word[i].lower()
        else:
            textToPrint = textToPrint + "_"

    # Print text for the player.
    print(textToPrint)
    results.append(textToPrint)

    # Create the return dictionary for the computer.
    dictionary = dict()
    dictionary["guesses"] = guesses
    dictionary["wordsUsed"] = guessedWords
    dictionary["wordResults"] = results

    return dictionary

####
# Print out the state of the current board
####
def showState():
    global guesses
    global guessedWords

    # Inner function to show the state of the current word.
    def showStateWord(targetWord,guessword):
        pos = 0 #Placeholder to hold results position
        results = "" #Placeholder to hold final results
        for chars in guessword: #Loop through the guess word
            if pos == len(guessword): #Validate if number of characters in thre final results equals guess word
                break
            else:
                if chars.upper() == targetWord[pos].upper(): #Check if guess word character matches the target word characters. If yes, write the character in uppercase
                    results = results +""+ chars.upper() 
                else: #If the guess word character do not match, write the character in lowercase
                    if (chars.lower() in targetWord):
                        results = results +""+ chars.lower()
                    else: #If the character doesn't exist, append underscrore
                        results = results +"_"

            pos = pos + 1 
        return results
    
    # Print a nicely formatted result.
    print("Guesses:", guesses)
    wordResults = []
    for word in guessedWords:
        resultingWord = showStateWord(targetWord, word)
        wordResults.append(resultingWord)
        print("Guess word : ", word, "Results :", resultingWord)
    
    # Create and return a dictionary with data results.
    dictionary = dict()
    dictionary["guesses"] = guesses
    dictionary["wordsUsed"] = guessedWords
    dictionary["wordResults"] = wordResults

    return dictionary


####
# Removes a guessed word from the dictionary
####
def removeWordFromDictionary(guessedWord, wordResult):
    global dictionary

    # Does an uppercase letter check
    def removeWordByChar(char, charPos):
        global dictionary
        workingDictionary = dictionary.copy()
        for word in dictionary:
            if word[charPos] != char:
                workingDictionary.remove(word)
        dictionary = workingDictionary.copy()

    # Does a lowercase letter check
    def removeWordByPos(char):
        global dictionary
        workingDictionary = dictionary.copy()
        for word in dictionary:
            if char not in word:
                workingDictionary.remove(word)
        dictionary = workingDictionary.copy()

    # Does a contains letter check
    def removeWordByLetter(char):
        global dictionary
        workingDictionary = dictionary.copy()
        for word in dictionary:
            if char in word:
                workingDictionary.remove(word)
        dictionary = workingDictionary.copy()

    # Check every character of the result
    for pos, char in enumerate(wordResult):
        if char.isupper():
            removeWordByChar(char.lower(), pos)
        elif char.islower():
            removeWordByPos(char)
        else:
            removeWordByLetter(guessedWord[pos].lower())

####
# Simple computer player
####
def computer():
    global dictionary
    playWordle()
    for i in range(0, 6):
        res = makeGuess(dictionary[0])
        if res is None:
            print("I got it!")
            return
        removeWordFromDictionary(res["wordsUsed"][-1], res["wordResults"][-1])
    print("I failed to get it")
    
