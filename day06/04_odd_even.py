def odd_number(number:int):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"

number = input("Enter a number: ")
number = int(number)

result = odd_number(number)

print(f"The value {number} is {result}")
