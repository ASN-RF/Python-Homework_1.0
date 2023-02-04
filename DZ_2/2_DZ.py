# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его
# цифр(отсекаем минус, считаем все в плюс).
# Пример:
# 67,82 -> 23
# 0,56 -> 11
# x = float(input(''))
# 1 вариант. Числа
# Chelay_chast = int(x)
# Drobnay_chast = x - Chelay_chast
# def cheloe (d):
#     rezult = 0
#     while d % 10 != 0:
#         rezult += d % 10
#         d //= 10
#     return rezult
# while (Drobnay_chast * 10)%10 != 0:
#     Drobnay_chast = round(Drobnay_chast,2)
#     Drobnay_chast *=10
# print (f'{x} -> {int(cheloe (Chelay_chast) + cheloe (Drobnay_chast))}')
# 2 вариант. Строки
# Stroka_1 = str(x)
# Stroka = Stroka_1.replace('.','')
# rezult = 0
# for i in Stroka:
#      rezult+= int(i)
# print (f'{Stroka_1} -> {rezult}')
# # 1 вариант "Строки"
# from posixpath import split
# a = str(input('Укажите Ваше любое вещественное число, хотя любое можете указать = '))
# if '.' in a:
#     z = a.replace('.', '')
# elif ',' in a:
#     z = a.replace(',', '')
# else:
#     z = a
# if '-' in z:
#     z = z.replace('-', '')
# b = list(z)
# sum = 0
# x = 0
# while x <= len(b)-1:
#     b[x] = int(b[x])
#     sum = sum + b[x]
#     x += 1
# print(f'{a} -> {sum}')

# 2 вариант "Числа"
# def Chisla(x):
#     m = x
#     if x<0:
#         x *=(-1)
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
#     print(f'{m} -> {int(U+I)}')
# your_number = float(input('Укажите Ваше любое вещественное число, хотя любое можете указать = '))
# Chisla(your_number)


# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел
# от 1 до N.
# Пример:
# Пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

def Opisanie (x):
    z = ','
    skobka='  ('
    for i in range(x):
        if i<1:
            print(skobka, end='')
        for j in range(1, i+2):
            print(j, end='')
        if i<x-1:
            print(z, end=' ')
        if i==x-1:
            print(')')
def Proizvedenie(a):
    Array = []
    count = 1
    sum = 1
    while count <= a:
        sum *= count
        Array.append(sum)
        count += 1
    print(Array, end="")    
N = int(input('Укажите Ваше любое целое положительное число = '))
if N<0:
    N *=(-1)
Proizvedenie(N)
Opisanie (N) 

# Задача 3. Реализуйте случайное перемешивания списка.
# Пример:
# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True']
# Результат -> [250, 3.14, 'True', 'Веселый пианист']
import random
Variant = int(input ('Здравствуйте! Если Вы хотите для проверки программы использовать пример из задания, то нажмите 1 и Enter, если сами ввести данные, то нажмите 2 и Enter:\n1 - Пример из задания\n2 - Ввести самому\nИтак, Ваше решение: '))
if Variant == 1:
    Primer = ['Веселый пианист', 250, 3.14, 'True']
    print(Primer, end="")
    print(' -> ', end="")
    random.shuffle(Primer)
    print(Primer)
elif Variant == 2:
    Vubor_Proveryushego = input('Введите Ваши данные элементов списка, через пробел\n').split(' ')
    print(Vubor_Proveryushego, end="")
    print(' -> ', end="")
    random.shuffle(Vubor_Proveryushego)
    print(Vubor_Proveryushego)