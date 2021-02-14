"""Provide a range is divisor or not
"""

try:
    input_apple = int(input("How many apple you have? "))
    min_nu = int(input("What is the minimum number? "))
    max_nu = int(input("What is the maximum number? "))

    lst = [i for i in range(min_nu, max_nu + 1)]
    if min_nu == max_nu:
        print("This is not a Range...")
    elif min_nu>max_nu:
        print("Minimum is not garter than maximum")
    for nu in lst:
        if input_apple % nu == 0:
            print(f"{nu} is a divisor of {input_apple}")
        else:
            print(f"{nu} is not a divisor of {input_apple}")

except ValueError:
    print("Please Enter only numeric value")
