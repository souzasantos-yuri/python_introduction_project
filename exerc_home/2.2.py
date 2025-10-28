# Create a program that receives a number. Check if the entered number is even or odd. Display the result in the following way:
# Number X is even
# Number X is odd

number = int(input("Give me a number! "))

print(f"{number} is Even" if number % 2 == 0 else f"{number} is Odd")