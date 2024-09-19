# Create a program that verifies if the user belongs to "Bald" family.

family_name = input("Tell me your family surname: ")

if family_name not in ["bald", "silva"]:
    print(f"You are not a {family_name} member")
else:
    print(f"You are a {family_name} member")