#Guess The Number
logo=""" _____                       _____ _            _   _                 _
|  __ \                     |_   _| |          | \ | |               | |
| |  \/_   _  ___  ___ ___    | | | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __
| | __| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |
 \____/\__,_|\___||___/___/   \_/ |_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|


"""
import random
print(logo)
easy_attempt=10
hard_attempt=5
def display():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 50.")
  level=input("Choose level of difficulty...Type 'easy' or 'hard':")
  if level=="easy":
    find_level(easy_attempt)
  if level=="hard":
    find_level(hard_attempt)
def find_level(attempt):
  print(f"You have {attempt} attempts to guess the number!")
  number=random.randint(1,50)
  while attempt>0:
    attempt-=1
    guess=int(input("Make a guess:"))
    if attempt==0 and guess!=number:
      print("You have run out of guesses.You lose")
      print(f"The answer is :{number}")
      break
    if guess>number:
      print("Your guess is too high!!")
      print(f"You have {attempt} attempts remaining to guess the number!")
    elif guess<number:
      print("Your guess is too low!!")
      print(f"You have {attempt} attempts remaining to guess the number!")
    elif guess==number:
      print(f"You got it!The answer was {number}")
      break
    else:
      print("Invalid Input")

display()
