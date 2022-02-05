'''Задание 1
Напишите программу, которая запрашивает два
целых числа x и y,
после чего вычисляет и выводит значение x в степени y.'''
play = True
while play:
    x = int(input("\nВведите число: "))
    y = int(input("Введите число для возведения в степень: "))
    if x != 0 and y != 0:
        print(f"Число {x} в степени {y} = ", x ** y)
    else:
        print("Ошибка, введены некорректные данные")
    play = bool(input("Нажмите любую клавишу для продолжения, \nдля завершения игры нажмите клавишу [Enter]"))


'''Задание 2
Подсчитать количество целых чисел в диапазоне от
100 до 999 у которых есть две одинаковые цифры.'''
a = 100
b = 999
count = 0
for i in range(a, b + 1):
    num = str(i)
    num1 = int(num[0])
    num2 = int(num[1])
    num3 = int(num[2])
    if num1 == num2 or num2 == num3 or num1 == num3:
        count = count + 1
print(f"количество целых чисел в диапазоне от {a} до {b} у которых есть две одинаковые цифры = ", count)

'''Задание 3
Подсчитать количество целых чисел в диапазоне от
100 до 9999 у которых все цифры разные.'''
a = 100
b = 9999
count = 0
for i in range(a, b + 1):
    num = str(i)
    num1 = int(num[0])
    num2 = int(num[1])
    num3 = int(num[2])
    if i // 1000 > 0:
        num4 = int(num[3])
    else:
        num4 = 99
    if num1 != num2 and num2 != num3 and num3 != num4 and num1 != num3 and num1 != num4 and num2 != num4:
        count = count + 1
print(f"количество целых чисел в диапазоне от {a} до {b} у которых все цифры разные= ", count)

'''Задание 4
Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все 
цифры 3 и 6 и вывести обратно на экран.'''

'''1 вариант'''
play_task4 = True
while play_task4:
    some_num = input('Введите целое число: ')
    for i in range(len(some_num)):
        if some_num[i] == "3" or some_num[i] == "6":
            continue
        else:
            print(some_num[i], end='')
    print()
    play_task4 = bool(input("Нажмите любую клавишу для продолжения, \nдля завершения игры нажмите клавишу [Enter]"))

'''2 вариант'''
play_task4 = True
while play_task4:
    some_num = input('Введите целое число: ')
    for i in range(len(some_num)):
        if some_num[i] == "3" or some_num[i] == "6":
            some_num == ""
        else:
            print(some_num[i], end='')
    print()
    play_task4 = bool(input("Нажмите любую клавишу для продолжения, \nдля завершения игры нажмите клавишу [Enter]"))

'''3 вариант'''
play_task4 = True
while play_task4:
    some_num = input('Введите целое число: ')
    for i in range(len(some_num)):
        if some_num[i] == "3" or some_num[i] == "6":
            del i
        else:
            print(some_num[i], end='')
    print()
    play_task4 = bool(input("Нажмите любую клавишу для продолжения, \nдля завершения игры нажмите клавишу [Enter]"))