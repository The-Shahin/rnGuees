import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Enter number between 1 and 10 :"))
        if guess > random_number:
            print("Try again! It was too high")
        elif guess < random_number:
            print("Try again! It was too low")
    print("Congratulations! You won the fucking simple game")


guess(10)
