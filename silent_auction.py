# Silent Auction

from art import logo

print(logo)
print('Welcome to the secret auction program')

auctioneers = {}

bids_complete = False

while bids_complete == False:
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $"))
    auctioneers[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if other_bidders == 'no':
        bids_complete = True

name_of_winner = max(auctioneers, key = auctioneers.get)
max_bid = auctioneers[name_of_winner]
    
print(f"The winner is {name_of_winner} with a bid of ${max_bid}.")


