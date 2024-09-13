# Create a program that sells a water bottle
# If the buyer chooses mineral water, charge R$ 1.50
# If the buyer chooses sparkling water, charge R$ 2.50

choice = int(input("What type of water do you want? \nChoose between:[mineral/sparkling]"))

if choice == "mineral":
    print("It will cost R$ 1.50")
elif choice == "sparkling":
    print("It will cost R$ 2.50")
else:
    print("Choose a valid option")

