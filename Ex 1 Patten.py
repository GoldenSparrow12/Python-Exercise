"""This Program are generate * patten.
 if chose 1 then generate top to bottom
  if chose 0 then generate bottom to top"""
number = int(input("Enter The Number "))
bo = int(input("Enter 0 or 1 "))
bol = bool(bo)

if bol is True:
    for i in range(1, number + 1):
        print("* " * i)
elif bol is not True:
    for i in range(number, 0, -1):
        print("* " * i)
else:
    print("Invalid Input")
