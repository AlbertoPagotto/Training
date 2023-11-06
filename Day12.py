import random
print("Welcome to the Number Guessing Name!\nI am thinking of a number between 1 and 100")

level=input("What level of difficulty do you choose? Type easy/hard: ")

def number_of_tries(difficulty):
  if difficulty.lower()=="easy":
    nr_attempts=5
    print(f"You have {nr_attempts} attempts.")
    return nr_attempts
  elif difficulty.lower()=="hard":
    nr_attempts=10
    print(f"You have {nr_attempts} attempts.")
    return nr_attempts
  else:
    print("ERROR: wrong typing")
    number_of_tries()

max_tries=number_of_tries(level)
number_to_guess=random.randint(1,100)

def guessing(attempt):
  your_guess=int(input("Make a guess: "))
  if your_guess<number_to_guess:
    attempt+=1
    if attempt>max_tries:
      print("You lost. You cannot try anymore.")
    else:
      print(f"Too low.\nGuess again.\nYou still have {max_tries-attempt+1}")
      guessing(attempt)
  if your_guess>number_to_guess:
    attempt+=1
    if attempt>max_tries:
      print("You lost. You cannot try anymore.")
    else:
      print(f"Too high.\nGuess again.\nYou still have {max_tries-attempt+1}")
      guessing(attempt)
  if your_guess==number_to_guess:
    print("Congratulations! You have guessed the right number.")

guessing(1)