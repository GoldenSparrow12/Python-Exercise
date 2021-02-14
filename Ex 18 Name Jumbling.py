""" Name jumbling """
import random

number = int(input("How Many name you enter? "))
names = []
print("Enter the name with lastname")
for i in range(number):
    name = input()
    names.append(name)

name_lst = [na.split(" ") for na in names]

f_name = [f_na[0] for f_na in name_lst]
l_name = [l_na[1] for l_na in name_lst]
for i in range(number):
    f_random = random.choice(f_name)
    l_random = random.choice(l_name)
    print(f_random, l_random)
