# Simple-Password-Generator
Hi Iam a beginner to python language and wanted to create some easy projets using python.Here is my beginner friendly version of Password generator.

Download or git clone the password.py and run it with python3 to use this random password generator.

since I used lowercase and uppercase alphabets ,digits and special characters the generated password have some cryptographic strongness.

This program will get length of the password as input from the user If you want to Use a Random length uncomment the input line.

import random,string

#creating a empty string 

a=""

#un-comment below line if u want to use random length

#length=random.randint(6,15)

length=int(input("Enter Your Password's Length = "))

#string.ascii_lowercase returns all lower case alphabets

#string.ascii_uppercase returns all upper case alphabets

set=string.ascii_lowercase+string.ascii_uppercase+string.digits+"!@#$%^&*(){}[]"

#joining the random values to empty string

print(a.join(random.choice(set) for i in range(0,length)))
