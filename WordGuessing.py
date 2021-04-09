import random
# To choose word randomly from list of words

# To enter the name of player
name = input("What is your name? ")

print("Good Luck ! ", name)

# List of words
words = ['rainbow', 'computer', 'science', 'program',
         'python', 'close', 'player', 'condition',
         'star', 'water', 'board', 'open']

# Function will choose one random word from this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ''

# any number of turns can be used here
turns = 10

while turns > 0:

    # To counts the number of times a user fails
    failed = 0

    for char in word:

        # comparing that character with the character in guesses
        if char in guesses:
            print(char)

        else:
            print("_")

            # for every failure, failed will increased by 1
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        print("...You Win...")

        # this print the correct word
        print("The word is: ", word)
        break

    # if input is wrong then it will ask user to enter another alphabet
    guess = input("guess a character:")

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:

        turns -= 1

        # if the character doesn’t match the word then “Wrong” will be displayed
        print("Wrong")

        # this will print the number of turns left
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")