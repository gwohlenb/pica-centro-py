# Pica Centro game; Python3 edition
# Objective: To guess a secret number of a specified length in the fewest attempts
#            Each secret number digit is in the range of 0-9; there can NOT be duplicates
# Rules: To make an guess, enter a number of the specified length, followed by a CR
#        In response, the program prints a string with the following character clues:
#          P = (pica) the digit is part of the answer but not in the right position
#          C = (centro) the digit is part of the answer and is in the correct position
#          X = the digit is not part of the answer
#        Continue guessing until you figure out the secret number or run out of guesses (max 20)
#        You can give up by pressing CTRL-C
#
# To run:
# python pica-centro.py <secret_number_length>
# where secret_number_length is optional; default is 4
# hit CTRL-C to give up
#
# Example:
# python pica-centro.py 6
# will run the program with a secret number of 6 digits in length
##
## Author: gwohlenb@yahoo.com
## GitHub: https://github.com/gwohlenb
## Date:   December 2023 (v2.0); adapted for Python3
####################################################
#!/usr/bin/env/python

import sys
import random
import typing # This is built-in to Python 3.9 or later

####################################################
def generateSecretNumber(secretNumberLength: int) -> list:
#
# This function returns a list of non-duplicate digits in
# the length specified. It is the number the user must guess
# in order to win the game

  secretNumber = list(range(10)) # generate a list of int from 0 to 9
                                 # this also prevents duplicates

  random.shuffle(secretNumber) # randomize it

  return secretNumber[:secretNumberLength]

####################################################

def collectGuess(secretNumberLength: int) -> typing.Tuple[bool, str]:
#
# This function collects a list of digits from the command
# line to serve as a guess of the secret number
#
# I looked into using raw mode but it adds too much complexity
# and has problems with multi-platform support; also hard to
# handle the ESC key as an exit method (need to use signal package)
#
# In Python 3.9 or later, you can type-hint a return tuple as follows:
# def collectGuess(secretNumberLength: int) -> tuple[bool, str]:

  isInvalid = False
  try:
    for guess in iter(sys.stdin.readline, ''):
      #print(guess, end='')
      guess = guess.rstrip('\n') # remove CR at end of guess
      if len(guess) < secretNumberLength:
        print("Invalid guess: length", len(guess), "is too short")
        isInvalid = True
      if guess.isnumeric() == False:
        print("Invalid guess: contains non-numeric characters")
        isInvalid = True
      guess = guess[:secretNumberLength] #chop off any extra characters
      return isInvalid, guess
  except KeyboardInterrupt:
    print("CTRL-C received, exiting program")
    exit()

####################################################

def analyzeDigit(digit: str, index: int, secretNumber: list):
  result = 'X' # default to "not found"

  for position, value in enumerate(secretNumber, start=1):
    if int(value) == int(digit):
      #print("Found a match for digit", digit, "at position", position)
      if int(position) == int(index):
        result = 'C' # present in correct position
      else:
        result = 'P' # present in incorrect position
      continue # don't need to worry about duplicates in the secretNumber
  return result

####################################################

def analyzeGuess(guess: list, secretNumber: list):
  isSolved = True
  analysisString: str = "" # immutable type so can't pass by ref
  for index, digit in enumerate(guess, start=1):
    result = analyzeDigit(digit, index, secretNumber)
    if result != 'C': # any non-centro result means a partial solution
      isSolved = False
    analysisString += result
  #print("analysisString =", analysisString)
  return isSolved, analysisString

####################################################
# MAIN
####################################################

def main():
  MAX_SECRET_NUMBER_LENGTH = 10
  MAX_GUESS_COUNT = 20

  print("Welcome to Pica Centro")
  print("Press CTRL-C to give up")

  if sys.version_info < (3,8):
    print("You need python 3.8 or later to run this program")
    exit()

  secretNumberLength = int(4) # default length if the user doesn't specify otherwise on the command line
  if len(sys.argv) > 1:
    secretNumberLength = int(sys.argv[1])

  if ((secretNumberLength < 1) or (secretNumberLength > MAX_SECRET_NUMBER_LENGTH)):
    print("Your secret number can contain from 1 to", MAX_SECRET_NUMBER_LENGTH, "digits")
    exit()
  print("The secret number contains", secretNumberLength, "digits")
  secretNumber = generateSecretNumber(secretNumberLength)
  print("The secret number is", secretNumber)

  guessCount = 0
  isSolved = False
  isInvalid = False # used to indicate if the current guess is invalid
  analysisString: str = ""
  while ((guessCount < MAX_GUESS_COUNT) and (isSolved == False)):
    guessCount += 1
    print("Enter guess #", guessCount, ":", sep='')
    isInvalid, guess = collectGuess(secretNumberLength)
    if isInvalid == True:
      continue
      # if the guess was improperly formatted, skip to the next guess
    print("You guessed", guess)
    isSolved, analysisString = analyzeGuess(guess, secretNumber)
    print(analysisString)
  if isSolved == True:
    print("You got it in", guessCount, "guesses!")
  else:
    print("You ran out of guesses! The secret number was", ''.join(str(i) for i in secretNumber))
    #print("You ran out of guesses! The secret number was", secretNumber)

####################################################
main()
####################################################
