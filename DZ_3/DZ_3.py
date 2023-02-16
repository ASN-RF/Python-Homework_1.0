# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# def poisk_nechet(x):
#     elementi = []
#     sum = 0
#     for i in range(len(x)):
#         if i % 2 != 0:
#             elementi.append(x[i])
#             sum += x[i]
#     return sum
# Spisok = [int(input(f'Введите {i+1} число: ')) for i in range (int(input('Введите длину списка: ')))]
# print(f'{Spisok} -> {poisk_nechet(Spisok)}')
# ------ 2 вариант --------------------
# def sum_of_odd_elems(lst, sum_el: int = 0):
#     for item in range(1, len(lst), 2):
#         sum_el += lst[item]
#     return sum_el

# --------------- КОНЕЦ 1 ЗАДАЧИ -----------------------------

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и
# последний элемент, второй и предпоследний и т.д. Если остается 1 элемент без пары - умножаем его самого на
# себя.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# Spisok_1 = [2, 3, 4, 5, 6]
# Spisok_2 = [2, 3, 5, 6]
# def proizved_par (x):
#     Spisol_rezult = []
#     if len(x)%2 != 0:
#         for i in range(len(x)//2+1):
#             Spisol_rezult.append(x[i]*x[len(x)-1-i])
#     else:
#         for i in range(len(x)//2):
#             Spisol_rezult.append(x[i]*x[len(x)-1-i])
#     return Spisol_rezult
# print(f'{Spisok_1} => {proizved_par (Spisok_1)}')
# print(f'{Spisok_2} => {proizved_par (Spisok_2)}')

# --------------- КОНЕЦ 2 ЗАДАЧИ -----------------------------
# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
Spisok = [1.1, 1.2, 3.1, 5, 10.01]
Spisok_rez = []
for i in Spisok:
    Spisok_rez.append(i-i//1)
print(f'{Spisok} => {round(max (Spisok_rez) - min(Spisok_rez), 3)}')
