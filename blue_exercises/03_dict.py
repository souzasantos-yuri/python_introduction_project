# Create a program for an ice cream parlor where the user can choose:
# Type of ice cream: cone (R$1.00), big cone (R$2.50), cup (R$4.00)
# Ice cream flavor: strawberry, vanilla, chocolate
# Topping: Caramel (R$1.50), strawberry (R$1.50), chocolate (R$1.50), no topping (R$0.00)

ice_cream_type = input("Choose the ice cream shell type - cone, big cone or cup: ").lower()
ice_cream_flavor = input("Choose the ice cream flavor - strawberry, vanilla or chocolate: ").lower()
ice_cream_topping = input("Choose the ice cream topping - caramel, strawberry, chocolate: ").lower()

value = 0

# Ice cream type

ice_cream = {
    "cone": 1.00,
    "big cone": 2.5,
    "cup": 4.00
}


if ice_cream_type in ice_cream:
    value += ice_cream[ice_cream_type]
else:
    print("Enter a valid option")


# Topping

topping = {
    "caramel": 1.50,
    "strawberry": 1.50,
    "chocolate": 1.50,
    "": 0
}

if ice_cream_topping in topping:
    value += topping[ice_cream_topping]
else:
    print("Enter a valid option")
    

print(f"The ice cream with {ice_cream_type}, {ice_cream_flavor} flavored and {ice_cream_topping} topping costs: R${value}")