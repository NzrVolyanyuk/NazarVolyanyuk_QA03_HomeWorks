'''Задание 1:
Пользователь вводит с клавиатуры арифметическое
выражение. Например, 23+12.
Необходимо вывести на экран результат выражения.
В нашем примере это 35. Арифметическое выражение
может состоять только из трёх частей: число, операция,
число. Возможные операции: +, -,*,/'''

user_text = str(input("Введите арифметическое выражение, например 23+12. Допустимые операции + - * / : "))
symbols = ["+", "-", "*", "/"]
for i in range(len(user_text)):
    a = user_text[i]
    if a in symbols:
        left_number = user_text[:i]
        right_number = user_text[i + 1:]
        symbols = a
if (left_number.isnumeric() == True) and (right_number.isnumeric() == True):
    left_number = int(left_number)
    right_number = int(right_number)
    if symbols == "+":
        print(f"{left_number} + {right_number} = {left_number+right_number}")
    elif symbols == "-":
        print(f"{left_number} - {right_number} = {left_number-right_number}")
    elif symbols == "*":
        print(f"{left_number} * {right_number} = {left_number*right_number}")
    elif symbols == "/":
        print(f"{left_number} / {right_number} = {left_number/right_number}")
else:
    print("Ошибка!")

'''Задание 2:
В списке целых, заполненном случайными числами,
определить минимальный и максимальный элементы,
посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
количество нулей. Результаты вывести на экран.'''

from random import randrange
n = 30
some_numbers = [randrange(-100, 100) for i in range(n)]
count_zero = 0
count_pozitive = 0
count_negative = 0
minimum = some_numbers[0]
minimum_index = 0
maximum = some_numbers[0]
maximum_index = 0
for i in some_numbers:
    if i == 0:
        count_zero = count_zero + 1
    if i >= 0:
        count_pozitive = count_pozitive + 1
    if i < 0:
        count_negative = count_negative + 1
    for index in range(len(some_numbers)):
        if minimum > some_numbers[index]:
            minimum = some_numbers[index]
            minimum_index = index
        if maximum < some_numbers[index]:
            maximum = some_numbers[index]
            maximum_index = index
print(f"Список случайных цифр: {some_numbers}")
print(f"минимальное {minimum} \nмаксимальное {maximum} \nк-ство отрицательных {count_negative} "
      f"\nк-ство положительных {count_pozitive} \nк-ство нулей {count_zero}")
