# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее
# и меньшее число. В качестве символа-разделителя используйте пробел.

i = '1 2 3 4 5 5  6'
result = list(map(int, (i.split())))
print(max(result), min(result))

# вариант 2
nums = '2 54 6  7 8  89 56 5 3'
my_list = [int(elem) for elem in nums.split()]
print(min(my_list), max(my_list))

# 2. Найти корни квадратного уравнения двумя способами. С помощью стандартных средств и
# с помощью внешних библиотек


def square_root():
    a = float(input())
    b = float(input())
    c = float(input())
    x1 = 0
    x2 = 0

    D = (b ** 2) - 4*a*c

    if D < 0:
        return 'нет вещественых корней'
    elif D == 0:
        return (-b/2*a)
    elif D > 0:
        return ((-b + D ** 0.5) / (2*a), (-b - D ** 0.5) / (2*a))


print(square_root())
