# Create a program that receives a number. Check if this number is prime or not, and return the result.

number = int(input("Enter the number: "))

if number > 1:
    for i in range (2, number):
        if(number % i) == 0:
            print(f"{number} is not prime")
            break
        else:
            print(f"{number} is prime")
            break
            
        