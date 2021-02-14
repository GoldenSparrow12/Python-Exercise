"""Enter the number and give the next palindrome number
"""


def palindrome(nu):
    nu += 1
    while str(nu) != str(nu)[::-1]:
        nu += 1
    return nu


if __name__ == '__main__':
    try:
        lst = []
        number = int(input("Number of case\n"))
        for i in range(number):
            in1 = int(input("Enter value\n"))
            lst.append(in1)
    except ValueError:
        print('''   This program only find numeric palindrome.
        Please enter numeric value only!!!''')
        exit()
    for i in range(number):
        print(f"The Next Palindrome of {lst[i]} is {palindrome(lst[i])}")
