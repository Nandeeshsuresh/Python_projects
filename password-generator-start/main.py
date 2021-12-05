#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_letters=""
for number in range(1,nr_letters+1):
  letter_no=random.randint(0,51)
  password_letters+=letters[letter_no]

password_numbers=""
for number in range(1,nr_symbols+1):
  number_no=random.randint(0,9)
  password_numbers+=numbers[number_no]

password_symbols=""
for number in range(1,nr_numbers+1):
  symbol_no=random.randint(0,8)
  password_symbols+=symbols[symbol_no]

print(f"{password_letters}{password_numbers}{password_symbols}")




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list_password=[]
for number in range(1,nr_letters+1):
  letter_no=random.randint(0,51)
  list_password+=letters[letter_no]


for number in range(1,nr_symbols+1):
  number_no=random.randint(0,9)
  list_password+=numbers[number_no]


for number in range(1,nr_numbers+1):
  symbol_no=random.randint(0,8)
  list_password+=symbols[symbol_no]

random.shuffle(list_password)

random_final_password=""

for character in list_password:
   random_final_password+=number

print(f"Your password is: {random_final_password}")
