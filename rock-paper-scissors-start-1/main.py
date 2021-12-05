rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game=[rock,paper,scissors]


user_chose=int(input("What do you choose?Type 0 for Rock,1 for Paper or 2 for Scissors."))

if user_chose == 0:
  print(game[0])

elif user_chose == 1:
  print(game[1])

elif user_chose==2:
  print(game[2])  

print("computer choose :")
computer_chose=random.randint(0,2)
print(game[computer_chose])

if user_chose==0 and computer_chose == 0 :
  print("Draw")

elif user_chose==0 and computer_chose == 1 :
  print("Computer wins")

elif user_chose==0 and computer_chose == 2 :
  print("User wins")

elif user_chose==1 and computer_chose == 0 :
  print("User wins")

elif user_chose==1 and computer_chose == 1 :
  print("Draw")  

elif user_chose==1 and computer_chose == 2 :
  print("Computer wins")

elif user_chose==2 and computer_chose == 0 :
  print("Computer wins")

elif user_chose==2 and computer_chose == 1 :
  print("User wins")

elif user_chose==2 and computer_chose == 2 :
  print("Draw")


else:
  print(" User chose invalid number you lose.")
