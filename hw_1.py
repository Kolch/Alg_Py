from random import random

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
print("Сумма цифр трехзначного числа")
input_num = input("Введите трехзначное число: ")
int_num = int(input_num)
result1 = 0
while int_num != 0:
    result1 = result1 + int_num % 10
    int_num = int_num // 10
print("Сумма цифр = ", result1)

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
a = 5     # 0101
b = 6     # 0110

c = a & b  # 0100 = 4
d = a | b  # 0111 = 7
e = a ^ b  # 011 = 3
f = ~ a  # 01...11111010 = -6
j = a >> 2  # 00...001 = 1
h = a << 2  # 10100 = 20

# Не понял, как именно надо объяснить полученый результат, как по мне все предельно ясно. Побитовый сдвиг - сдвиг всех
# битов числа на указанное расстояние в указанном направлении, от туда и результат. Результат битовых операций -
# результат применения указаного оператора(И, ИЛИ и тд) к битам обоих операндов


# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

print("Введите координаты точки A:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("Введите координаты точки B:")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

print("Уравнение прямой:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print("y = %.2f*x + %.2f" % (k, b))

# 4. Написать программу, которая генерирует в указанных пользователем границах:
#
#     случайное целое число;
#     случайное вещественное число;
#     случайный символ.
#
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

print("Выберете вариант:")
print("\tслучайное целое число - 1")
print("\tслучайное вещественное число - 2")
print("\tслучайный символ - 3")
opt = int(input("[1/2/3]: "))
if opt == 1:
    int1 = int(input("Введите нижнюю границу:"))
    int2 = int(input("Введите верхнюю границу:"))
    result4 = int(random() * (int2 - int1 + 1)) + int1
    print(result4)
elif opt == 2:
    int1 = float(input("Введите нижнюю границу:"))
    int2 = float(input("Введите верхнюю границу:"))
    result4 = random() * (int2 - int1) + int1
    print(round(result4, 2))
elif opt == 3:
    ch_1 = ord(input("Введите нижнюю границу:"))
    ch_2 = ord(input("Введите верхнюю границу:"))
    result4 = int(random() * (ch_2 - ch_1 + 1)) + ch_1
    print(chr(result4))
else:
    print("Такого варианты нет!")


# alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
# #         "w", "x", "y", "z"]

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

# Вариант с массивом (сначала сделал с ним, потом прочитал следующее задание и понял что это слишком просто,
# значит имелась в виду другая реализация)
# char1 = input("Введите первую букву:")
# char2 = input("Введите вторую букву:")
# index1 = alph.index(char1.lower())
# index2 = alph.index(char2.lower())
# if index1 > index2:
#     dif = index1 - index2
# else:
#     dif = index2 - index1
# print("Место буквы", char1, "в алфавите -", index1 + 1)
# print("Место буквы", char2, "в алфавите -", index2 + 1)
# print("Мужду ними -", dif - 1)


# Вариант через таблицу символов
char1 = ord(input("Введите первую букву:"))
char2 = ord(input("Введите вторую букву:"))
char1 = char1 - ord("a") + 1
char2 = char2 - ord("a") + 1
print("Позиции: %d и %d" % (char1, char2))
print("Мужду ними -", abs(char1-char2)-1)


# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# Вариант через массив. Тут то я и понял что это подозрительно легко)
# char_num = input("Введите номер буквы в алфавите: ")
# print("Это буква ", alph[int(char_num) - 1])

char_id = int(input('Номер буквы в алфавите: '))
char_id = ord("a") + char_id - 1
print("Это буква", chr(char_id))

# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
print("Задача с треугольником")
t_a = int(input("a = "))
t_b = int(input("b = "))
t_c = int(input("c = "))

if t_a + t_b <= t_c or t_a + t_c <= t_b or t_b + t_c <= t_a:
    print("Треугольника не существует")
elif t_a != t_b and t_a != c and b != t_c:
    print("Треугольник разносторонний")
elif t_a == t_b == t_c:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")


# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
year = int(input("Введите год: "))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("Это не високосный год")
else:
    print("Это високосный год!")

# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print("Посик среднего числа")
int_a = int(input("Введите число А: "))
int_b = int(input("Введите число B: "))
int_c = int(input("Введите число C: "))

if (int_a > int_b and int_a < int_c) or (int_a < int_b and int_a > int_c):
    result9 = int_a
elif (int_b < int_a and int_b > int_c) or (int_b > int_a and int_b < int_c):
    result9 = int_b
else:
    result9 = int_c
print("Среднее число -", result9)
