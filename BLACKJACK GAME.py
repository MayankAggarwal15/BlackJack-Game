# CAPSTONE PROJECT ON BLACKJACK GAME

import random
import os


def compare_scores(money):

    if p_blackjack == 1 and d_blackjack != 1:
        print("\nNATURAL! You scored 21 in first 2 cards 😎")
        print(f"YOU WIN $ {2.5*bet}")
        money += 2.5*bet

    elif d_blackjack == 1 and p_blackjack != 1:
        print("\nNATURAL! Dealer scored 21 in first 2 cards 😱")
        print(f"BUST! YOU LOSE $ {bet}")

    elif dealer_score == player_scores:
        print("\nBoth have equal score 🙃")
        print("DRAW!(PUSH!)(STAND-OFF!)")
        money += bet

    elif player_scores > 21:
        print("\nYour score are greater than 21 😭")
        print(f"BUST! YOU LOSE $ {bet}")

    elif dealer_score > 21:
        print("\nDealer's score are greater than 21 😁")
        print(f"YOU WIN $ {2*bet}")
        money += 2*bet

    elif dealer_score > player_scores:
        print("\nYour score are less than Dealer's score 😤")
        print(f"BUST! YOU LOSE $ {bet}")

    elif dealer_score < player_scores:
        print("\nYour score are greater than Dealer's score 😃")
        print(f"YOU WIN $ {2*bet}")
        money += 2*bet

    return money


def calculate_score(cards):

    """Take a list of cards and return the score calculated from the cards"""

    duplicate = cards.copy()
    counts = duplicate.count("Ace")

    score = 0

    for i in range(counts):
        if "Ace" in duplicate:
            duplicate.remove("Ace")
            duplicate.append("Ace")

    for item in duplicate:
        if item == "Jack" or item == "Queen" or item == "King":
            score += 10
        elif item == "Ace":
            if score < 11:
                score += 11
            else:
                score += 1
        else:
            score += item

    return score


def hit_button():

    player_cards.append(random.choice(cards))
    player_scores = calculate_score(player_cards)

    print("\nAFTER HIT :-")
    print(f"Your Cards are : {player_cards}")
    print(f"Your Score is : {player_scores}")

    return player_scores


def stand_button(money):

    d_blackjack = 0

    dealer_cards.append(random.choice(cards))
    dealer_score = calculate_score(dealer_cards)

    print(f"\nDealer's Cards are : {dealer_cards}")
    print(f"Dealer's Score is : {dealer_score}")

    if dealer_score == 21:
        print("\nDealer has BLACKJACK 😱")
        d_blackjack = 1

        if insurance == "yes":
            print(f"\nYou WON the Insurance Amount : $ {bet}")
            money += bet
            print(f"\nAfter winning Side Bet, you have $ {money}")
    else:
        if insurance == "yes":
            print(
                f"\nNo BLACKJACK \nYou LOST the Insurance Amount : $ {0.5*bet}")

    if player_scores <= 21:
        while dealer_score < 17:
            dealer_cards.append(random.choice(cards))
            dealer_score = calculate_score(dealer_cards)

        if "Ace" in dealer_cards and dealer_score == 17 and dealer_score < player_scores:
            dealer_cards.append(random.choice(cards))
            dealer_score = calculate_score(dealer_cards)

    if len(dealer_cards) > 2:
        print("\nAFTER HIT :-")
        print(f"Dealer's Cards are : {dealer_cards}")
        print(f"Dealer's Score is : {dealer_score}")

    return dealer_score, d_blackjack, money


def double_button(bet, money):

    print(f"\nNow Bet Amount is : $ {2*bet}")
    print(f"\nAfter Doubling Betting Amount,  you have $ {money-bet} left")

    player_scores = hit_button()
    dealer_score, d_blackjack, money = stand_button(money)

    money -= bet
    bet = 2*bet

    return player_scores, dealer_score, bet, money, d_blackjack


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

