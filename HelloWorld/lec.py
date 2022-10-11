# print('hello world')

# # типы данных и переменная
# # int, float, boolean, str, list, None

# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 12334
# print(value)

# print(type(a))
# print(type(b))
# print(type(value))

# s = 'qwerty'

# print(s)
# print(type(s))

# st = "qwe 'rty' "

# print(st)

# print(a,' - ',b,' - ',s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ["1","2","3"]
# col = ["hello", 1,2,4.5,True]
# print(list)
# print(col)

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, '+' , b, '=', a+b)

# a = 1.312312
# b = 3
# c = round(a * b, 5)
# print(c)

# # Сокращенное присваивание

# a = 3
# a += 5

# print (a)

# # Логические операции
# # >, >=, <, <=, ==, !=
# # not, and, or - не путать с &, |, ^
# # is, is not, in, not in
# # gen

# a = 1 < 4 and 5 > 2
# print(a)
# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# # Управляющие конструкции
# # if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# for

for i in 1,2,3,4,10,5:
    print(i**2)

for i in range(1,10,2):
    print(i)

for i in 'qwe - rty':
    print(i)

# Функции

def f(x):
    if x == 1:
        return "Целое"
    elif x == 2.3:
        return 23
    else:
        return

arg = 2.3
print(f(arg))
print(type(f(arg)))