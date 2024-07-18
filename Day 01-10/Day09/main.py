from art import logo
bids = {}
audition = True
highest_bid = 0

print(logo)
print('Welcome to my secret auction program.\n')


while audition:
    user_name = input("What is your name?:\n")
    bid_price = int(input("What's your bid?: $"))

    bids[user_name] = bid_price

    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if continue_bid == "no":
           
        for bidder in bids:
            if bids[bidder] > highest_bid:
                highest_bid = bid_price
                bid_winner = bidder
        audition = False 

print(f'The highest bidder is {bid_winner} at ${highest_bid} ')
