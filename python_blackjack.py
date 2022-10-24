import random

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", ]
money = 100
bet = 0
minimum_bet = 10
dealer_soft = 17

def new_card(hand, hand_int):
    rand_card = random.choice(cards)
    hand.append(rand_card)

    if rand_card == "J" or rand_card == "Q" or rand_card == "K":
        hand_int.append(10)
    elif rand_card == "A":
        hand_int.append(11)
    else:
        hand_int.append(rand_card)
    return hand, hand_int

def list_conversion(hand):
    return ", ".join(str(item) for item in hand)

def sum_function(hand):
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


print("\nWelcome to Edmond's Python Blackjack Game!")

while money > 0 and bet != "q" and money >= minimum_bet:
    bet = input(f"----------------------------------------------\nYou have ${money}. The minimum bet is ${minimum_bet}. Please enter a bet or type 'q' to quit: ")
    if bet == "q":
        print("Thank You For Playing Edmond's Python Blackjack Game!\n")
        break
    else:
        try:
            bet = int(bet)
            first_hand = True

            if bet > money:
                print("Sorry, insufficient funds.")

            elif bet < minimum_bet:
                print(f"Sorry, the minimum bet is ${minimum_bet}.")

            else:
                player = []
                player_int = []
                dealer = []
                dealer_int = []
                decision = ""

                new_card(player, player_int)
                new_card(player, player_int)

                print("\nPLAYER'S HAND:")

                while sum_function(player_int) < 21:
                    if first_hand == True and money >= bet*2:
                        decision = input(f"\nYour cards are {list_conversion(player)}.\nThe total is {sum_function(player_int)}.\nDo you want to hit (h), stay (s), or double (d)? ")
                    else:
                        decision = input(f"\nYour cards are {list_conversion(player)}.\nThe total is {sum_function(player_int)}.\nDo you want to hit (h) or stay (s)? ")

                    if decision == "h":
                        new_card(player, player_int)
                        first_hand = False
                    elif decision == "d" and first_hand == True and money >= bet*2:
                        bet *= 2
                        new_card(player, player_int)
                        break
                    elif decision == "s":
                        first_hand = False
                        break
                    else:
                        print("Sorry, invalid decision.")

                if sum_function(player_int) == 21:
                    print(f"Your cards are {list_conversion(player)}. \nThe total is 21, a blackjack!")

                elif sum_function(player_int) > 21:
                    print(f"Your cards are {list_conversion(player)}.\nThe total is {sum_function(player_int)}.\nPlayer busted!")
                else:
                    print(f"Your total is {sum_function(player_int)}.")


                print("\nDEALER'S HAND:")
                new_card(dealer, dealer_int)
                new_card(dealer, dealer_int)

                while sum_function(dealer_int) < dealer_soft:
                    new_card(dealer, dealer_int)

                print(f"The dealer's cards are {list_conversion(dealer)}.\nDealer's total is {sum_function(dealer_int)}.")
                if sum_function(dealer_int) == 21:
                    print(f"Dealer blackjack!")

                if sum_function(dealer_int) > 21:
                    print(f"Dealer busted!")

                if sum_function(player_int) > sum_function(dealer_int):
                    if sum_function(player_int) <= 21:
                        print("Congrats, you won!")
                        money += bet
                    elif sum_function(player_int) > 21 and sum_function(dealer_int) <= 21:
                        print("Sorry, you lose.")
                        money -= bet
                    else:
                        print("Push.")

                elif sum_function(dealer_int) > sum_function(player_int):
                    if sum_function(dealer_int) <= 21:
                        print("Sorry, you lose")
                        money -= bet
                    elif sum_function(dealer_int) > 21 and sum_function(player_int) <= 21:
                        print("Congrats, you won!")
                        money += bet
                    else:
                        print("Push")

                else:
                    print("Push")

        except:
            print("Sorry, invalid bet")


print("\nSorry, you have don't have enough money to play. Game over.\nThank You For Playing Edmond's Python Blackjack Game!\n")