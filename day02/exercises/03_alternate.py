# Create a program for an ice cream parlor where the user can choose:
# Type of ice cream: cone (R$1.00), big cone (R$2.50), cup (R$4.00)
# Ice cream flavor: strawberry, vanilla, chocolate
# Topping: Caramel (R$1.50), strawberry (R$1.50), chocolate (R$1.50), no topping (R$0.00)

ice_cream_type = input("Choose the ice cream shell type - cone, big cone or cup: ")
ice_cream_flavor = input("Choose the ice cream flavor - strawberry, vanilla or chocolate: ")
ice_cream_topping = input("Choose the ice cream topping - caramel, strawberry, chocolate: ")

value = 0

# Ice cream type

if(ice_cream_type == "cone"):
    value += 1.00

elif ice_cream_type == "big cone":
    value += 2.50

elif ice_cream_type == "cup":
    value += 4.00

else:
    print("Please enter a valid option")


# Topping

if(ice_cream_topping in ["caramel", "strawberry", "chocolate"]):
    value += 1.50
    
elif ice_cream_topping == "":
    pass
    
else:
    print("Please enter a valid option")

print(f"The ice cream with {ice_cream_type}, {ice_cream_flavor} flavored and {ice_cream_topping} topping costs: R${value}")