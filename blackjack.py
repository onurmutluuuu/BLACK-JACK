def play_blackjack():
    import random
    import os
    
    
    default_money = 100
    player_money = ""
    index = 1
    
    def calculate_hand(hand):
        non_aces = [i for i in hand if i != 'A']
        aces = [i for i in hand if i == 'A']

        sum = 0

        for i in aces:
            if sum <= 10:
                sum += 11
            else:
                sum +=1

        for i in non_aces:
            if i in 'JQK':
                sum += 10
            else:
                sum += int(i)

        return sum


    while True:
        
        
        cards = [
            '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
            '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
            '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
            '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        ]
        
        random.shuffle(cards)

        player = []
        dealer = []

        dealer.append(cards.pop())
        player.append(cards.pop())
        dealer.append(cards.pop())
        player.append(cards.pop())

        first_hand = True
        standing = False
        
        
        while True:
            if index == 1:
                print ("Your Many = {}".format(default_money))
                player_question = float(input("How Much Money Do You Want to Play With: "))
                if player_question > default_money:
                    print("You Cann't Play for More Than Your Money")
                else:
                    player_money = default_money - player_question
                    break
                print()

            elif index > 1:
                print ("Your Many = {}".format(player_money))
                player_question = float(input("How Much Money Do You Want to Play With: "))
                if player_question > player_money:
                    print("You Cann't Play for More Than Your Money")
                else:
                    player_money = player_money - player_question
                    break
                print()


        while True:

            player_score = calculate_hand(player)
            dealer_score = calculate_hand(dealer)


            ##print("Player Cards {}".format(player))
            ##print("Player score {}".format(player_score))
            ##print("Dealer Cards {}".format(dealer))
            ##print("Dealer score {}".format(dealer_score))
            ##break
        ##break

            
            if standing:
                print("Dealer Cards: [{}] ({})".format(']['.join(dealer),dealer_score))
            else:
                print("Dealer Cards: [{}][?] ({})".format(dealer[0],dealer[0]))
            print("Player Cards: [{}] ({})".format(']['.join(player), player_score))
            print("")
            ##break
        #break


            if first_hand and player_score == 21:
                player_money = player_question * 2.5 + player_money
                print("Blackjack! Nice! Your New Money: {}".format(player_money))
                print('')
                break

            if standing:
                if dealer_score > 21:
                    player_money = player_question * 2 + player_money
                    print('Dealer busted, you win! Your New Money: {}'.format(player_money))
                elif player_score == dealer_score:
                    player_money = player_question * 2
                    print('Push, nobody wins. Your New Money: {}'.format(player_money))
                elif player_score > dealer_score:
                    player_money = player_question * 2 + player_money
                    print('You beat the dealer, you win! Your New Money: {}'.format(player_money))
                else:
                    print('You lose :( Your New Money: {}'.format(player_money))

                print("")
                break

            if player_score > 21:
                print('You busted! Your New Money: {}'.format(player_money))
                print('')
                break 


            print('What would you like to do')
            print(' [1] Hit')
            print(' [2] Stand')

            print("")
            choice = input("Your Choice: ")
            print()

            first_hand = False

            if choice == "1":
                player.append(cards.pop())
            elif choice == "2":
                standing = True
                while calculate_hand(dealer) < 16:
                    dealer.append(cards.pop())
                    
        if player_money == 0:
            print("Unfortunately You ran out of Money")
            break
            
            
        answer = input('Play again? Hit enter to continue OR Please, write "no" to quit ')
        if answer.lower() == "no":
            if player_money > 100:
                print()
                print(f"Your Earnings Today {player_money-default_money} Dollars")
            elif player_money < 100:
                print()
                print(f"Your Loss Today {default_money-player_money} Dollars")
            else:
                print()
                print(f"You Have no Loss or Earning")
            break
        else:
            index += 1
            continue
        pass
    
if __name__ == "__main__":
    play_blackjack()