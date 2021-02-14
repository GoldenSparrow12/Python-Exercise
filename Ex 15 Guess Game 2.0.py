"""This is a Guess game which can play two player.
 Guess the number between a and b
 for 2nd player the number will change
 who are guess the number in less trial it will win... """
from random import randint


def guess(number_guess):
    """this fu are use to guess the number and return the number of guess."""
    i = 0
    print(f"Guess The Number between {player_1} and {player_2}")
    while True:
        user_guess = int(input())

        if user_guess in range(player_1, player_2 + 1):
            i += 1

            if user_guess > number_guess:
                print("Guess the smaller number")
            elif user_guess < number_guess:
                print("Guess the greater number")
            elif user_guess == number_guess:
                print(f"Correct you took {i} trail for Guess\n")
                break
        else:
            print(f"\tGuess is not in range of {player_1} and {player_2}")
            print("\tGuess Again")
    return i


if __name__ == '__main__':
    player_1 = int(input("Enter the value of a\n"))
    player_2 = int(input("Enter the value of b\n"))

    print('''\n\tPlayer 1's Turn\n''')
    number_guess_1 = randint(player_1, player_2)
    p1 = guess(number_guess_1)
    print('''\tPlayer 2's Turn\n''')
    number_guess_2 = randint(player_1, player_2)
    p2 = guess(number_guess_2)
    print(f"The Number of Player 1 is {number_guess_1} and for Player 2 is {number_guess_2}")
    if p1 < p2:
        print("Player 1 Win..")
    elif p1 > p2:
        print("Player 2 Win..")
    else:
        print("Draw Match...")
