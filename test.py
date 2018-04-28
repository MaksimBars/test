import random
import json
import re

# 1) a = [‘hello’, 1, ‘my’, 2, ‘dear’, 3, ‘friend’] -> b = [‘hello’, ‘my’,  ‘dear’, ‘friend’]

a = ["hello", 1, "my", 2, "dear", 3, "friend"]
del a[1::2]
b = a
print(b)

# 2) a = [‘hello’, 1, ‘my’, 2, ‘dear’, 3, ‘friend’] -> b = [1,2,3]

a = ["hello", 1, "my", 2, "dear", 3, "friend"]
del a[::2]
b = a
print(b)

# 3) есть список  a = [1,2,3,4,5,6] из него сделать список b -> b = [1, 2, 3, [1, 2, 3, 4, 5, 6], 5, 6]

a = [1, 2, 3, 4, 5, 6]
c = [1, 2, 3, 4, 5, 6]
del a[3]
a.insert(3, c)
print(a)

# 4) a = [1,2,3,4,5,6] -> b = ‘1,2,3,4,5,6’

a = [1, 2, 3, 4, 5, 6]
a = map(str, a)
b = ','.join(a)
print(b)

# 5) a = [‘ba’, ‘e’, ‘wqrt’, ‘frt’, ‘povrt’] -> b = [‘e’, ‘ba’, ‘frt’, ‘wqrt’, ‘povrt’]

a = ['ba', 'e', 'wqrt', 'frt', 'povrt']


def sorti(x):
    return len(x)


a.sort(key=sorti)
print(a)

# 6) a = [‘ba’, ‘e’, ‘wqrt’, ‘frt’, ‘povrt’] -> b = [‘ba’, ‘e’, ‘frt’, ‘povrt’, ‘wqrt’]

a1 = ["ba", "e", "wqrt", "frt", "povrt"]
random.shuffle(a1)


def sort(x):
    return x[0]


a1.sort(key=sort)
print(a1)


# 7) a = [‘a’, ‘b’, ‘ ‘, 1, ‘ ’, ‘ ’, 3, ‘ ’, ‘ ’, ‘ ‘, ‘r’, ‘ ‘, ‘t’, ‘p’, ‘ ‘, ‘ ‘, ‘ ‘, ‘ ‘]
# ->  a=[‘a’, ‘b’, ‘ ‘, 1, ‘ ’,3, ‘ ’, ‘r’, ‘ ‘, ‘t’, ‘p’, ‘ ‘ ]

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

# 8) >>> a = [1,2,3,4,5] >>> d = {a: 'a'}
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
# Почему нельзя так сделать? И как мне последовательность чисел а, сделать ключем словаря d?

a = [1, 2, 3, 4, 5]
b = tuple(a)
d = {b: 'a'}
print(d)

# 9) a = [3, 2, 5,7,10, 1,] b = [10, 9, 0, 4, 3, 2] найти пересечение списков, найти разницу списков

a = [3, 2, 5, 7, 10, 1]
b = [10, 9, 0, 4, 3, 2]
intersection = [x for x in a if x in b]
print(intersection)
intersection_second = list(set(a) & set(b))
print(intersection_second)
# разница списков
difference = list(set(a) ^ set(b))
print(difference)

# 10 e = {1: [1,11,21,31,41,51], 2: [2,12,22,32,42,52]} - e записать в файл в формате json(Java и считать обратно).

# Save---------------
filename = "json_test.txt"
my_file = open(filename, mode='w')
e = {1: [1, 11, 21, 31, 41, 51], 2: [2, 12, 22, 32, 42, 52]}
json.dump(e, my_file)
my_file.close()
# Load---------------
my_file = open(filename, mode='r')
json_load = json.load(my_file)
print(json_load)

# 11) a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] - суммировать все элементы списка.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
b = sum(a)
print(b)

# 12) a из 11 пункта, суммировать квадраты чисел списка.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
num = [a*a for a in a]
b = sum(num)
print(num, b)

# 13) a из 11 пункта, найти только четные числа.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = [x for x in a if x % 2 == 0]
print(a)

# 14) a = [1] -> b = [1,1,1]

a = [1]
b = a * 3
print(b)

# 15) a = [[' ', ' ', ' ', '▆', ' ', ' ', ' '],
#          [' ', ' ', '▆', '▆', '▆', ' ', ' '],
#          [' ', '▆', '▆', '▆', '▆', '▆', ' '],
#          ['▆', '▆', '▆', '▆', '▆', '▆', '▆'],
#          [' ', '▆', '▆', '▆', '▆', '▆', ' '],
#          [' ', ' ', '▆', '▆', '▆', ' ', ' '],
#          [' ', ' ', ' ', '▆', ' ', ' ', ' ']]
# Мир в опасности и срочно нужен код который выведет такую фигуру, причем ромб может быть любых размеров,
# каких надо для спасения мира, и что бы это все красивенько выводилось в консолечку, вся надежда только на тебя.
# И тоже самое надо сделать еще строкой, сделать на массив массивов,
# а строку чтобы при выводе в консоль у меня рисовался ромб.
# Пробельные символы можешь заменить квадратом другого цвета, чтобы были равные интервалы.

