# 25.Нужно функцию, которая будет имитировать звуки животных домашних - кошку, собаку, птичку.
#  На вход подается тип животного строкой - dog, cat, parrot - на выходе издаваемые ими звуки,
# (только для этого задания - если мы не передаем никакого животного - по умолчанию оно должно
#  чирикать как птичка)

name = str(input())
animals = {"cat": 'may-may', "dog": 'gay-gay', "parrot": 'chirik-chirik', "pig": 'xry-xry', "cow": 'my-my'}


def main():
    if name in animals:
        print(animals.get(name))
    else:
        print('kar-kar')


if __name__ == '__main__':
    main()
