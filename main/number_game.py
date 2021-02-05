from random import randint

def main():
    start = 1
    end = 10
    greeting = "Привет, я хочу сыграть с тобой в игру."
    rules = "Правила такие: я загадываю число от {} до {}. \n У тебя есть 5 попыток на то, чтобы его угадать)".format(start, end)
    rules = "Правила такие: я загадываю число от 1 до 10. \n У тебя есть 5 попыток на то, чтобы его угадать)".format(start, end)
    my_number = randint(start, end)
    counter = 1
    print(greeting + rules + " Поехали!")
    while counter <= 5:
        your_number = input("Твоё число: ")
        try:
            your_number = int(your_number)
        except ValueError:
            print('Это не число. Минус попытка.')
            counter += 1
            continue
        if your_number == my_number:
            print("Да, ты угадал! Я загадывал " + str(my_number) + "!")
            break
        elif counter == 5:
            print("Увы, попыток больше нет. Моё число: {}".format(my_number))
        elif your_number > end or your_number < start:
            print("Нехорошо. Осуждаю. В пределах от {} до {} включительно. Осталось {} попыток.".format(start, end, (5 - counter)))
        else:
            print("Увы, нет. Осталось {} попыток.".format(5 - counter))
        counter += 1


if __name__ == '__main__':
    main()