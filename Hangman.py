import json
import random

with open('C:/Users/lordnishant/Desktop/words_dictionary.json','r') as file:
    word_dict = json.load(file)
original_list = list(word_dict.keys())
word_list = [word for word in original_list if 4<=len(word)<=8]

def convert(list_of_chars):
        convert_to = ""
        for char in list_of_chars:
            convert_to += char
        return convert_to
    
def start():
    secret_word = random.choice(word_list)
    guesses = []
    blanks = [letter if letter in guesses else "_" for letter in secret_word]
    print("The word is : %s, there are %s letters"%(convert(blanks),len(secret_word)))
    counter = 0
    while True:
        guess = input("Guess a letter: ")
        while len(guess) != 1:
            guess = input("Input a single letter please: ")
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
                if counter == 6:
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
        start()
        if not play_again():
            return



            
                                                                                    

  
        
    
    