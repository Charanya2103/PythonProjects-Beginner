#HIGHER-LOWER
import random
import os
score=0

logos="""         _________ _______           _______  _______
|\     /|\__   __/(  ____ \|\     /|(  ____ \(  ____ )
| )   ( |   ) (   | (    \/| )   ( || (    \/| (    )|
| (___) |   | |   | |      | (___) || (__    | (____)|
|  ___  |   | |   | | ____ |  ___  ||  __)   |     __)
| (   ) |   | |   | | \_  )| (   ) || (      | (\ (
| )   ( |___) (___| (___) || )   ( || (____/\| ) \ \__
|/     \|\_______/(_______)|/     \|(_______/|/   \__/

 _        _______           _______  _______
( \      (  ___  )|\     /|(  ____ \(  ____ )
| (      | (   ) || )   ( || (    \/| (    )|
| |      | |   | || | _ | || (__    | (____)|
| |      | |   | || |( )| ||  __)   |     __)
| |      | |   | || || || || (      | (\ (
| (____/\| (___) || () () || (____/\| ) \ \__
(_______/(_______)(_______)(_______/|/   \__/

"""
VS="""          _______
|\     /|(  ____ \
| )   ( || (    \/
| |   | || (_____
( (   ) )(_____  )
 \ \_/ /       ) |
  \   /  /\____) |
   \_/   \_______)

"""
data=[
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',

    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',

    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality',
    }


]
def another(ans,c1,c2):
  os.system('cls')
  print(logos)
  global score
  if ans==1:
    c2=random.choice(data)
    print(f"Compare1:{c1['name']},{c1['description']}")
    print(VS)
    print(f"Compare2:{c2['name']},{c2['description']}")
    ans=int(input("Who has more followers?Type '1' or '2':"))
    find_answer(ans,c1,c2)
  if ans==2:
    c1=random.choice(data)
    print(f"Compare1:{c1['name']},{c1['description']}")
    print(VS)
    print(f"Compare2:{c2['name']},{c2['description']}")
    ans=int(input("Who has more followers?Type '1' or '2':"))
    find_answer(ans,c1,c2)


def find_answer(ans,c1,c2):
  global score
  if c1["follower_count"]>c2["follower_count"] and ans==1:
    score+=1
    print(f"You are correct..Your final score is {score}")
  elif c1["follower_count"]<c2["follower_count"] and ans==2:
    score+=1
    print(f"You are correct..Your final score is {score}")
  else:
    print(f"You are wrong..Your final score is {score}")
    return
  another(ans,c1,c2)


print(logos)
c1=random.choice(data)
c2=random.choice(data)

print(f"Compare1:{c1['name']},{c1['description']}")
print(VS)
print(f"Compare2:{c2['name']},{c2['description']}")
ans=int(input("Who has more followers?Type '1' or '2':"))
find_answer(ans,c1,c2)
