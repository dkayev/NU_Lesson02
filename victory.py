# Курс Python-разработчик Тема 2.
# victory.py - программа для задания Модуль 6.

# Программа "Викторина - годы рождения знаменитостей"

# Используем следующие данные о знаменитостях:

# W. Blake - 1757
# A. Pushkin - 1799
# N. Gogol - 1809
# W. Whitman - 1819
# M. Bulgakov - 1891

game_on = True

print('Hello!')
print("In this game you will be asked about birth years of 5 famous persons.")
print()

while game_on:

    year_entered = 0
    right_answers_count = 0
    wrong_answers_count = 0
    right_answers_percentage = 0
    wrong_answers_percentage = 0


    year_entered = int(input("Enter the birth year of W. Blake: "))
    if year_entered != 1757:
        wrong_answers_count += 1
    else:
        right_answers_count += 1

    year_entered = int(input("Enter the birth year of A. Pushkin: "))
    if year_entered != 1799:
        wrong_answers_count += 1
    else:
        right_answers_count += 1

    year_entered = int(input("Enter the birth year of N. Gogol: "))
    if year_entered != 1809:
        wrong_answers_count += 1
    else:
        right_answers_count += 1

    year_entered = int(input("Enter the birth year of W. Whitman: "))
    if year_entered != 1819:
        wrong_answers_count += 1
    else:
        right_answers_count += 1

    year_entered = int(input("Enter the birth year of M. Bulgakov: "))
    if year_entered != 1891:
        wrong_answers_count += 1
    else:
        right_answers_count += 1

    right_answers_percentage = (right_answers_count * 100)/5
    wrong_answers_percentage = 100 - right_answers_percentage

    print()
    print("OK, now your results are:")
    print()
    print("Right answers number: ", right_answers_count)
    print("Wrong answers number: ", wrong_answers_count)
    print("Right answers percentage: ", right_answers_percentage)
    print("Wrong answers percentage: ", wrong_answers_percentage)
    print("That's it!")

    request = input("Wanna start the game again? Enter y(es) or n(o): ")
    if request == "n":
        game_on = False
print("Thank you! The game is over!")