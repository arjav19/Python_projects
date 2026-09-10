print('Welcome to Blind Auction')
bids = {}
is_game_finished = False

def compare(bidding_record):
    highest_bidder = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of {highest_bidder}.")

while not is_game_finished:
    name = input("Enter your name:")
    bidding_amount = int(input("Enter your bidding amount: "))
    bids[name] = bidding_amount

    should_continue = input("Are there any other bidders? Type 'yes' or 'no':")
    if should_continue == "no":
        is_game_finished = True
        compare(bids)
    elif should_continue == "yes":
        print ("Countinue Bidding")    
