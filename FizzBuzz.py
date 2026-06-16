#FizzBuzz interview question
#divisible by 3=fizz,divisible by 5=buzz,divisible by 3 and 5=fizzbuzz,other just number
for i in range(1,101):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)
