""" This is a one type of faulty calculator which do some operation wrong. """
def Calculator():
    print("Welcome To Calculator.. Created By Harshit Thumar")
    op = input('''Please Type the Match operations:
                       + Addition
                       - Substation
                       * Multiplication
                       / Division
                       ** Power
                       % Module

                       Enter Your Choices:
                       ''')
    i1 = int(input("Enter The First Number:"))
    i2 = int(input("Enter The Second Number:"))

    if op == "+" and i1 == 56 and i2 == 9:
        print("77")
    elif op == "*" and i1 == 45 and i2 == 3:
        print("555")
    elif op == "/" and i1 == 56 and i2 == 6:
        print("4")
    elif op == "*":
        print(i1 * i2)
    elif op == "+":
        print(i1 + i2)
    elif op == "/":
        print(i1 / i2)
    elif op == "-":
        print(i1 - i2)
    elif op == "**":
        print(i1 ** i2)
    elif op == "%":
        print(i1 % i2)
    else:
        print("Invalid Input")
    again()


def again():
    ag = input('''      Do You Calculate Again?
            Type y for Yes Or n For No.
                ''').lower()
    if ag == "y":
        Calculator()
    elif ag == "n":
        print("See You Later")
    else:
        again()


Calculator()
