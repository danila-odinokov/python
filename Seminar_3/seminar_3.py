# 1. Алгоритм генерации случайного значения (1-100)

from time import time
my_time = time()
print(int((my_time % 1)*100))

# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

my_list = ["123", "1234", "567"]
number = "123"
nul = 0
for i in my_list:
    if i == number:
        print("Число присутствует в списке")
        break

for elem in my_list:
    if number in elem:
        print(elem)
        print(my_list.index(elem, nul))
        nul = my_list.index(elem, nul) + 1

for i, elem in enumerate(my_list):
    if number in elem:
        print(elem)
        print(i)

# 3. Ищем второе вхождение элемента в списке

my_list = ["123", "234", "12333", "123", "567", "123"]
number = my_list[0]

print(my_list.index(number, 1))