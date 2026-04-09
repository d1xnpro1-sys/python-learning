import random
import sys

player = {
   "hp": 100,
   "money": 100,
   "name": "tryavoid",
   "level": 1,
   "damage": 15
}
enemy = {
    "name": "goblin",
    "hp": 30,
    "damage": 30
}

print()
print("Ваша статистика:")
print("Имя: ",player["name"])
print("Количество денег: ",player["money"])
print("Количество HP: ",player["hp"])
print("Уровень: ",player["level"])
print()

print("Вы шли в лесу и увидели гоблина, ваши действия:")
print("1. Подойду ближе.")
print("2. Пройду мимо.")
print()

choice = input("Выберите действие (1 или 2): ")

if choice == "2":
  print("Вы прошли мимо, дальше ничего не случилось. День прошел спокойно.")
  sys.exit()
elif choice == "1":
  print("Вы подошли поближе и увидели что он один.")
else:
  print("Неверный выбор.")
  sys.exit()


print()
print("Что будете делать?")
print("1. А ничего. Буду сидеть и наблюдать дальше.")
print("2. Приближусь и ... Буду осматривать местность.")
print("3. Уйду подальше.")

choice2 = input("Выберите действие: ")
print()

if choice2 == "3":
   print("Вы ушли.")
   exit()
elif choice2 == "1" or choice2 == "2":
  print("Спустя 10 минут вы решились подойти к нему, гоблин оказался агрессивным.")
else:
  print("Неверный выбор.")
  sys.exit()

print()
print("============ Начался бой! ============")
print()


while enemy["hp"] > 0 and player["hp"] > 0:

  input("Нажми Enter что бы ударить... ")

  enemy["hp"] -= player["damage"]
  print("Вы ударили гоблина.")
  print("У него осталось: ",enemy["hp"], "здоровья")

  if enemy["hp"] <= 0:
    print("Вы победили!")
    break

  damage = random.randint(15, 50)
  player["hp"] -= damage

  print("Гоблин ударил вас.")
  print("Гоблин нанес", damage, "урона.")

  if player["hp"] <= 0:
    print("Вы проиграли!")
    break

print()
print("=========== Бой закончился! ===========")
print()


print("После боя у вас осталось", player["hp"], "здоровья.")

if player["hp"] > 0:
  print("Сразу после победы гоблин исчез, а на его месте появилось 50 монет.")
  player["money"] += 50
  print("Ваш баланс: ",player["money"], "монет.")
