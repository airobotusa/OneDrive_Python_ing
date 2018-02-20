#!/usr/bin/env python
"""guesser.py, by Richard White, 2012-01-16
This program has the user guess a number between 1 and 100.
"""

def main():
	print "Guess a number between 1 and 100."
	randomNumber = 35
	found = False	#flag variable to see
					# if they guessed it
	while not found:
		userGuess = input("Your guess: ")
		if userGuess == randomNumber:
			print "You got it!"
			found = True
		else:
			print "That is not it."

if __name__ == "__main__":
	main()
	