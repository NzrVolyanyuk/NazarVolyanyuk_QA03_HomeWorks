'''Задание 1:
Пользователь вводит с клавиатуры арифметическое
выражение. Например, 23+12.
Необходимо вывести на экран результат выражения.
В нашем примере это 35. Арифметическое выражение
может состоять только из трёх частей: число, операция,
число. Возможные операции: +, -,*,/'''

# user_input = '23+12'
# numbers_1 = []
# numbers_2 = ""
# symbols = ["+", "-", "*", "/"]
# for i in user_input:
#     numbers_1.append(i)
#     print(numbers_1)
#     for symb in user_input:
#         if symb == symbols:
#             symb = symbols

operations = ["+", "-", "*", "/"]
text = "25+36"
text = text.replace(" ", "")
# print(text)


for i in range(len(text)):
    a = text[i]
    if a in operations:
        l = text[:i]  # left number
        r = text[i + 1:]  # right number
        operation = a
print(l, r)
if (l.isnumeric() == True) and (r.isnumeric() == True):
    l = int(l)
    r = int(r)
    if operation == "+":
        print(f"{l} + {r} = {l+r}")
    elif operation == "-":
        print(f"{l} - {r} = {l-r}")
    elif operation == "*":
        print(f"{l} * {r} = {l*r}")
    elif operation == "/":
        if r != 0:
            print(f"{l} / {r} = {l/r}")
        else:
            print("No division by zero!")
else:
    print("Incorrect input!")




# number = '0123456789'
# spe = '!?,.'
# s = 'some interesting, text and else! what i am doing. how do you do? i am fine! thank you.'
# count_number = 0
# count_symbol = 0
# count_spe = 0
# count_spea = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#
#     if a in number:
#         count_number = count_number + 1
#     if a in spe:
#         count_spe = count_spe + 1
#     if a == spe[0]:
#         count_spea = count_spea + 1
# print(count_symbol, count_number, count_spe,count_spea)



# Пользователь вводит с клавиатуры строку. Посчитайте количество букв,
# цифр в строке. Выведите оба
# количества на экран.'''
# #V1
# letters = 'abcdefghijklmnopqrstuvwxyz'
# numbers = '0123456789'
# s = 'hello123'
# count_numbers = 0
# count_letters = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     for l in range(len(letters)):
#         if a == letters[l]:
#             count_letters = count_letters + 1
#     for n in range(len(numbers)):
#         if a == numbers[n]:
#             count_numbers = count_numbers + 1
# print(count_numbers,count_letters)


# number = '9'
# print(number.isnumeric())
# print(number.isalpha())
# #GDPR
#
# #V2
# s = 'hello123'
# count_numbers = 0
# count_letters = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     if a.isalpha():
#         count_letters = count_letters + 1
#     if a.isnumeric():
#         count_numbers = count_numbers + 1
# print(count_numbers,count_letters)