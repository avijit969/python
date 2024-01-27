import os

bidders = {}


def find_winner(bidders_details):
    max_price = 0
    winner = ""
    for bidder in bidders_details:
        if max_price < bidders_details[bidder]:
            max_price = bidders_details[bidder]
            winner = bidder
    print(f"Winner is {winner} 🥇🥇 with bidding price {max_price}")


flag = False
while not flag:
    name = input("Enter your name:\n")
    price = int(input("Enter your bidding price:\n"))
    bidders[name] = price
    more_bidders = input("Are there any more bidder type 'yes' or 'no' :\n")
    if more_bidders == 'no':
        flag = True
        find_winner(bidders)
    elif more_bidders == 'yes':
        os.system('cls')
