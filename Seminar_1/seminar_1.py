# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# Примеры:

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# print('Введите число a');
# a = int(input())
# print('Введите число b');
# b = int(input())

# if a*a == b:
#     print(f"Число {b} является квадратом числа {a}")
# else:
#     print(f"Число {b} не является квадратом числа {a}")


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# print('Введите число a');
# a = int(input())
# print('Введите число b');
# b = int(input())
# print('Введите число c');
# c = int(input())
# print('Введите число d');
# d = int(input())
# print('Введите число e');
# e = int(input())

# ls = [a,b,c,d,e]
# max = ls[0]

# for i in ls:
#     if ls[i-1]>max: max=ls[i-1]

# print(f'Максимальное число {max}')


# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# Примеры:

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# print('Введите число N');
# n = int(input())

# if n < 0:
#     end = -n;
#     while(n<=end):
#         print(n, ' ', end='')
#         n += 1
# else:
#     st = -n;
#     while(st<=n):
#         print(st, ' ', end='')
#         st += 1


# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# print('Введите дробное число (дробная часть через точку)')
# a = float(input())

# a *= 10
# a %= 10

# if (a == 0):
#     print('Дробной части нет')
# else:
#     print(int(a))
