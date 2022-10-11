
# открытие и чтение данных из файла

path = 'Lecture_2/file.txt'
data = open(path, 'r')
for line in data:
    print(line, end='')
data.close()

# присвоение аргументу функции стандартного значения

def new_string(symbol, count = 3):
    return symbol * count
print(new_string('!', 5))   # !!!!!
print(new_string('!'))      # !!!
print(new_string(4))        # 12

# набор данных в качестве аргумента функции

def cont(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(cont('a', 's', 'd', 'w'))     # asdw
print(cont('a', '1'))               # a1


# кортеж - это неизменяемый список

a = (3,4)

print(a)        # (3, 4)
print(a[0])     # 3
# a[0] = 12 --- ошибка
for item in a:
    print(item)     # 3
                    # 4

# превращение списка в кортеж и последующее превращение его в отдельные переменные

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print(red, green, blue)

# словари - это неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}
dictionary = \
    {
        'up': '1',
        'down': '2'
    }
print(dictionary)
print(dictionary['up'])
del dictionary['down']
print(dictionary)
