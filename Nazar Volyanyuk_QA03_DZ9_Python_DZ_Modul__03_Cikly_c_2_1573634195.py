'''Задание 1
Пользователь вводит с клавиатуры два числа.
Нужно посчитать отдельно
сумму четных,
нечетных
и чисел,кратных 9 в указанном диапазоне,
а также среднеарифметическое каждой группы.'''

a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
summ_nech = 0
summ_chet = 0
krat9 = 0
count_summ_nech = 0
count_summ_chet = 0
count_krat9 = 0
for i in range(a,b + 1):
    if i % 2 == 0:
        summ_chet = summ_chet + i
        count_summ_chet = count_summ_chet + 1
    if i % 2 != 0:
        summ_nech = summ_nech + i
        count_summ_nech = count_summ_nech + 1
    if i % 9 == 0:
        krat9 = krat9 + i
        count_krat9 = count_krat9 + 1
print(f"сумма четных чисел в дипазоне {a}-{b} = ", summ_chet)
print(f"сумма нечетных чисел в дипазоне {a}-{b} = ", summ_nech)
print(f"сумма чисел, кратных 9 в дипазоне {a}-{b} = ", krat9)
print(f"среднеарифметическое группы четных чисел в дипазоне {a}-{b} = ", summ_chet/count_summ_chet)
print(f"среднеарифметическое группы нечетных чисел в дипазоне {a}-{b} = ", summ_nech/count_summ_nech)
print(f"среднеарифметическое чисел, кратных 9 в дипазоне {a}-{b} = ", krat9/count_krat9)

'''Задание 2
Пользователь вводит с клавиатуры длину линии и
символ для заполнения линии. Нужно отобразить на
экране вертикальную линию из введенного символа,
указанной длины.
Например, если было введено 5 и символ %, тогда
вывод на экран будет такой:
%
%
%
%
%'''

length = int(input('Введите длину линии: '))
symbol = str(input('Введите символ для линии: '))
for i in range(length):
    print(symbol)

'''Задание 3
Пользователь вводит с клавиатуры числа. 
Если число больше нуля нужно вывести надпись «Number is positive»,
если меньше нуля «Number is negative», 
если равно нулю «Number is equal to zero». 
Когда пользователь вводит число 7 программа прекращает свою работу и выводит
на экран надпись «Good bye!»'''

while True:
    x = int(input("\nEnter your number: "))
    if x == 7:
        print("Good bye!")
        break
    elif x > 0:
        print("Number is positive")
    elif x < 0:
        print("Number is negative")
    elif x == 0:
        print("Number is equal to zero")

'''Задание 4 
Пользователь вводит с клавиатуры числа. 
Программа должна подсчитывать сумму, максимум и минимум, введенных чисел. 
Когда пользователь вводит число 7 программа прекращает свою работу и 
выводит на экран надпись «Good bye!»'''

max_number = 0
summ_numbers = 0
user_number = int(input("Enter your number: "))
min_number = user_number
while user_number != 7:
    if user_number == 7:
        print("Good bye!")
    summ_numbers = summ_numbers + user_number
    if user_number > max_number:
        max_number = user_number
    if user_number < min_number:
        min_number = user_number
    user_number = int(input("Enter your number or 7 to stop and view results: "))
print(f"min number is {min_number},\nmax number is {max_number}, \nsumm of numbers is {summ_numbers}")