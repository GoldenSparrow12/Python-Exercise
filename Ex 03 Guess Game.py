"""This is the Guess Game which can provide you to guess the number between 1 to 100.
   you have only 10 chance to Guess number."""
from random import randint

n = randint(1, 100)
i = 1
print("\tWelcome To The Guess Game")
while True:
    num = int(input("Guess The Number:"))
    if num == n + 1 or num == n + 2:
        print("Guess Minimum Less Number")
    elif num > n:
        print("Guess Less Number")
    elif num == n - 1 or num == n - 2:
        print("Guess Minimum Garter Number")
    elif num < n:
        print("Guess High Number")
    elif num == n:
        print('''\tCongest!! 
        You Guess The Number is {}
        in {} Try'''.format(num, i))
        break
    print("You have Left the guess", 10 - i)
    if i == 10:
        print("Game Over")
        break
    i += 1
