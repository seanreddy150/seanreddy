#Hangman Game

import random
from time import sleep

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
-------------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
-------------
""",
"""
 ------
 |    |
 |    O
 |    +
 | 
 |   
 |   
-------------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
-------------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
-------------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\ 
 |   
 |   
 |   
-------------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\ 
 |    | 
 |   
 |   
-------------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\ 
 |    |
 |    |
 |   
-------------
""","""
 ------
 |    |
 |    O
 |  /-+-\ 
 |    |
 |    |
 |   /
-------------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\ 
 |    |  
 |    | 
 |   / \ 
-------------
""")

WORD_BANK = ("SHARK", "LIGHT", "PHONE", "COUCH", "APPLE", "BIRDS", "MAINE", "BLACK", "SHOES", "BEARD")
choice = random.choice(WORD_BANK)
SUCCESSFUL_ATTEMPTS = ("Great!", "You Got It!")
MAX_WRONG = len(choice) + 5 
so_far = ("-") * len(choice)
used = []
wrong = 0

print("\t \t Welcome to Hangman!")
print()
input("Press Enter to START: ")

while wrong < MAX_WRONG and so_far != choice:
    print()
    print(HANGMAN[wrong])
    print("Words already used: ", so_far)
    print("Letters already used: ", used)

    guess = input("Please guess a letter: ").upper()
    print()

    while guess in used:
        print("Try again... You've already used this letter")
        guess = input("Guess a letter: ").upper()
        print()
    used.append(guess)

    if guess in choice:
        print(random.choice(SUCCESSFUL_ATTEMPTS),"...Updating words that have been used thus far...")

        new = ""
        for i in range(len(choice)):
            if guess == choice[i]:
                new += guess

            else:
                new += so_far[i]
        so_far = new 

    else:
        print("Not quite, please try again!")
        wrong += 1

print("Game Outcome:")
if wrong == MAX_WRONG:
    print("Not quite, better luck next time!")

else:
    print("You got it, Nice Job!")

print()
print()
input("Press Enter to Leave: ")