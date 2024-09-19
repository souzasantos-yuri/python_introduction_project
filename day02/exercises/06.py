# Create a program that checks if the item the person chose to buy from the store is on the list: orange, beer, instant noodles, charcoal, picanha.

market_list = ["orange", "beer", "noodles", "charcoal", "picanha"]

written_or_not = input("Give me any item to buy on market, see if I already have it on my list: ")

if written_or_not in market_list:
    print(f"{written_or_not} is already on the list")
else:
    print(f"{written_or_not} is not on the list")