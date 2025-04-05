# empty dictionary to store the bidder
bidding = {}

# function to print questioning of the bidders
def new_bidder():
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bidding[name] = bid

# loop to keep checking if their are other bidders

keep_bidding = True

while keep_bidding:
    new_bidder()
    more_bidding = input("Are there other more bidders? ").lower()
    if more_bidding != "yes":
        keep_bidding = False
    print("\n"*20)

# variable to tell the winner of the auction
highest_bid = 0
winner =""

# for loop to get the highest bidder and bid
for key in bidding:
    if bidding[key] > highest_bid:
        highest_bid = bidding[key]
        winner = key


# printing of the results
print(f"The winner of the bid is {winner} with a bid of {highest_bid}")
