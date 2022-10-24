# 1.
# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def list_create():
    a = int(input("Введите длину списка: "))
    ls = []
    for i in range(0, a):
        ls.append(int(input(f"Введите значение {i} элемента: ")))
    return ls


new_ls = list_create()
print(new_ls)
sum = 0

for i in range(1, len(new_ls), 2):
    sum += new_ls[i]

print(f"Сумма элементов на нечётной позиции {sum}")

# 2.
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

ls = [2, 3, 4, 5, 6]
ls_2 = [2, 3, 5, 6]
ls_3 = [1]


def pair_mulitply(num_ls):
    if len(num_ls) > 1:
        res_ls = []
        for elem in range((len(num_ls)+1) // 2):
            res_ls.append(num_ls[elem] * num_ls[-elem - 1])
    else:
        res_ls = num_ls
    return res_ls


print(pair_mulitply(ls))
print(pair_mulitply(ls_2))
print(pair_mulitply(ls_3))

# 3.
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def float_list_create():
    a = int(input("Введите длину списка: "))
    new_ls = []
    for i in range(a):
        new_ls.append(float(input(f"Введите значение {i} элемента: ")))
    return new_ls


# new_list = [round(i % 1, 2) for i in ls if i % 1 != 0]
def point_value(float_ls):
    new_ls = []                 # данный код выполняет точно такую же функцию

    for elem in float_ls:
        num = elem - int(elem)
        new_ls.append(num)

    max = new_ls[0]
    min = new_ls[0]

    for elem in new_ls:
        if elem > max:
            max = elem
        elif elem < min:
            min = elem
    return max-min


ls = float_list_create()
print(ls)
print(
    f"Разница между максимальным и минимальным значением дробной части {point_value(ls)}")


# 4.
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_bin():
    x = 33
    a = int(input("Введите десятичное число: "))
    ls = []

    if a == 0:                      # проверка на ноль
        return 0

    while (a // 2 ** x == 0):       # нахождение подходящей степени двойки
        x -= 1

    while (x >= 0):                 # перевод из десятичной системы в двоичную
        if (a // 2 ** x == 1):
            ls.append(1)
            a -= 2 ** x
        else:
            ls.append(0)
        x -= 1

    return ls


print(f'Число в двоичной системе счисления: {decimal_to_bin()}')


numb = int(input('Введите целое число: '))
x = ''
while numb != 0:
    x += str(numb % 2)
    numb = numb // 2
print(f'Двоичное представление числа: {x}')


# 5.
# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.

#     Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1,
# 0, 1, 1, 2, 3, 5, 8, 13, 21]


def negpos_fibo():
    n = int(input("Введите число: "))
    pos_ls = [0, 1]
    neg_ls = []

    # Создание положительной последовательности
    for i in range(2, n+1):
        pos_ls.append(pos_ls[i-2] + pos_ls[i-1])

    for i in range(n+1):
        # Создание отрицательной последовательности
        neg_ls.insert(-i, (-1) ** (i+1) * pos_ls[i])

    # Объединение двух последовательностей
    neg_ls.extend(pos_ls)
    print(neg_ls)


negpos_fibo()
