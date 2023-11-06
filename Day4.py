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
mychoice=input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n")
mychoice=int(mychoice)
if mychoice==0:
  print("You have chosen Rock")
elif mychoice==1:
  print("You have chosen Paper")
elif mychoice==2:
  print("You have chosen Scissors")
else:
  print("ERROR: invalid input")

compchoice=random.randint(0,2)
if compchoice==0:
  print("The laptop has chosen Rock")
elif compchoice==1:
  print("The laptop has chosen Paper")
elif compchoice==2:
  print("The laptop has chosen Scissors")
row1=["Even","You loose","You win"]
row2=["You win","Even","You loose"]
row3=["You loose","You win","Even"]
combin=[row1,row2,row3]

print(combin[mychoice][compchoice])