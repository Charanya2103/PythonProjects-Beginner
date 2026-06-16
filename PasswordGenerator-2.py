import random
passwrd=[]
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*','(',')']
print("Welcome to the Password Generator!")
l=int(input("How many letters would you like in your password?"))
for i in range(l):
  le=random.choice(letters)
  passwrd.append(le)
s=int(input("How many symbols would you like?"))
for i in range(s):
  sy=random.choice(symbols)
  passwrd.append(sy)
n=int(input("How many numbers would you like?"))
for i in range(n):
  nu=random.randint(0,9)
  passwrd.append(nu)
random.shuffle(passwrd)
password=""
for i in passwrd:
  password=password+str(i)
print(password)
