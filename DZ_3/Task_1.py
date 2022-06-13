# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#           стоящих на нечётной позиции.
#                                        Пример:
#                                        [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
ArrayPrimer = [2, 3, 5, 9, 3]
def SummmaNechetnix_Var1(a):
    print(f'{a} -> на нечётных позициях элементы ', end='')
    count = 0
    summa = 0
    shetI = 1
    for count in range(len(a)):
        if shetI < int(len(a)/2):
            if count % 2 == 1:
                print(f'{a[count]} и ', end='')
                summa += a[count]
                shetI += 1
        else:
            if count % 2 == 1:
                print(f'{a[count]}', end='')
                summa += a[count]
                shetI += 1
    print(f', ответ: {summa}')
    print('Большое СПАСИБО, что потратили своё время на проверку моего решения!')
def  SummmaNechetnix_Var2(a, summa: int = 0):
    print(f'{a} -> на нечётных позициях элементы ', end='')
    shetI = 1
    for i in range(1, len(a), 2):
        if shetI < int(len(a)/2):
            print (f'{a[i]} и ', end='')
            summa += a[i]
            shetI += 1    
        else:
            print (f'{a[i]}, ответ: ', end='')
            summa += a[i]
            shetI += 1
    print (summa)
    print('Большое СПАСИБО, что потратили своё время на проверку моего решения!')
    return summa
print('Здравствуйте! Для повышения удобства проверки задания, можете выбрать один из предложеных вариантов:')
print('1 вариант - Проверить решение задания на основании указанного списка в примере\n2 вариант - Проверить решение задания введя список чисел самостоятельно\nВведите цифру варианта и нажмите -Enter-\nИ так Ваш выбор?')
x = int(input('Вариант: '))
if x == 1:
    SummmaNechetnix_Var1(ArrayPrimer) # 1 способ
    # SummmaNechetnix_Var2(ArrayPrimer)   # 2 способ
if x == 2:
    ArrayVvod = input(
        'Введите Ваши данные элементов списка, через пробел\n').split(' ')
    ArrayVvod = list(map(int, ArrayVvod))
    SummmaNechetnix_Var1(ArrayVvod) # 1 способ
    # SummmaNechetnix_Var2(ArrayVvod) # 2 способ
if x < 1 or x > 2:
    print('К большому сожалению данной программой предусмотренного всего два варианта. Попробуйте снова!')
