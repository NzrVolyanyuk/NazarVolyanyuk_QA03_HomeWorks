'''Задание 1
Доработайте игру «Guess my number», добавив следующие функции.
1. Улучшите игру так, чтобы после угадывания числа,выводился номер попытки,
которую сделал пользователь для угадывания магического числа.

!!!! мне кажется что это то же число что и пункте 1 !!!!!!
2. Улучшите игру так, чтобы после угадывания числа, выводилось количество потраченных попыток,
которые сделал пользователь для угадывания магического числа.

Задание 2
(Дополнительное, на высокую оценку)
Добавить возможность играть в игру заново. После того как пользователь угадает число,
отображается сообщение: «Вы хотите сыграть заново? ([Да] или [Нет])».
Если пользователь отвечает [Да], игра начинается заново,
если отвечает [Нет] – игра заканчивается.'''

#Guess my number
import random
game = True
while game:
    secret_number = 5
    # secret_number = random.randint(1,20)
    guess_number = 0
    lifes = 3
    attempt = 0
    while secret_number != guess_number and lifes > 0:
        guess_number = int(input("\nEnter number from 1 to 20: "))
        lifes = lifes - 1
        attempt = attempt + 1
        if lifes !=0:
            print(f"You have {lifes} lifes")
        if secret_number < guess_number:
            print("Your number greater ^^^ than secret")
        elif secret_number > guess_number:
            print("Your number less  than secret")
    if lifes >= 0:
        print(f"You WIN from {attempt} attempt")
        if input("If you want continue write Y, if you want finish the game write N: ") == "Y":
            game = True
        else:
            game = False
    else:
        print(f"you LOSE, the number that the bot guessed is {secret_number}")
        if input("If you want continue write Y, if you want finish the game write N: ") == "Y":
            game = True
        else:
            game = False
