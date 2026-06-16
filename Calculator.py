#Calculator
def display2(result):
  print("+\n-\n*\n/\n")
  op=input(" Pick an operation:")
  num2=int(input("Enter next number:"))
  if op=="+":
    results=result+num2
    print(f"{result}{op}{num2}={results}")
  if op=="-":
    results=result-num2
    print(f"{result}{op}{num2}={results}")
  if op=="*":
    results=result*num2
    print(f"{result}{op}{num2}={results}")
  if op=="/":
    results=result/num2
    print(f"{result}{op}{num2}={results}")
  result=results
  print(display3(result))
def display():
  num1=int(input("Enter first number:"))
  print("+\n-\n*\n/\n")
  op=input(" Pick an operation:")
  num2=int(input("Enter next number:"))
  if op=="+":
    result=num1+num2
    print(f"{num1}{op}{num2}={result}")
  if op=="-":
    result=num1-num2
    print(f"{num1}{op}{num2}={result}")
  if op=="*":
    result=num1*num2
    print(f"{num1}{op}{num2}={result}")
  if op=="/":
    result=num1/num2
    print(f"{num1}{op}{num2}={result}")
  a=display3(result)
  print(a)
def display3(result):
  ans=input(f"Enter 'y' to continue calculation with {result} or 'n' to start new calculation or 'x' to exit:")
  if ans=="y":
    display2(result)
  if ans=="n":
    display()
  if ans=="x":
    return


display()
