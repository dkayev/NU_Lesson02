# Курс Python-разработчик Тема 2.
# bornyearforewer.py - программа для задания Модуль 4.

# Программа "Год рождения Пушкина" с использованием while

print('Привет!')

year_of_birth = int(input("Укажите год рождения А.С. Пушкина: "))

while year_of_birth != 1799:
    print("Неверный год!")
    year_of_birth = int(input("Укажите год рождения А.С. Пушкина: "))

print("Все правильно!")