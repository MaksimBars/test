# 25.Нужно функцию, которая будет имитировать звуки животных домашних - кошку, собаку, птичку.
#  На вход подается тип животного строкой - dog, cat, parrot - на выходе издаваемые ими звуки,
# (только для этого задания - если мы не передаем никакого животного - по умолчанию оно должно
#  чирикать как птичка)


def main():
    animal = str(input())
    if animal == 'cat':
        print('may-may')
    elif animal == 'dog':
        print('gay-gay')
    elif animal == 'parrot':
        print('chirik-chirik')
    else:
        print('kar-kar')


if __name__ == '__main__':
    main()
