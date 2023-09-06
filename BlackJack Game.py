import random
import os
from art import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def clear_screen():
    # Check the operating system and clear the screen accordingly
    if os.name == 'posix':
        # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Other or unknown OS
        print("Sorry, clearing the screen is not supported on this operating system.")

def deal_cards():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculate the sum of cards and return the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, dealer_score):
    """Compare the users score and dealers score"""
    if user_score == dealer_score:
        return "Draw!"
    elif dealer_score == 0:
        return "You Lost! Dealer has a BlackJack"
    elif user_score == 0:
        return "You Won with a BlackJack"
    elif user_score > 21:
        return "You went over. You Lost!"
    elif dealer_score > 21:
        return "Dealer went over. You Won!"
    elif user_score > dealer_score:
        return "You Won!"
    elif user_score < dealer_score:
        return "You Lost!"

def play_again():
    print (logo)
    user_cards = []
    dealer_cards = []
    is_game_over = False

    #two cards need to be given to each so we will call for loop 2 times
    for _ in range(2):
        user_cards.append(deal_cards())    #adding card to user's list by append function in which we are calling deal_cards function
        dealer_cards.append(deal_cards())  ##adding card to dealer's list by append function in which we are calling deal_cards function

    #This while loop code is for user's card and score
    while not is_game_over:
        user_score = calculate_score(user_cards)    #calculating users score by calling calculate function
        dealer_score = calculate_score(dealer_cards)  ##calculating dealers score by calling calculate function

        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Dealer's first card: {dealer_cards[0]}")    #according to game rule only one card of dealer will be shown

        #if any of the given condition meets, game will be over 
        if user_score == 0 or dealer_score == 0 or user_score > 21:   
            is_game_over = True    #we will assign True to 'is_game_over' variable and the while loop will break
        else:
            #if any of the condition doesn't meet, we will ask user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            if user_should_deal == 'y':
                #if user want to have more card, we will again append card one by one to user_card list using 'deal_card' function
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    #This while loop code is for dealers card and score    
    while dealer_score != 0 and dealer_score < 17:
        #if dealers score is not 0(basically means not a blackjack i.e. 21) and score is less than 17 than by rule they need to have one more card
        dealer_cards.append(deal_cards())  #Appending cards to dealers card list by calling deal_card function
        dealer_score = calculate_score(dealer_cards)   #Calculating dealers score by calling calculate_scor function and passing the list of cards dealer have

    #Displaying users and dealers score    
    print(f"  Your final hand: {user_cards}, Final score: '{user_score}'")
    print(f"  Dealer's final hand: {dealer_cards}, Final_score: '{dealer_score}'")
    #We will compare their scores and give them the result by calling compare function and passing users and dealers score
    print(compare(user_score, dealer_score))

#ask the user again and again until they want to play
while input("Do you want to play BlackJack game? Type 'y' for yes or 'n' for no. ") =='y':
    #if they want to play again clear the screen and call the play_again function in which all the codes are written through 'Recursion' method.
    clear_screen()
    play_again()


