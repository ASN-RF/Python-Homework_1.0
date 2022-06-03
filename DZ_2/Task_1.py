# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его
#           цифр(отсекаем минус, считаем все в плюс).
# Пример:
# 67,82 -> 23
# 0,56 -> 11
# 1 вариант "Строки"
from posixpath import split
a = str(input('Укажите Ваше любое вещественное число, хотя любое можете указать = '))
if '.' in a:
    z = a.replace('.', '')
elif ',' in a:
    z = a.replace(',', '')
else:
    z = a
if '-' in z:
    z = z.replace('-', '')
b = list(z)
sum = 0
x = 0
while x <= len(b)-1:
    b[x] = int(b[x])
    sum = sum + b[x]
    x += 1
print(f'{a} -> {sum}')
# 2 вариант "Числа"
# def Chisla(x):
#     a = x//1
#     b = round((x-a), 5)
#     U = 0.0
#     if a > 0:
#         while a/10 > 1:
#             a /= 10
#             q = round((a - (a//1)), 5)
#             U = U + round((a-q), 5)
#             a = q*10
#         else:
#             U += a
#     else:
#         U += a
#     if b > 0:
#         I = 0.0
#         while b > 0:
#             b *= 10
#             I = I + (b//1)
#             b = round(b - (b//1), 5)
#     print(f'{x} -> {int(U+I)}')
# your_number = float(input('Укажите Ваше любое вещественное число, хотя любое можете указать = '))
# Chisla(your_number)
