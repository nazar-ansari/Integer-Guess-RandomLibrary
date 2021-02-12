import random
# IMPORTING RANDOM MODULE
randnumber = random.randint(1, 100)  # Initializing random number
userGuess = None
guesses = 0
# Creating Through While loop
while(userGuess != randnumber):
    # Taking userGuess as an Integer input
    userGuess = int(input(" ENTER YOUR GUESS \n  "))
    guesses += 1
    if (userGuess == randnumber):
        print("*********YOUR GUESSSED IT RIGHT BRO !********")
    else:
        if (userGuess > randnumber):
            print("YOU GUESSED IT WRONG \n PLEASE ENTER THE SMALLER NUMBER")

        else:
            print("YOU GUESSES IT WRONG \n PLEASE ENTER THE LARGER NUMBER")
print(f"YOU HAVE GUESS THE NUMBER IN {guesses} GUESSES")
# END