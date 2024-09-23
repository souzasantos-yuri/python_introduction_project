# Create a program that receives an indefinite number of values corresponding to "account balance." However, when the user presses "enter" without entering any value, the program stops receiving values and displays the sum of all previously entered values.

balance = 0
value = 0

while True:
    value = input("Tell me any values to put up in your bank account. When you are finished, just send a blank input: ")
    
    if value == "":
        break
    
    balance += float(value)

print(balance)