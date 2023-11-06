import random

def get_card(yr_cards):
    yr_cards.append(random.choice(cards))
    print(f"Your cards: {yr_cards}") #You know your cards
    flag_get_card=input("Type 'y' to get another card, 'n' to pass: ") #Dealer's first cards is revealed
    if flag_get_card=='y':
        get_card(yr_cards)

def get_comp_card(cp_cards, cp_score):
    if cp_score<12:
        random_card=random.choice(cards)
        cp_cards.append(random_card)
        cp_score+=card_dict[random_card]
        if random_card=="A":
            if cp_score>10:
                cp_score+=1
            else:
                cp_score+=11
        get_comp_card(cp_cards, cp_score)
    final_cp_cards=cp_cards
    final_cp_score=cp_score
    return [final_cp_cards,final_cp_score]

cards=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_dict={
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 0,
}

print("WELCOME TO BLACKJACK!!!!")
play_flag=input("Do you want to play a Blackjack? Type y/n: ")

if play_flag=="n":
    print("See you next time!")
else:
    #Initialization
    your_cards=[]
    comp_cards=[]
    #You get your first card
    your_cards.append(random.choice(cards))
    #The dealer gets the first two cards
    comp_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
    print(f"Computer's first card: {comp_cards[0]}") #End initialization
    get_card(your_cards)
    
    #Calculation of your score
    your_score=0
    for card in your_cards:
        your_score+=card_dict[card]
    if your_cards.count("A")>0:
        if your_score>10:
            your_score=your_score+1
        else:
            your_score=your_score+11

    #Calculation of dealer's score
    comp_score=0
    for card in comp_cards:
        comp_score+=card_dict[card]
    if comp_cards.count("A")>0:
        if comp_score>10:
            comp_score+=1
        else:
            comp_score+=11
    [final_comp_cards,final_comp_score]=get_comp_card(comp_cards,comp_score)
    comp_cards=final_comp_cards
    comp_score=final_comp_score

    print(f"Computer's cards: {comp_cards}")
    print(f"You got {your_score}.\nYour opponet got {comp_score}.")
    
    #Evaluation of the winner

    if your_score>21 and comp_score>21:
        print("You both have a score higher than 21: you both loose!")
    elif your_score>21 and comp_score<=21:
        print("You have a score higher than 21: you loose!")
    elif your_score<=21 and comp_score>21:
        print("Your opponent has a score higher than 21: you win!")
    elif your_score<comp_score:
        print("Your opponent has a score higher than yours: you loose!")
    elif your_score>comp_score:
        print("You have a score higher than your opponent: you win!")
    elif your_score==comp_score:
        print("It's a draw!")
    else:
        print("ERROR: there's an error somewhere")
    

    

    


    

