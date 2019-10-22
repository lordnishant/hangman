# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:17:47 2019

@author: lordnishant
"""
def convert(list_of_chars):
        convert_to = ""
        for char in list_of_chars:
            convert_to += char
        return convert_to

def startgame():
    guesses = []
    secret_word = input("Set your secret word: ")
    while " " in secret_word:
        secret_word = input("Please only input one word! Try again:")
    blanks = [letter if letter in guesses else "_" for letter in secret_word]
    print('\n'*200)
    print("The word is : %s, there are %s letters"%(convert(blanks),len(secret_word)))
    counter = 0
    while True:
        guess = input("Guess a letter: ")
        while len(guess) != 1:
            guess = input("Input a single   letter please: ")
        if guess not in guesses: 
            guesses.append(guess)
            if guess in secret_word:
                blanks = [letter if letter in guesses else "_" for letter in secret_word]
                print("The word is now: " + convert(blanks))
                if convert(blanks).count('_') == 0:
                    print("You Win!")
                    return False
            else:
                print("That letter is not in my word. Try again.")
                counter += 1
                print("You have %s tries left."%(7 - counter))
                if counter == 7:
                    print("You have reached the maximum number of incorrect guesses. You lose! :)")
                    print("The word was: " + secret_word)
                    return False
        else:
            print("You've already guessed that. Try again.")
            
def play_again():
    while True:    
        answer = input("Do you want to play again? (Y/n): ")
        if not answer or answer.lower() in ('y', 'yes'):
            return True
        elif answer.lower() in ('n', 'no'):
            return False
        else:
            print("Not a valid answer!")

def hangman():
    while True:
        startgame()
        if not play_again():
            return
