"""Data analysis Lab 2
Task 3. Атманов Дидар. Информатика"""

numberA, numberB = [int(input("Введите числа :")) for numbers in range(2)]
even = numberA + numberA % 2

for numbers in range(even, numberB + 1, 2):
    print(numbers, end=' ')
