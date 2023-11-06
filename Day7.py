import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
count=0
lives=5
conditio=True
while conditio==True:
    guess = input("Guess a letter: ").lower()
    flag=0
    #Check guessed letter

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            count+=1
            flag=1
    if flag==0:
         lives-=1
    if not(count<word_length and lives>0):
        conditio=False
    
    print(display)
    print(f"Condition is {conditio} because is count is {count} and you have {lives} lives")

if lives!=0:
    print("You won")
else:
    print("You loose")