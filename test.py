import random
import collections
import math
import json
import re
#1) a = [‘hello’, 1, ‘my’, 2, ‘dear’, 3, ‘friend’] -> b = [‘hello’, ‘my’,  ‘dear’, ‘friend’]
a = ["hello", 1, "my", 2, "dear", 3, "friend"]
del a[1::2]
b = a
print(b)
#2) a = [‘hello’, 1, ‘my’, 2, ‘dear’, 3, ‘friend’] -> b = [1,2,3]
a = ["hello", 1, "my", 2, "dear", 3, "friend"]
del a[::2]
b = a
print(b)
#3) есть список  a = [1,2,3,4,5,6] из него сделать список b -> b = [1, 2, 3, [1, 2, 3, 4, 5, 6], 5, 6]
a = [1,2,3,4,5,6]
c = [1,2,3,4,5,6]
del a[3]
b = a.insert(3,c)
print(a)

#4) a = [1,2,3,4,5,6] -> b = ‘1,2,3,4,5,6’
a = [1,2,3,4,5,6]
a= map(str,a)
b = ','.join(a)
print(b)

#5) a = [‘ba’, ‘e’, ‘wqrt’, ‘frt’, ‘povrt’] -> b = [‘e’, ‘ba’, ‘frt’, ‘wqrt’, ‘povrt’]
a = ['ba', 'e', 'wqrt', 'frt', 'povrt']
def sorti(i):
    return len(i)
a.sort(key=sorti)
print(a)

#6) a = [‘ba’, ‘e’, ‘wqrt’, ‘frt’, ‘povrt’] -> b = [‘ba’, ‘e’, ‘frt’, ‘povrt’, ‘wqrt’]
a1 = ["ba", "e", "wqrt", "frt", "povrt"]
random.shuffle(a1)
def sort(i):
    return i[0]
a1.sort(key=sort)
print(a1)


#7) a = [‘a’, ‘b’, ‘ ‘, 1, ‘ ’, ‘ ’, 3, ‘ ’, ‘ ’, ‘ ‘, ‘r’, ‘ ‘, ‘t’, ‘p’, ‘ ‘, ‘ ‘, ‘ ‘, ‘ ‘]
#->  a=[‘a’, ‘b’, ‘ ‘, 1, ‘ ’,3, ‘ ’, ‘r’, ‘ ‘, ‘t’, ‘p’, ‘ ‘ ]
a = ['a', 'b', ' ', 1, ' ', ' ', 3, ' ', ' ', ' ', 'r', ' ', 't', 'p', ' ', ' ', ' ', ' ']
count = 0
is_spase = False
len_a = len(a)

while len_a:
    i = a[count]
    if i == ' ':
        if is_spase:
            a.pop(count)
            len_a -= 1
            continue
        is_spase = True
        count += 1
    else:
        is_spase = False
        count += 1
    len_a -= 1
print(a)

