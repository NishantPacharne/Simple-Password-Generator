import random,string
a=""
length=int(input("Enter Your Password's Length = "))
set=string.ascii_lowercase+string.ascii_uppercase+string.digits+"!@#$%^&*(){}[]"
print(a.join(random.choice(set) for i in range(0,length)))