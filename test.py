import math
import random
targetWord = ""
guesses = 0
previousGuesses = []
results = []

def playWordle():

    def isFiveLetterWord(val):
        return len(val) == 5

    possibleWordleWords = []
    with open("words_alpha.txt", 'r') as file:
        fileData = file.read()
        possibleWordleWords = filter(isFiveLetterWord,fileData.split("\n"))

    targetWord = possibleWordleWords[math.floor(random.random() * len(possibleWordleWords))]
    print("Welcome To Wordle")
    print("Upper case letters are in the correct location")
    print("Lower case letters are in the word but incorrectly placed")
    print("missing letters are not in the word")
    print("Make a Guess")

def giveUp():
    print("You Gave Up")
    targetWord = ""
    guesses = 0
    previousGuesses.clear()

def makeGuess(word: str):
    guesses = guesses + 1
    if(guesses>6 or targetWord == ""): giveUp()

    previousGuesses.append(word)
    print(f"you guessed {word} this is guess: {guesses}\n")
    textToPrint = ""

    if(word == targetWord):
        print("You guessed the correct word!!!")
        targetWord = ""
        guesses = 0
        previousGuesses.clear()

    for i in range(len(word)):
        if(word[i] == targetWord[i]):
            textToPrint = textToPrint + word[i].capitalize()
        elif(word[i] in targetWord):
            textToPrint = textToPrint + word[i].lower()
        else:
            textToPrint = textToPrint + "_"
    print(textToPrint)
    results.append(textToPrint)
    dictionary = dict()
    dictionary["guesses"] = guesses
    dictionary["wordsUsed"] = previousGuesses
    dictionary["wordResults"] = results

    return dictionary

def showState():
    print(f"There have been {guesses} guesses the words are: {previousGuesses}")
    



    
