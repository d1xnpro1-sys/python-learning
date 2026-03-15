print("===== Игра: Угадай число =====")
print()
print("-" * 30)

print("Хочешь сыграть в игру?")
print()

answer = input("Да / нет: ").lower()

if answer not in ["да", "хочу", "хорошо", "ага"]:
    print()
    print("Ну ладно")
else:
    print("Отлично! Начинаем игру")
    print("Нужно угадать число от 1 до 20")
    print()

    attempt = 5
    secret = 8

    while attempt > 0:

        if attempt == 1:
            print("У тебя осталась", attempt, "попытка")
        elif attempt < 5:
            print("У тебя осталось", attempt, "попытки")
        else:
            print("У тебя будет всего", attempt, "попыток")

        x = int(input("Введи число: "))

        if x == secret:
            print("Молодец! Ты угадал")
            break

        elif x < secret:
            print("Заданное число больше")

        else:
            print("Заданное число меньше")

        attempt -= 1
        print()

    print("Игра закончена")
