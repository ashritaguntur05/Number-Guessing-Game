import random
import art
print(art.logo)
def guess_number(value):
    num=random.randint(1,100)
    if value=="easy":
        turns=10

    else:
        turns=5
    print(f"You have {turns} turns to guess the number")
    for i in range(0,turns):
        guess=int(input("guess a number between 1 to 100"))
        if guess>num:
            print("you've guessed too high , guess again :(")
        elif guess<num:
            print("you've guessed too low , guess again :(")
        elif guess==num:
            print(f"congrats!! you found the number that is {num}")
            exit()
    print(f"{num} is the actual number")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100")
value=input("Choose a difficulty. Type 'easy' or 'hard'").lower()
guess_number(value)
