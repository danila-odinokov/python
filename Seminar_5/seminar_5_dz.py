# 1.
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# file = open('file_1.txt', 'r')
# text = file.read()


# new_text = list(filter(lambda x: "абв" not in text, text))
# " ".join(new_text)
# print(new_text)

# 2.
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint                                     # импорт функции из библиотеки
num_candy = 100                                               # назначение кол-ва конфет
dice = lambda: randint(1,6)                                    # лямбда-функция броска кубика

def dice_roll():                                               # функция жеребьёвки
    print("\nЖеребьёвка.")
    print("Игрок один бросает кубик:", end='')
    input()
    first = dice()
    print(f"Выпало число: {first}")
    print("Игрок два бросает кубик:", end='')
    input()
    second = dice()
    print(f"Выпало число: {second}")
    if (first==second):
        print("Ничья. Перебрасываем")
        dice_roll()
    elif(first>second):
        print("Игрок один ходит первым")
        return 1
    else:
        print("Игрок два ходит первым")
        return 2

def candy_grab(total,mode,turn):                                      # функция взятия конфет игроком
    if (mode == 2):
        if turn == 2:
            grab = randint(0,28)
            print(f"Бот взял {grab} конфет")
            total = total - grab
            return total 
    grab = int(input("Сколько конфет вы хотите взять: "))
    if (grab < 0 or grab > 28):
        print("Значение больше 28 или меньше 0")
        candy_grab(total)
    elif(total >= grab):
        print(f"Вы взяли {grab} конфет")
        total = total - grab
        return total
    else:
        print("Столько конфет не осталось")
        candy_grab(total)

def menu():
    print("Правила игры: \nНа столе лежит 2021 конфета.") 
    print("Играют два игрока делая ход друг после друга.")
    print("Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.")
    print("Все конфеты оппонента достаются сделавшему последний ход")
    print("Выберите режим игры:\n1. Против игрока\n2. Против бота (бот будет игроком 2)")
    mode = int(input())
    turn = dice_roll()
    return turn,mode


turn_order,game_mode = menu()

while (num_candy > 0):                                          # условие окончания игры                                         
    print(f"Ход игрока {turn_order}")
    num_candy = candy_grab(num_candy,game_mode,turn_order)
    print(f"Осталось {num_candy} конфет")
    if  turn_order == 1:                                         # смена ходов
        turn_order = 2
    else:
        turn_order = 1 
    

if (turn_order == 2):                                           # определение победителся
    print("Победил игрок 1")
else:
    print("Победил игрок 2")


# 3.
# Создайте программу для игры в ""Крестики-нолики"".

# 4.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.
