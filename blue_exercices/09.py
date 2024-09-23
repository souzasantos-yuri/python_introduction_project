# Create a program that receives an indefinite number of values corresponding to "account balance." However, when the user presses "enter" without entering any value, the program stops receiving values and displays the sum of all previously entered values.

balance = 0
value = 0

while(value != ""):
    balance += int(value)
    value = input("Tell me any values to put up in your bank account. When you are finished, just send a blank input: ")

print(balance)