#import art and data
import art 
from game_data import data
from random import randint
score=0
from replit import clear

option1=randint(0,49)
print(art.logo)


game_continues=True
while game_continues:
    option2=randint(0,49)
    if option1 == option2 :
      option2=randint(0,49)
    # print(f"{data[option1]['follower_count']}")
    # print(f"{data[option2]['follower_count']}")  
    print(f"Compare A: {data[option1]['name']}, a {data[option1]['description']}, from {data[option1]['country']}.")
    print(art.vs)
    print(f"Against B: {data[option2]['name']}, a {data[option2]['description']}, from {data[option2]['country']}.")
    answer=input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a":
      answer=option1
    elif answer == "b":
      answer=option2
    
    clear()
    print(art.logo)


    if data[option1]["follower_count"]>data[option2]["follower_count"] and data[answer]["follower_count"]>data[option2]["follower_count"] :
        score = score+1
        print(f"You are right! Current score {score} ")
        option1=option2
      
      
    elif data[option1]["follower_count"]<data[option2]["follower_count"] and data[option1]["follower_count"]<data[answer]["follower_count"]:
      score = score+1
      print(f"You are right! Current score {score} ")
      option1=option2
      
      
    else:
      print(f"Sorry, that's wrong. Final score: {score} ")  
      game_continues= False
      

