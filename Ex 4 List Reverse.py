"""Reverse a list in multiple way.
use call by value
"""


def method1(lst1):
    lst1.reverse()
    print(lst1)


def method2(lst2):
    re = lst2[::-1]
    print(re)


def method3(lst3):
    for i in range(len(lst3) // 2):
        lst3[i], lst3[len(lst3) - i - 1] = lst3[len(lst3) - i - 1], lst3[i]
    print(lst3)


if __name__ == '__main__':
    try:
        lst = []
        lst_length = int(input("what is the length of list? "))
        print('''Enter the element''')
        for i in range(0, lst_length):
            lst_item = input()
            lst.append(lst_item)
        print(f"List is {lst}\n")

        method1(lst[:])  # copy of the list not a list
        method2(lst[:])
        method3(lst[:])

    except ValueError:
        print("Please Enter only numeric value")
