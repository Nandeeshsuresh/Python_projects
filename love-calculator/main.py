# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

name1=name1.lower()
name2=name2.lower()

total_name=name1+name2

T=total_name.count('t')
R=total_name.count('r')
U=total_name.count('u')
E=total_name.count('e')

TRUE=T+R+U+E

L=total_name.count('l')
O=total_name.count('o')
V=total_name.count('v')
E=total_name.count('e')

LOVE=L+O+V+E

    
score=int(f"{TRUE}{LOVE}")


if score<10:
  print(f'Your score is {score}, you go together like coke and mentos.')

if score>40 and score<50 :
  print(f"Your score is {score}, you are alright together. ")

else:  
  print(f"Your score is {score}")   







