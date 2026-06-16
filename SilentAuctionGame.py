#Silent Auction Program
import os
auction_details={}
def display():
  name=input("What is your name:")
  bid=int(input("What is your bid:"))
  auction(name,bid)
  ans=input("Are there any other bidders?Type 'yes' or 'no'.")
  if ans=="yes":
    os.system('cls')
    display()
  if ans=="no":
    find_winner(auction_details)
def auction(name,bid):
  auction_details[name]=bid
def find_winner(auction_details):
  highest_bid=0
  for name in auction_details:
    if auction_details[name]>highest_bid:
      highest_bid=auction_details[name]
      winner=name
  print(f"The winner is {winner} with a bid of ${highest_bid}")

display()
