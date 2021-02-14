""" This is a program to log or retrieve the data of 3 people."""
import datetime

client_name = {1: "Jay", 2: "Ram", 3: "Krishna"}
log_list = {1: "Log", 2: "Retrieve"}
food_list = {1: "Exercise", 2: "Food"}
ext = True


def getdate():
    """This function get date"""
    return datetime.datetime.now()


def log(fx, name):
    """This function for Log the data"""
    date = getdate()
    fx = fx  # fx= food_exercise
    name = name

    if fx == 1:
        data = input("Type Here\n")
        if name == 1:
            with open("Jay_Exercise", "a") as f:
                f.write(f"{str([str(date)])}:{data}\n")
            print("Successful Write")
        elif name == 2:
            with open("Ram_Exercise", "a") as f:
                f.write(f"{str([str(date)])}:{data}\n")
            print("Successful Write")
        elif name == 3:
            with open("Krishna_Exercise", "a") as f:
                f.write(f"{str([str(date)])}:{data}\n")
            print("Successful Write")
    elif fx == 2:
        data = input("Type Here\n")
        if name == 1:
            with open("Jay_Food", "a") as f:
                f.write(f"{str([str(date)])}:{data}\n")
            print("Successful Write")
        elif name == 2:
            with open("Ram_Food", "a") as f:
                f.write(f"{str([str(date)])}:{data}\n")
            print("Successful Write")
        elif name == 3:
            with open("Krishna_Food", "a") as f:
                f.write(f"{str([str(date)])}:{data}\n")
            print("Successful Write")


def retrieve(fx, name):
    """This function for the Retrieve the Data"""
    fx = fx
    name = name
    if fx == 1:
        if name == 1:
            with open("Jay_Exercise") as f:
                print(f.read())
        elif name == 2:
            with open("Ram_Exercise") as f:
                print(f.read())
        elif name == 3:
            with open("Krishna_Exercise") as f:
                print(f.read())
    elif fx == 2:
        if name == 1:
            with open("Jay_Food") as f:
                print(f.read())
        elif name == 2:
            with open("Ram_Food") as f:
                print(f.read())
        elif name == 3:
            with open("Krishna_Food") as f:
                print(f.read())


def longretrive():
    """This Is The function which is call the other function"""
    try:
        print("\tSelect Client Name")
        for key, value in client_name.items():
            print(f"\t\tPress {key} for {value}\n", end="")
        name = int(input())
        if name <= 3:
            print(f"\tSelected Client {client_name[name]}\n", end="")
        else:
            print("Invalid Input for Client Name")
            again()

        if ext is True:
            print("\tWhat You Want to Do?")
            for key, value in log_list.items():
                print(f"\t\tPress {key} for {value}\n", end="")
            lr = int(input())
            if lr <= 2:
                print(f"\tYou Chose {log_list[lr]} Data\n", end="")
            else:
                print("Invalid Input for Log & Retrieve")
                again()

            if ext is True:
                print("\tFor What")
                for key, value in food_list.items():
                    print(f"\t\tPress {key} for {value}\n", end="")
                fx = int(input())
                if fx <= 2:
                    print(f"\tYou Select {log_list[lr]} the {food_list[fx]}\n", end="")
                else:
                    print("Invalid Input for Food & Exercise")
                    again()

                if lr == 1:
                    log(fx, name)
                    again()
                elif lr == 2:
                    retrieve(fx, name)
                    again()
    except Exception:
        print('''Invalid Input!!
        Please Input only Number''')
        again()


def again():
    """This function are use to do the loop"""
    ag = input('''
    Do You Done Operation Again?
    Type y for Yes Or n For No.
    ''')
    if ag == "y":
        longretrive()
    elif ag == "n":
        print("See You Later")
        global ext
        ext = False
    else:
        again()


longretrive()
