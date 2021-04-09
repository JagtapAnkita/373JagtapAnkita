import random
n = random.randint(1,100)

number_of_guesses = 1
print("\n...Welcome to number guessing game...\n")
print("Remember You have only 10 guesses \n")
while number_of_guesses <= 10:
    guess_number=int(input("Guess the number: \n"))
    if guess_number<18:
        print("Entered number is small,"
              "please enter greater number \n")
    elif guess_number>18:
        print("Entered number is large,"
              "please enter small number \n")
    else:
        print("\n ...Congratulations You won... \n")
        print("Number of guesses took to finish: \n",number_of_guesses)
        break
    print("Number of guesses left: \n",10-number_of_guesses)
    number_of_guesses=number_of_guesses+1

if number_of_guesses > 10:
    print("\n ...Game over...You loose the game \n")