print('\n\nWELCOME TO "BLACKJACK GAME" ("21" GAME )\n')

again = False
money = 1000


while not again:

    count = 0

    print(f"\nYou have $ {money} for Betting in Game")

    bet = int(input("\nEnter the Betting Amount : $ "))

    if bet > money:
        print("\nINVALID INPUT! You don't have enough money for Betting in Game.")
        break
    elif bet <= 0:
        print("\nINVALID INPUT!")
        break

    money -= bet

    print(f"\nAfter betting $ {bet} , you have $ {money} left")

    start = input('\nType "Deal" to start the game.\n').title()

    if start != "Deal":
        print("\nINVALID INPUT!")
        break

    cards = [i for i in range(2, 11)]
    cards += ["Jack", "Queen", "King", "Ace"]

    random.shuffle(cards)

    player_cards = [random.choice(cards), random.choice(cards)]
    player_scores = calculate_score(player_cards)

    dealer_cards = [random.choice(cards)]
    dealer_score = calculate_score(dealer_cards)

    print(f"\nYour Cards are : {player_cards}")
    print(f"Your current score is : {player_scores}")

    p_blackjack = 0

    if player_scores == 21:
        print("\nYou have BLACKJACK 😎")
        p_blackjack = 1

    print(f"\nDealer's First Cards is : {dealer_cards[0]}")
    print(f"Dealer's current score is : {dealer_score}")

    if "Ace" in dealer_cards:
        print("\nDo you want INSURANCE (Side Bet)?")
        print(f"Insurance Amount : {0.5*bet}")

        insurance = input(
            "\nType 'yes' to take Insurance , otherwise type 'no'.\n").lower()

    else:
        insurance = "no"

    if insurance == "yes":
        if money < 0.5*bet:
            print("\nSORRY! You don't have that enough money to take insurance.")
            insurance == "no"
        else:
            money -= 0.5*bet
            print(f"\nAfter taking Insurance , you have $ {money} left.")

    end = False
    flag = 0

    while not end:

        invalid = 0

        if player_scores < 21:

            print("\nWhat do you want to do?")
            print('1. Type "HIT" to get another card')
            print(
                '''2. Type "STAND" to pass the turn to dealer and reveal dealer's another card''')

            if flag == 0:
                print(
                    '3. Type "DOUBLE" to double the bet and get another card and pass the turn to dealer')

            choice = input("\nType your choice : ").title()

            if choice == "Hit":
                player_scores = hit_button()
                flag = 1

            elif choice == "Stand":
                dealer_score, d_blackjack, money = stand_button(money)
                end = True

            elif choice == "Double" and flag == 0 and money >= bet:
                player_scores, dealer_score, bet, money, d_blackjack = double_button(
                    bet, money)
                end = True

            else:
                if money < bet:
                    print(
                        "\nINVALID INPUT! You don't have enough money for Doubling Bet.")
                    money += bet
                else:
                    print("\nINVALID INPUT!")

                end = True
                invalid = 1

        elif player_scores >= 21:
            dealer_score, d_blackjack, money = stand_button(money)
            end = True

        else:
            end = True

    if invalid == 0:

        print(f"\nYour Final Hand is : {player_cards}")
        print(f"Your Final Score is : {player_scores}")

        print(f"\nDealer's Final Hand is : {dealer_cards}")
        print(f"Dealer's Final Score is : {dealer_score}")

        money = compare_scores(money)

        print(f"\nNow You have $ {money}")

        if money == 0:
            break

    print("\nDo you want to Bet Again or Exit from the Game")

    continues = input(
        "Type 'yes' if you want to Bet Again or Type 'no' to Exit from Game.\n").lower()

    if continues == "yes":
        if money == 0:
            print("\nSORRY , You don't have enough money to Bet again")
            again = True
        else:
            os.system("cls")

    elif continues == "no":
        again = True
    else:
        print("\nINVALID INPUT!")
        again = True


print(f"\nYour Total Money is : $ {money}")
