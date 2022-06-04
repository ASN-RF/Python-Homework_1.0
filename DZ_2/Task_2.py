# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#                         Пример:
#                         пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)
def Opisanie (x):
    z = ','
    skobka='  ('
    for i in range(x):
        if i<1:
            print(skobka, end='' , flush=True)
        for j in range(1, i+2):
            print(j, end='' , flush=True)
        if i<x-1:
            print(z, end=' ' , flush=True)
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
    print(Array, end="", flush=True)    
N = int(input('Укажите Ваше любое целое положительное число = '))
if N<0:
    N *=(-1)
Proizvedenie(N)
Opisanie (N)    
