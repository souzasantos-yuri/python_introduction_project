# Create a program that sells a water bottle
# If the buyer chooses mineral water, charge R$ 1.50
# If the buyer chooses sparkling water, charge R$ 2.50
# Charge the buyer also by the number of bottles

choice = input("What type of water do you want? \nChoose between mineral or sparkling ")
quantity = int(input("How many bottles do you want? "))

if choice == "mineral" and quantity > 0:
    print("It will cost R$", (quantity * 1.50))
elif choice == "sparkling" and quantity > 0:
    print("It will cost R$", (quantity * 1.50))
else:
    print("Choose a valid option")