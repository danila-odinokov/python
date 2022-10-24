# 1.
# Вычислить число c заданной точностью d
# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = input("Введите точность: ")     
num = input("Введите число: ")
d_ls = [int(i) for i in d if i.isdigit()]            # преобразование строки в список чисел
num_ls = [int(i) for i in num if i.isdigit()]
d = d_ls.index(1)                                    # поиск разряда до которого округляем
result = 0

while (len(num_ls)-1 > d):
    if num_ls[-1] >= 5:                              # округление к ближайшему целому
        num_ls[-2] += 1                     
    num_ls.pop()

for i in range(len(num_ls)):                         # преобразование списка в число
    result += num_ls[i] * 10 ** -i

print(result)


# 2.
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def primes():
    ls = []
    d = 2                                               # наименьшее простое число (делитель)
    n = int(input("Введите натуральное число: "))
    while d <= n:
        if n % d == 0:                                  # проверка деления нацело
            ls.append(d)                                # добавление простого множителя в список
            n /= d                                      # деление исходного числа на множитель
            d = 2                                       # сброс значения делителя
        else:
            d += 1                                      # инкремент делителя
    print(f"Список простых множителей: {ls}")

primes()

# 3.
# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

def list_create():
    a = int(input("Введите длину списка: "))
    sp = []
    for i in range(a):
        sp.append(int(input(f"Введите значение {i} элемента: ")))
    return sp

def unique_elem(ls):
    res = []
    [res.append(elem) for elem in ls if elem not in res]
    return res

nums = list_create()
print(unique_elem(nums))

# 4.
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input("Введите степень многочлена: "))
ls = []
delim = "+"                                                   # разделитель 
for i in range(k+1):                    
    a = randint(0,100)                                        # генерация числа от 0 до 100
    if a == 0:
        continue
    if i == 0:
        ls.append(str(a))
    else:
        ls.append(f"${str(a)}*x^" + "{" + str(i) + "}$")      # форматирование для markdown

ls.reverse()
ls = delim.join(ls)                                           # преобразование списка в строку с разделителем

f = open('res.md', 'w')                                       # работа с файлом
f.write(ls)
f.close()

# 5.
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

first = open('file_1.md', 'r')
second = open('file_2.md', 'r')
a,b = first.read(),second.read()
numbers = []
res = []

def transform(str):                 # форматирование входных данных
    new_ls = []
    str = str.replace("$", "")
    str = str.replace("x^{", "")
    str = str.replace("}", "")
    str = str.split("+")
    for elem in str:
        elem = elem.split("*")
        new_ls.append(elem)
    for elem in new_ls:
        for num in elem:
            num = int(num)
    new_dict = dict(new_ls)
    new_dict = {int(key):int(value) for key, value in new_dict.items()}
    new_dict = {value:key for key, value in new_dict.items()}
    return new_dict

dict_a, dict_b = transform(a), transform(b)    
a_max, b_max = len(dict_a), len(dict_b)

if a_max > b_max:              
    k = a_max
else:
    k = b_max

for i in range(k):
    numbers.append(dict_a.get(i,0)+dict_b.get(i,0))

numbers.reverse()

for num in numbers:
    k -= 1
    res.append(f"${str(num)}*x^" + "{" + str(k) + "}$")

res = ("+").join(res) 

f = open('result.md', 'w')                                       # работа с файлом
f.write(res)
f.close()
