import math


def square(storona):
    storona = math.ceil(storona)
    return storona ** 2


user_input = input("Введите сторону квадрата: ").replace(',', '.')
user_input = float(user_input)
S = square(user_input)
print(f"Площадь квадрата со стороной {math.ceil(user_input)} равна: {S}")
