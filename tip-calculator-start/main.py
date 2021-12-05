#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welcome to the tip calculator")
bill=float(input("what was the total bill ? $"))
tip_percentage=input("how much tip would you like to give? 10, 12, or 15? ")
no_people=int(input("how many people will split the bill? "))

tip_percentagec=float(f"1.{tip_percentage}")

pay=(bill/no_people)*tip_percentagec
# print(pay)
# pay2=round(pay,2)
pay2="{:.2f}".format(pay)
print(f"Each person should pay: ${pay2}")
# print(type(pay2))