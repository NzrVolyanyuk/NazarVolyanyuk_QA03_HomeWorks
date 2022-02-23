'''Задание 1
Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
Bill Gates'''
def bill():
    print("\"Don\'t compare yourself with anyone in this world…\nif you do so, you are insulting yourself.\"\n"
          "\t\t\t\t\t\t\t\t\t\tBill Gates")
bill()

'''Задание 2
Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.'''
def num_chet(num1, num2):
    lst = []
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            lst.append(i)
    print(f"even numbers from {num1} - {num2} is\n",lst)
    return lst
num_chet(int(input("Enter num1: ")),int(input("Enter num2: ")))

'''Задание 3
Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция принимает в качестве 
параметров: длину стороны квадрата, символ и переменную логического типа:
■■ если она равна True, квадрат заполненный;
■■ если False, квадрат пустой.'''
def square_fun(length, type, symbol):
    space = " "
    height = length
    while length > 0:
        if type == 'True':
            for i in range(length):
                print(length * symbol)
            break
        if type == 'False':
            for i in range(length):
                if i == 0 or i == (height - 1):
                    print(length * symbol)
                else:
                    print(symbol + ((length - 2) * space) + symbol)
            break
square_fun(5, "True", "*")

'''Задание 4
Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров'''

'''var1'''
def max_num(a, b, c, d, e):
    if a >= b and a >= c and a >= d and a >= e:
        print(a)
    elif b >= a and b >= c and b >= d and b >= e:
        print(b)
    elif c >= a and c >= b and c >= d and c >= e:
        print(c)
    elif d >= a and d >= b and d >= c and d >= e:
        print(d)
    elif e >= a and e >= b and e >= c and e >= d:
        print(e)
a = 1
b = 2
c = 3
d = 4
e = 5
max_num(a, b, c, d, e)

'''var2'''
def max_num(list_num):
    max_number = max(list_num)
    print(max_number)
list_num = [10, 4, 8, 1, 2]
max_num(list_num)

'''Задание 5
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона передаются в 
качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 — нижняя граница), 
их нужно поменять местами.'''
def proizv_num(numb1, numb2):
    if numb1 == numb2:
        return "Диапазон введен неверно"
    if numb1 > numb2:
        numb1, numb2 = numb2, numb1
    proizv_num_final = 1
    for i in range(numb1, numb2 + 1):
        proizv_num_final = proizv_num_final * i
    return proizv_num_final
print(f'Произведение диапазона чисел = ', proizv_num(int(input("Введите число 1: ")), int(input("Введите число 2: "))))

'''Задание 6
Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра. Из функции нужно 
вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.'''
def count_f(some_number):
    count_numbers = 0
    for i in range(len(str(some_number))):
        count_numbers = count_numbers + 1
    return count_numbers
print("количество цифр в числе = ", count_f(int(input("Введите число: "))))

'''Задание 7
Напишите функцию, которая проверяет является ли число палиндромом. Число передаётся в качестве параметра. 
Если число палиндром нужно вернуть из функции true, иначе false. «Палиндром» — это число, у которого первая часть
цифр равна второй перевернутой части цифр. Например, 123321 — палиндром (первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром, а 421987 — не палиндром.'''

def palindrom_num_f(a):
    b = a
    if a == b[::-1]:
        return True
    else:
        return False
print(palindrom_num_f(str(input("Enter number: "))))