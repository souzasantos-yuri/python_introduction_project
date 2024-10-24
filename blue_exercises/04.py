# Create a program that verifies if the user belongs to "Bald" family.

family_name = input("Tell me your family surname: ")
family_name.lower()

if family_name in "bald":
    print("You are a Bald member")
else:
    print("You are not a Bald member")