from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

   
bidding_dictionary = {}
def bidding_function():
    name = input("What is your name?: ")
    bid = int(input("What is your bid? :$"))
    bidding_dictionary[name] = bid


bidders_remaining = True
while bidders_remaining:
    bidding_function()
    bidders_remaining = input(
        "Are there are any other bidders? Type 'yes' or 'no'.\n")
    if bidders_remaining != "no":
        clear()
    else:
        bidders_remaining = False

print(bidding_dictionary)


def highest_bid_finder():
    highest_bid = 0
    highest_bidder_name = ""
    for name in bidding_dictionary:
        bid_value = bidding_dictionary[name]

        if bid_value > highest_bid:
            highest_bid = bid_value
            highest_bidder = name
    clear()
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


highest_bid_finder()
