"""The Snack Water And Gun Game"""
import random


def game():
    u_win = 0
    c_win = 0
    d_match = 0
    i = 1
    print('''\tWelCome To The Snack Water And Gun Game ''')
    while i <= 10:
        print(f"\t****** {i} Turn ******")
        lst = ["Snack", "Water", "Gun"]
        computer_choose = random.choice(lst)
        dic1 = {"S": "Snack", "W": "Water", "G": "Gun"}
        for key, value in dic1.items():
            print(f"Enter {key} for Choose {value}")
        user_choose = input().upper()
        if user_choose not in dic1.keys():
            print("Invalid Input")
            print("Restart The Game")
            game()

        else:
            if computer_choose == "Snack":
                if user_choose == "S":
                    print("Draw Match")
                    d_match += 1
                elif user_choose == "W":
                    print("Computer Win")
                    c_win += 1
                else:
                    print("You win")
                    u_win += 1
            elif computer_choose == "Water":
                if user_choose == "S":
                    print("You win")
                    u_win += 1
                elif user_choose == "W":
                    print("Draw match")
                    d_match += 1
                else:
                    print("Computer Win")
                    c_win += 1
            elif computer_choose == "Gun":
                if user_choose == "S":
                    print("Computer Win")
                    c_win += 1
                elif user_choose == "W":
                    print("You win")
                    u_win += 1
                else:
                    print("Draw Match")
                    d_match += 1
        i += 1
    print("\n******* RESULT ********")
    print(f"You Win {u_win} Times")
    print(f"Computer Win {c_win} Times")
    print(f"Draw The Match {d_match} Times")
    if u_win > c_win:
        print("You Win This Game")
    elif u_win < c_win:
        print("You Lose This Game")
    else:
        print("Tie This Game")


game()
