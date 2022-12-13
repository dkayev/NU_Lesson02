# Курс Python-разработчик Тема 2.
# bornyday.py - программа для задания Модуль 3.

# Программа "Дата рождения Пушкина"

print('Привет!')
year_of_birth= int(input("Укажите год рождения А.С.Пушкина: "))

if year_of_birth == 1799:
    day_of_birth = input("Теперь укажите день рождения А.С. Пушкина в формате dd.mm: ")
    if day_of_birth == "06.06":
        print("Все правильно!")
    else:
        print("Вы указали неверный день!")
#   print("You are right!")
else:
    print("Вы указали неверный год!")