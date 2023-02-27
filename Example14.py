#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


n = int(input("Введите число N: "))
temp = 1
count = 0
while temp < n:
    print(temp)
    temp*=2
    count = 1
if count == 0:
    print("таких чисел нет")