s = 7
if s % 2 == 1:
    for i in range(1, s, 2):
        i = ' ' * ((s - i)//2) + '*' * i + ' ' * (s - i)
        print(i)
    for i in range(s, 0, -2):
        i = ' ' * ((s - i) // 2) + '*' * i + ' ' * (s - i)
        print(i)

# 16) a = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11'}
# Хочу точно такой же словарь, только чтобы у ключа 8 было значение 88

a = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: '11'}
b = a.copy()
key = 8
if key in b:
    b[key] = '88'
    print(b)

# 17) Дана строка ‘Eat more of these soft French rolls, but drink some tea.’
# подсчитать количество каждой буквы в этой фразу и записать в  словарь где ключ буква - количество занчение.
#  Пробелы и запятые не считаем. Только буквы.

a = 'Eat more of these soft French rolls, but drink some tea.'
b = re.findall(r'\w', a)
d = dict()
for i in b:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

# 18) есть два листа a = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’] b = [1,2,3,4,5,6,7,8,9]
# сделать из них третий с = ['1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '1b', '2b', '3b', '4b', '5b',
#  '6b', '7b', '8b', '9b', '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '1d', '2d', '3d', '4d', '5d',
#  '6d', '7d', '8d', '9d', '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e', '9e', '1f', '2f', '3f', '4f', '5f',
#  '6f', '7f', '8f', '9f']

a = ['a', 'b', 'c', 'd', 'e', 'f']
b = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# c = [str(x)+y for x in b for y in a]
c = []
for x in a:
    for y in b:
        c.append(y+x)
print(c)

# 19)есть два листа a = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’] b = [1,2,3,4,5,6]
# сделать дикт d = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f'}

a = ['a', 'b', 'c', 'd', 'e', 'f']
b = [1, 2, 3, 4, 5, 6]
c = {}
for x, y in zip(b, a):
    c[x] = y
print(c)

# 20) есть дикт a = {'eat': {'fruit' : {'bananas': 15, 'lemon': 11}, 'vegetables': {'carrot': 10,'potato': 5}}}
# хочу узнать количество бананов и хочу чтобы картошки было 17

a = {'eat': {'fruit': {'bananas': 15, 'lemon': 11}, 'vegetables': {'carrot': 10, 'potato': 5}}}
# print(a['eat']['fruit']['bananas'])
key = 'bananas'
b = a['eat']['fruit']
if key in b:
    print(b.get(key))
# a['eat']['vegetables']['potato'] = 17
# print(a)
key = 'potato'
b = a['eat']['vegetables']
if key in b:
    b[key] = 17
    print(a)

# 21) сделать две функции первая - куда я в качестве параметров передаю мой dict a из 20 задания
#  мне должно вернуться количество лимонов,вторая - в качестве параметров принимает мой дикт,
# и количество моркови и мне возвращается новый дикт с измененным количеством морковки.
# 21)-1 функция

food = {'eat': {'fruit': {'bananas': 15, 'lemon': 11}, 'vegetables': {'carrot': 10, 'potato': 5}}}
key_1 = 'eat'
key_2 = 'fruit'
key_3 = 'lemon'


def box(x):
    b = x[key_1][key_2]
    if key_3 in b:
        return key_3, b.get(key_3)


print(box(food))

# 21)-2 функция

food = {'eat': {'fruit': {'bananas': 15, 'lemon': 11}, 'vegetables': {'carrot': 10, 'potato': 5}}}
key_one = 'eat'
key_two = 'vegetables'
key_three = 'carrot'


def how_carrot(x, y):
    b = x[key_one][key_two]
    if key_three in b:
        b[key_three] = y
        return x


print(how_carrot(food, int(input('Количество моркови:'))))

# 22) a = [1,2,3,4,5] -> b = [1,3,6,10,15]

a = [1, 2, 3, 4, 5]
b = [sum(a[:x]) for x in range(a[0], len(a)+1)]
print(b)

# 23) Надо сделать три функции. первая функция - главная(допустим main) - в ней необходимо получать строку с ввода
# с консоли-это должно быть число, далее в зависимости от того, четное это число или нет делаем следующее:
# Если четное - вызывать функцию (int_sum) и передать туда в качестве параметра полученное с ввода число и внутри
# функции int_sum суммировать его с самим собой и вернуть результат в функцию main.# Если нечетное вызвать функцию
# (int_mult) и передать туда на в качестве параметра введеное число, внутри функции int_mult его возвести в куб и
#  вернуть функции main.В функции main полученный результат распечатать в консоль.


def int_sum(number):
    sum_number = number + number
    return sum_number


def int_mult(number):
    mult_number = number ** number
    return mult_number


def main():
    number = int(input("Input number: "))
    if number % 2 == 0:
        print(int_sum(number))
    else:
        print(int_mult(number))


if __name__ == '__main__':
    main()


# 24) Есть маленькая одинокая функция:
# def a():
#   return "Sergey"
# если мы сделаем:
# print(a()) то увидим в консоли Sergey
# создать декоратор и обернуть в него нашу функцию а, таким образом, чтобы print(a()) выводил: Hi! i’am Sergey!

def decorator(func):
    def wrapper():
        print('Hi! i’am {}!'.format(func()))
        return 'Hi! i’am %s!' % (func())
    return wrapper


@decorator
def a():
    return "Sergey"


print(a())

# 25.Нужно функцию, которая будет имитировать звуки животных домашних - кошку, собаку, птичку.
#  На вход подается тип животного строкой - dog, cat, parrot - на выходе издаваемые ими звуки,
# (только для этого задания - если мы не передаем никакого животного - по умолчанию оно должно
#  чирикать как птичка)

name = str(input("Enter the name: "))
animals = {"cat": 'may-may', "dog": 'gay-gay', "parrot": 'chirik-chirik', "pig": 'xry-xry', "cow": 'my-my'}


def main():
    if name in animals:
        print(animals.get(name))
    else:
        print('kar-kar')


if __name__ == '__main__':
    main()
