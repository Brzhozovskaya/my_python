#if_random_game.py
import random
a = random.randint(1,4)
b = int(input("введите число от 1 до 4:\n"))
if a==b:
    print("Победа!\n")
elif a>b:
    print("результат больше введенного числа\n")
elif a<b:
    print("результат меньше введенного числа\n")
