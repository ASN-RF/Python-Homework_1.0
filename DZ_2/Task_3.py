# Задача 3. Реализуйте случайное перемешивания списка.
# Пример:
# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True'] Результат -> [250, 3.14, 'True', 'Веселый пианист']
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
