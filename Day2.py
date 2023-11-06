#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
tot_bill=float(input("How much is your bill in $? "))
people=int(input("How many people? "))
tip=float(input("is the tip 10, 12 or 15%? "))
x=round(tot_bill/people*(1+tip/100),2)
print(f"Each person should pay {x} dollars")

x="{:.2f}".format(x) #in this way it rounds to the 2 digit
print(f"Each person should pay {x} dollars")