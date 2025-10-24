import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")  

def guess_game():
    number_random = random.randint(1, 100)
    count = 0
    print(number_random)
    number = int(input("Make a guess: "))
     
    if(number == number_random):
        print(f"You guessed it right! The number was {number_random}.")

    else:
        while(number != number_random):
            print("Wrong guess. Try again!")
            count += 1
            number = int(input("Make a guess: "))

    print(f"You took {count} attempts to guess the number.")

guess_game()