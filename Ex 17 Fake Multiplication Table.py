"""
Enter the number for the multiplication table.
and check the multiplication table and give the index which table was wrong!!

"""
from random import randint


def wrongTable(number):
    """fu give the list of multiplication table for given number.
    give the wrong multiplication of random generated number """
    wrong_nu = randint(0, 9)
    lst = [(i * number) if i != wrong_nu else i * number + randint(1, 10) for i in range(1, 11)]
    return lst


def checkTable(number, lst):
    for i in range(1, 11):
        if lst[i - 1] != i * number:
            return i
    return None


if __name__ == '__main__':

    try:
        n = int(input("Enter a number: "))

        wrong_table = wrongTable(n)
        print("\tMultiplication Table")
        print(wrong_table)
        index = checkTable(n, wrong_table)
        if index is not None:
            print(f"The Table is Wrong in position {index}")
        else:
            print("Table Correct!!")

    except ValueError:
        print("Please Enter only numeric value")
