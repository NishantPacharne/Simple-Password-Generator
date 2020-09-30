import random,string
a=""

# asking the user if he wants a random lenght password?

random_custom_input = input("Do you want to have a password with random lenght (y/n) = ")
if random_custom_input == "y":
    length=random.randint(6,15)
else:
    length=int(input("Enter Your Password's Length = "))


set=string.ascii_lowercase+string.ascii_uppercase+string.digits+"!@#$%^&*(){}[]"
print(a.join(random.choice(set) for i in range(0,length)))