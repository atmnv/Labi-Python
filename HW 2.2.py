"""Data analysis Lab 2
Task 2. Атманов Дидар. Информатика"""

enterAYear = int(input("Введите год :"))
if enterAYear < 3000 and enterAYear > 0:
    if enterAYear %4 == 0:
        print ("Yes")
    else:
        print("No")
else:
    print("Вы ввели неправильный год!")

