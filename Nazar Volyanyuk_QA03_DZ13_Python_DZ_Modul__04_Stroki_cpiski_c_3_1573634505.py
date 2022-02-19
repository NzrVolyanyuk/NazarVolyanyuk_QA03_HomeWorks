'''Задание 1
Два списка целых заполняются случайными числами.
Необходимо:
■ Сформировать третий список, содержащий элементы
обоих списков;
■ Сформировать третий список, содержащий элементы
обоих списков без повторений;
■ Сформировать третий список, содержащий элементы
общие для двух списков;
■ Сформировать третий список, содержащий только
уникальные элементы каждого из списков;
■ +++ Сформировать третий список, содержащий только
минимальное и максимальное значение каждого из
списков.'''

from random import randrange

n = 50

some_numbers1 = [randrange(0, 50) for i in range(n)]
some_numbers2 = [randrange(0, 50) for i_1 in range(n)]

minimum1 = some_numbers1[0]
minimum1_index1 = 0
maximum1 = some_numbers1[0]
maximum1_index1 = 0

minimum2 = some_numbers2[0]
minimum2_index2 = 0
maximum2 = some_numbers2[0]
maximum2_index2 = 0

print(some_numbers1)
print(some_numbers2)

'''Сформировать третий список, содержащий элементы обоих списков'''
'''var 1'''
list_merge = some_numbers1 + some_numbers2
print(f"третий список, содержащий элементы обоих списков: {list_merge}")

'''var 2'''
list_3_merge = []
for i1 in range(len(some_numbers1)):
    list_3_merge.append(some_numbers1[i1])
for i2 in range(len(some_numbers2)):
    list_3_merge.append(some_numbers2[i2])
print(f"третий список, содержащий элементы обоих списков: {list_3_merge}")


'''Сформировать третий список, содержащий элементы обоих списков без повторений'''
list_3_non_repeat = list(set(some_numbers1 + some_numbers2))
print(f"третий список, содержащий элементы обоих списков без повторений: {list_3_non_repeat}")

'''Сформировать третий список, содержащий элементы общие для двух списков;'''
list_3_repeat = list(set(some_numbers1) & set(some_numbers2))
print(f"третий список, содержащий элементы общие для двух списков: {list_3_repeat}")


'''Сформировать третий список, содержащий только уникальные элементы каждого из списков'''
list_3_unique1 = list(set(some_numbers1))
list_3_unique2 = list(set(some_numbers2))
list_3_unique_all = list_3_unique1 + list_3_unique2
print(f"третий список, содержащий только уникальные элементы каждого из списков: {list_3_unique_all}")


'''Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков'''
for index in range(len(some_numbers1)):
    if minimum1 > some_numbers1[index]:
        minimum1 = some_numbers1[index]
        minimum_index1 = index
    if maximum1 < some_numbers1[index]:
        maximum1 = some_numbers1[index]
        maximum_index1 = index

for index in range(len(some_numbers2)):
    if minimum2 > some_numbers2[index]:
        minimum2 = some_numbers2[index]
        minimum_index2 = index
    if maximum2 < some_numbers2[index]:
        maximum2 = some_numbers2[index]
        maximum_index2 = index

list_min_max = [minimum1, maximum1, minimum2, maximum2]

print(f"{list_min_max[0]} - мин. число 1 списка,\n{list_min_max[2]} - мин. число 2 списка\n"
      f"{list_min_max[1]} - макс. число 1 списка\n{list_min_max[3]} - макс. число 2 списка")