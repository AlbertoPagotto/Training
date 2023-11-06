from replit import clear
#HINT: You can call clear() to clear the output in the console.

print("Welcome to the secret auction program.")
my_dict={}
flag=False
while flag==False:
  clear()
  name=input("What is your name?: ")
  bid =input("What's your bid?: ")
  my_dict[name]=bid
  end_bid=input("Are there any other bidders? Type 'yes' or 'no'. ")
  if end_bid=="no":
    flag=True
    
print(my_dict)
max_bid=0
for key in my_dict:
  L=len(my_dict[key])
  if float(my_dict[key][1:L])>=float(max_bid):
    max_bid=my_dict[key][1:L]
    max_name=key

print(f"The winner is {max_name} with a bid of ${max_bid}")