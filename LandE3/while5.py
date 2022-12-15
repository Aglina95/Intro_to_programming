# Write your code here :-)
from random import randint
# Change the code below

secret_number = randint(1, 100)

while True:

    guess = int(input('I chose a number between 1 and 100. Which one? Your guess: '))
    if secret_number == guess:
        print("Correct!")
        break
    elif guess >= 1 and guess <= 100 and secret_number < guess:
        print("Wrong! My number is smaller.")
    elif guess >= 1 and guess <= 100 and secret_number > guess:
        print("Wrong! My number is larger.")
    else:
        print("I asked for a number between 1 and 100, not " + str(guess) + ".")


#Other Solution
guess = ''

secret_number = randint(1, 100)
while secret_number != guess:
    guess = int(input('I chose a number between 1 and 100. Which one? Your guess: '))
    if secret_number == guess:
        print("Correct!")
    elif guess >= 1 and guess <= 100 and secret_number < guess:
        print("Wrong! My number is smaller.")
    elif guess >= 1 and guess <= 100 and secret_number > guess:
        print("Wrong! My number is larger.")
    else:
        print("I asked for a number between 1 and 100, not " + str(guess) + ".")


