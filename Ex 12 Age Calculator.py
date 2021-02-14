"""this program are take input year or age and
   return the year which you can turn in 100 year old."""


def hundred(age):
    """fun are count the hundred year"""
    i = 0
    while True:
        if age >= 100:
            break
        i += 1
        age += 1
    print(f"You Turn 100 year old in year {cur_year + i}")


if __name__ == '__main__':
    try:
        in1 = int(input("Enter Your Age/year"))
        cur_year = 2020
        if len(str(in1)) <= 3:
            age = in1
            if age > 100:
                print(f"Your age is {age} which is grater than 100 year")
            else:
                hundred(age)

        elif len(str(in1)) == 4:
            age = cur_year - in1
            hundred(age)
        else:
            print("Invalid Input")
    except Exception:
        print("Please Enter Numeric Value ")
