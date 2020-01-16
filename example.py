#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

for i in range(1,6):
    print("0" * i)


'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
count = 0
for i in range(1, n + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print("Было введено %d цифр %d" % (count, d))

'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
    sum+=i
print(sum)

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
pr = 1

for i in range(1,11):
        pr*=i
print(pr)


'''
Задача 5

Вывести цифры числа на каждой строчке.
'''

integer_number = 2329

#print(integer_number%10,integer_number//10)

while integer_number>0:
     print(integer_number%10)
     integer_number = integer_number//10

'''
Задача 6

Найти сумму цифр числа.
'''
from random import random
n=int(random()*5687)
print(n)
s = str(n)
sm = 0
for i in range(len(s)):
    sm+=int(s[i])
print(sm)

'''
Задача 7

Найти произведение цифр числа.
'''
from random import random
n=int(random()*5687)
print(n)
s = str(n)
sm = 1
for i in range(len(s)):
    sm*=int(s[i])
print(sm)

'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 2134513
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9

Найти максимальную цифру в числе
'''
x = 234
maxim = 1
print(x)

while x > 0:
    last = x % 10
    if last > maxim:
        maxim=last
    x = x // 10

print('число=', maxim)

'''
Задача 10

Найти количество цифр 5 в числе

'''

n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
count = 0
for i in range(1, n + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print("Было введено %d цифр %d" % (count, d))5