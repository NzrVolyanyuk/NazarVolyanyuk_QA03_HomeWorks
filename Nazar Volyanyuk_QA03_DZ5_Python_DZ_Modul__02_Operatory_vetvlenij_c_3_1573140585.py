'''Задание 1
Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.
Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
Если число кратно 5 нужно вывести слово Buzz.
Если число кратно 3 и 5 нужно вывести Fizz Buzz.
Если число не кратно не 3 и 5 нужно вывести само число.
Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.'''

# number_user = int(input("Введите число в диапазоне от 1 до 100: "))
# if number_user > 0 and number_user <= 100:
#     if number_user % 3 == 0 and number_user % 5 == 0:
#         print("Fizz Buzz")
#     elif number_user % 3 == 0:
#         print("Fizz")
#     elif number_user % 5 == 0:
#         print("Buzz")
#     else:
#         print(number_user)
# else:
#     print("error")

'''Задание 2
Написать программу, которая по выбору пользователя возводит введенное им число в степень 
от нулевой до седьмой включительно.'''

# user_n = int(input("Введите число: "))
# user_st = int(input("Введите степень в которую возвести введенное Вами число (от 1 до 7): "))
#
# if user_st >= 0 and user_st < 8:
#     print(f"{user_n} в степени {user_st} = ", user_n**user_st)
# else:
#     print("Ошибка, диапазон возведения в степень от 0 до 7.")

'''Задание 3
Написать программу подсчета стоимости разговора для разных мобильных операторов. 
Пользователь вводит стоимость разговора и выбирает с какого на какой оператор он звонит. 
Вывести стоимость на экран.'''

# count_money = float(input("Введите стоимость разговора, грн/мин: "))
# operator_out = int(input("Введите от 1 до 3 с какого оператора будет совершен звонок, где: \n1 - Киевстар\n2 - Life\n3 - Vodafone\n"))
# operator_in = int(input("Введите от 1 до 3 на какой оператор будет совершен звонок, где: \n1 - Киевстар\n2 - Life\n3 - Vodafone\n"))
# if (operator_out == 1 and operator_in == 1) or (operator_out == 2 and operator_in == 2) or (operator_out == 3 and operator_in == 3):
#     print(f"стоимость 1 мин. разговора составляет", float(count_money) * 1, "грн/мин")
# elif (operator_out == 1 and operator_in <= 3) or (operator_out == 2 and operator_in <= 3) or (operator_out == 3 and operator_in <= 3):
#     print(f"стоимость 1 мин. разговора составляет", float(count_money) * 1.75, "грн/мин")
# else:
#     print("ощибка, введены некорректные данные")

'''Задание 4
Зарплата менеджера составляет 200$ + процент от продаж, 
продажи до 500$ — 3%, 
от 500 до 1000 — 5%, 
свыше 1000 — 8%. 
Пользователь вводит с клавиатуры уровень продаж для трех менеджеров. 
Определить их зарплату,
определить лучшего менеджера, начислить ему премию 200$, 
вывести итоги на экран.'''

manager1_sales = 1400
manager2_sales = 1800
manager3_sales = 1800

if manager1_sales > 0 and manager1_sales < 500:
    sales1_count = 200 + manager1_sales * 1.03
elif manager1_sales >= 500 and manager1_sales < 1000:
    sales1_count = 200 + manager1_sales * 1.05
elif manager1_sales > 1000:
    sales1_count = 200 + manager1_sales * 1.08
else:
    print("error")

if manager2_sales > 0 and manager2_sales < 500:
    sales2_count = 200 + manager2_sales * 1.03
elif manager2_sales >= 500 and manager2_sales < 1000:
    sales2_count = 200 + manager2_sales * 1.05
elif manager1_sales > 1000:
    sales2_count = 200 + manager2_sales * 1.08
else:
    print("error")

if manager3_sales > 0 and manager3_sales < 500:
    sales3_count = 200 + manager3_sales * 1.03
elif manager3_sales >= 500 and manager3_sales < 1000:
    sales3_count = 200 + manager3_sales * 1.05
elif manager3_sales > 1000:
    sales3_count = 200 + manager3_sales * 1.08
else:
    print("error")

if manager1_sales > manager2_sales and manager1_sales > manager3_sales:
    print(f"manager 1 best (+200$) = ", sales1_count + 200, "$\nmanager 2 = ", sales2_count, "$\nmanager 3 = ", sales3_count, "$")
elif manager2_sales > manager1_sales and manager2_sales > manager3_sales:
    print(f"manager 1 = ", sales1_count, "$\nmanager 2 best (+200$) = ", sales2_count + 200, "$\nmanager 3 = ", sales3_count, "$")
elif manager3_sales > manager1_sales and manager3_sales > manager2_sales:
    print(f"manager 1 = ", sales1_count, "$\nmanager 2 = ", sales2_count, "$\nmanager 3 best (+200$) = ", sales3_count + 200, "$")
else:
    print(f"manager 1 = ", sales1_count + 200, "$\nmanager 2 = ", sales2_count, "$\nmanager 3 = ", sales3_count, "$")