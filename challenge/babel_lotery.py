# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

import random

def get_input():
    while True:
        try: number = int(input("enter a number: "))

        except ValueError as err:
                print("Invalid value")
                continue
        
        if 1 <= number <= 15:
            return number
        print("invalid valie, it must be between 1 and 15")


def check_numbers(sort, user_number):
    if sort == user_number:
        print("You won")
        return True
    elif user_number > sort:
        print("Too high, try lower")
        return False
    else:
         print("Too low, try higher")
         return False

sorted_number = random.randint(1,15)

