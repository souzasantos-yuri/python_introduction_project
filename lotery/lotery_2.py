lucky_number = 7

for i in range(3):

    while True:

        try:
            number = int(input("Enter a number between 1 and 15"))
            break
        except ValueError:
            print("Please only numbers!")

    if number == lucky_number:
        print("Congrats, you got it right")
        break
    elif number > lucky_number:
        print("Thats unfortunate, try a lower number")
    else:
        print("Thats unfortunate, try a higher number")
