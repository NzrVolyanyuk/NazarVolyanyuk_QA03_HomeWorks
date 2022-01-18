'''Задание 1
Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.
Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
Если число кратно 5 нужно вывести слово Buzz.
Если число кратно 3 и 5 нужно вывести Fizz Buzz.
Если число не кратно не 3 и 5 нужно вывести само число.
Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.'''

number_user = int(input("Введите число в диапазоне от 1 до 100: "))
if number_user > 0 and number_user <= 100:
    if number_user % 3 == 0 and number_user % 5 == 0:
        print("Fizz Buzz")
    elif number_user % 3 == 0:
        print("Fizz")
    elif number_user % 5 == 0:
        print("Buzz")
    else:
        print(number_user)
else:
    print("error")

'''Задание 2
Написать программу, которая по выбору пользователя возводит введенное им число в степень 
от нулевой до седьмой включительно.'''

user_n = int(input("Введите число: "))
user_st = int(input("Введите степень в которую возвести введенное Вами число (от 1 до 7): "))

if user_st >= 0 and user_st < 8:
    print(f"{user_n} в степени {user_st} = ", user_n**user_st)
else:
    print("Ошибка, диапазон возведения в степень от 0 до 7.")

'''Задание 3
Написать программу подсчета стоимости разговора для разных мобильных операторов. 
Пользователь вводит стоимость разговора и выбирает с какого на какой оператор он звонит. 
Вывести стоимость на экран.'''

count_money = float(input("Введите стоимость разговора, грн/мин: "))
operator_out = int(input("Введите от 1 до 3 с какого оператора будет совершен звонок, где: \n1 - Киевстар\n2 - Life\n3 - Vodafone\n"))
operator_in = int(input("Введите от 1 до 3 на какой оператор будет совершен звонок, где: \n1 - Киевстар\n2 - Life\n3 - Vodafone\n"))
if (operator_out == 1 and operator_in == 1) or (operator_out == 2 and operator_in == 2) or (operator_out == 3 and operator_in == 3):
    print(f"стоимость 1 мин. разговора составляет", float(count_money) * 1, "грн/мин")
elif (operator_out == 1 and operator_in <= 3) or (operator_out == 2 and operator_in <= 3) or (operator_out == 3 and operator_in <= 3):
    print(f"стоимость 1 мин. разговора составляет", float(count_money) * 1.75, "грн/мин")
else:
    print("ощибка, введены некорректные данные")
