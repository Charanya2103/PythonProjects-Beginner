#Hangman Game(Project)
import random
print("Let's play Hangman!")
print("You have only 6 lives so try to guess the word within 6 attempts!Good Luck!")
lives=6
arr=[]
fruits=['apple','mango','cherry','grape']
fruit=random.choice(fruits)
for i in fruit:
  arr.append("_")
print(arr)
while lives>0:
  if "_" not in arr:
    break
  guess=input("Guess a letter:")
  if guess in fruit:
    for i in range(len(fruit)):
      if fruit[i]==guess:
        arr[i]=guess
    print(arr)
  else:
    if "_" not in arr:
      break
    print("You guessed",guess,"that is not present in the word.So you lose a life.")
    lives-=1
    print(lives)
    print(arr)
  if lives==5:
    print(" +---+\n |   |\n 0   |\n     |\n     |\n     |\n     |\n")
  if lives==4:
    print(" +---+\n |   |\n 0   |\n |   |\n     |\n     |\n     |\n")
  if lives==3:
    print(" +---+\n |   |\n 0   |\n/|   |\n     |\n     |\n     |\n")
  if lives==2:
    print(" +---+\n |   |\n 0   |\n/|\\ |\n     |\n      |\n     |\n")
  if lives==1:
    print(" +---+\n |   |\n 0   |\n/|\\ |\n /   |\n      |\n     |\n")
if '_' in arr:
  print("You lost the game!")
  print(" +---+\n |   |\n 0   |\n/|\\   |\n / \\ |\n     |\n     |\n")
else:
  print("You won the game!")




#We can also create a list of hangman then for index 0 lives will be 0 we can just access it using file_name.stages[lives]
#we can create a file  for words also.
