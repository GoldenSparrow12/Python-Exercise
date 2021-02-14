"""This program are find the email and save into a file"""
import re

str = '''
Note: Email can also be accessed through the COM Mobile App.
Step #1:
Go to https://outlook.com/com.edu for the Office 365 Email Login.

Step #2:
Your User ID is the same as your WebAdvisor User ID with, @com.edu.in.
jaykisan@yahoo.com
gtu@ac.edu.in
bagichelp@bajajallianz.co.in customercare@bajajallianz.co.in
For example, if your User ID is jdoe, then your Email User ID is jdoe@com.edu.in'''

find = re.findall(r'\w+@\S+\w+', str)
n = 1
with open("email.txt", 'a') as f:
    for i in find:
        f.write(f"Email_{n} : {i}\n")
        n += 1
