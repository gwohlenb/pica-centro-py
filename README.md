# pica-centro-py

Pica Centro game

Objective:
* To guess a secret number of a specified length in the fewest attempts
* Each digit in the secret number is in the range of 0-9; there can NOT be duplicates

Rules:
* To make an guess, enter a number of the specified length, followed by a CR
* In response, the program prints a string with the following digit clues:
  * P = (pica) the digit is part of the answer but not in the right position
  * C = (centro) the digit is part of the answer and is in the correct position
  * X = the digit is not part of the answer
* Continue guessing until you figure out the secret number or run out of guesses (max 20)
* You can give up by pressing CTRL-C

To Run:
* **python pica-centro.py <secret_number_length>**
* or
* **python3 pica-centro.py <secret_number_length>**
* where secret_number_length is optional; default is 4
* hit CTRL-c to give up

Example:
* **python pica-centro.py 6**
* will run the program with a secret number of 6 digits in length
