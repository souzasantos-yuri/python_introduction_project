# Create a program that calculates the square root and show the result

number = int(input("Enter the number to calculate the sqrt: "))
sqrt = (number ** 0.5)
sqrt = round(sqrt, 2)

print("Sqrt of", number, "is:", sqrt)