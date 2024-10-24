#Create a program that receives a person's name and age.
#If the person is under 18 years old, display the message: 'Fulano, you cannot drive or drink.'
#For people between 18 and 65 years old, display the message: 'Fulano, drinking is allowed! Just don’t drive!'
#For people over 65 years old, display the message: 'Fulano, drink with great moderation!'

name = input("Give me your name: ")
age = int(input("Give me your age: "))

if age <= 18:
    print(f"{name}, you cannot drive or drink")
elif age >= 18 and age <= 65:
    print(f"{name}, drinking is allowed! Just dont drive!")
else:
    print(f"{name}, drink with moderation!")