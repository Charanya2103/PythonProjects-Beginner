#Coffee Machine
stop_func=True
coffee_cost={
    "cappuccino":250,
    "expresso":150,
    "water":100,
    }
def cofe(coffee):
  global total
  global stop_func # Declared global at the start of the function
  if coffee=='report':
    print(f"Water:1l\nMilk:50ml\nCoffee:58g\nMoney:{total}")
    return
  if coffee=="exit":
    stop_func=False
    return
  print(f"You have selected {coffee}")
  print(f"The cost of {coffee} is {coffee_cost[coffee]} ")
  print("Please enter coins:")
  fives=int(input("How many fives:"))
  tens=int(input("How many tens:"))
  twenties=int(input("How many twenties:"))
  total=fives*5+tens*10+twenties*20
  print(f"The total amount is {total}")
  if total==coffee_cost[coffee]:
    print("Please collect your coffee")
  elif total>coffee_cost[coffee]:
    print("Please collect your coffee")
    print(f"The change is {total-coffee_cost[coffee]}")
  else:
    print("Enter correct amount..")
    cofe(coffee)

# Fix: Delete the overwritten 'input' variable to restore the built-in function
if 'input' in globals() and not callable(globals()['input']):
    del input

while stop_func==True:
  print("Hi....!,I am here to refresh your mind!")
  coffee=input("Which type of coffee you would like to prefer!!(latte/cappuccino/expresso/water)")
  cofe(coffee)