#8) >>> a = [1,2,3,4,5] >>> d = {a: 'a'}
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: unhashable type: 'list'
#Почему нельзя так сделать? И как мне последовательность чисел а, сделать ключем словаря d?
a = [1,2,3,4,5]
b = tuple(a)
d = {b: 'a'}
print(d)
#9) a = [3, 2, 5,7,10, 1,] b = [10, 9, 0, 4, 3, 2] найти пересечение списков, найти разницу списков
a = [3, 2, 5,7,10, 1]
b = [10, 9, 0, 4, 3, 2]
intersection = [x for x in a if x in b]
print(intersection)
intersection_second = list(set(a) & set(b))
print(intersection_second)
# разница списков
difference = list(set(a) ^ set(b))
print(difference)
#10 e = {1: [1,11,21,31,41,51], 2: [2,12,22,32,42,52]} - e записать в файл в формате json(Java и считать обратно).
# Save---------------
filename = "json_test.txt"
myfile = open(filename, mode='w')
e = {1: [1,11,21,31,41,51], 2: [2,12,22,32,42,52]}
json.dump(e, myfile)
myfile.close()
# Load---------------
myfile = open(filename, mode='r')
json_load = json.load(myfile)
print(json_load)
#11) a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] - суммировать все элементы списка.
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b = sum(a)
print(b)
#12) a из 11 пункта, суммировать квадраты чисел списка.
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
num = [a*a for a in a]
b = sum(num)
print(num,b)
#13) a из 11 пункта, найти только четные числа.
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a = [x for x in a if x % 2 == 0]
print(a)
#14) a = [1] -> b = [1,1,1]
a = [1]
b = a * 3
print(b)
#15) a = [[' ', ' ', ' ', '▆', ' ', ' ', ' '],
#         [' ', ' ', '▆', '▆', '▆', ' ', ' '],
#         [' ', '▆', '▆', '▆', '▆', '▆', ' '],
#         ['▆', '▆', '▆', '▆', '▆', '▆', '▆'],
#         [' ', '▆', '▆', '▆', '▆', '▆', ' '],
#         [' ', ' ', '▆', '▆', '▆', ' ', ' '],
#         [' ', ' ', ' ', '▆', ' ', ' ', ' ']]
#Мир в опасности и срочно нужен код который выведет такую фигуру, причем ромб может быть любых размеров,
#каких надо для спасения мира, и что бы это все красивенько выводилось в консолечку, вся надежда только на тебя.
#И тоже самое надо сделать еще строкой, сделать на массив массивов,
#а строку чтобы при выводе в консоль у меня рисовался ромб.
#Пробельные символы можешь заменить квадратом другого цвета, чтобы были равные интервалы.
s = 7
if s%2 == 1:
    for i in range(1,s,2):
        i = ' ' * ((s - i)//2) + '*' *i + ' ' * (s -i)
        print(i)
    for i in range(s,0,-2):
        i = ' ' * ((s - i) // 2) + '*' * i + ' ' * (s - i)
        print(i)

#16) a = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11'}
#Хочу точно такой же словарь, только чтобы у ключа 8 было значение 88
a = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11'}
b = a.copy()
key = 8
if key in b:
    b[key] = '88'
    print(b)
#17) Дана строка ‘Eat more of these soft French rolls, but drink some tea.’
# подсчитать количество каждой буквы в этой фразу и записать в  словарь где ключ буква - количество занчение.
#  Пробелы и запятые не считаем. Только буквы.
a = 'Eat more of these soft French rolls, but drink some tea.'
b = re.findall(r'\w', a)
d = dict()
for i in b:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
print(d)
#18) есть два листа a = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’] b = [1,2,3,4,5,6,7,8,9]
# сделать из них третий с = ['1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '1b', '2b', '3b', '4b', '5b',
#  '6b', '7b', '8b', '9b', '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '1d', '2d', '3d', '4d', '5d',
#  '6d', '7d', '8d', '9d', '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e', '9e', '1f', '2f', '3f', '4f', '5f',
#  '6f', '7f', '8f', '9f']
a = ['a','b','c','d','e','f']
b = ['1','2','3','4','5','6','7','8','9']
#c = [str(x)+y for x in b for y in a]
c =[]
for x in a:
    for y in b:
        c.append(y+x)
print(c)
#19)есть два листа a = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’] b = [1,2,3,4,5,6]
# сделать дикт d = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f'}
a = ['a', 'b', 'c', 'd', 'e', 'f']
b = [1,2,3,4,5,6]
c = {}
for x,y in zip(b,a):
    c[x] = y
print(c)
#20) есть дикт a = {'eat': {'fruit' : {'bananas': 15, 'lemon': 11}, 'vegetables': {'carrot': 10,'potato': 5}}}
# хочу узнать количество бананов и хочу чтобы картошки было 17
a = {'eat': {'fruit' : {'bananas': 15, 'lemon': 11}, 'vegetables': {'carrot': 10,'potato': 5}}}
print(a['eat']['fruit']['bananas'])
a['eat']['vegetables']['potato'] = 17
print(a)