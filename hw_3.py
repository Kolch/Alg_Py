from random import randint

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
print("Задача 1")
array1 = [i for i in range(2, 100)]
result1 = [0] * 8
for i in array1:
    count = 0
    for j in range(2, 10):
        if i % j == 0:
            result1[j-2] += 1
i = 0
while i < len(result1):
    print("Чисел кратных %d - %d" % (i+2, result1[i]))
    i += 1

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
print("Задача 2")
array2 = [randint(0, 100) for _ in range(15)]
even_array = []
for i in array2:
    if i % 2 == 0:
        even_array.append(array2.index(i))
print("Исходный массив -", array2)
print("индексы четных элементов массива -", even_array)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
print("Задача 3")
array3 = [randint(0, 100) for _ in range(15)]
a = -1
b = 100
for i in array3:
    if i > a:
        a = i
for i in array3:
    if i < b:
        b = i
print("Начальный массив -", array3)
inx_a = array3.index(a)
inx_b = array3.index(b)
array3[inx_a], array3[inx_b] = b, a
print("Измененный массив -", array3)

# 4. Определить, какое число в массиве встречается чаще всего.
# при наличии нескольких чисел равных по частоте появления выводится то, что больше по индексу
print("Задача 4")
array4 = [randint(0, 10) for _ in range(15)]
digit = -1
d_count = 0
for i in array4:
    count = 0
    for j in array4:
        if j == i:
            count += 1
    if count > d_count:
        d_count = count
        digit = i
print("В массиве -", array4)
print("Чаще всего встречается число %d (%d раз)" % (digit, d_count))

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
print("Задача 5")
array5 = [randint(-100, 100) for _ in range(15)]
result5 = 0
pos = -1
for i in array5:
    if i < result5:
        result5 = i
        pos = array5.index(i)
print("В массиве -", array5)
print("максимальный отрицательный элемент: %d, индекс - %d" % (result5, pos))

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
print("Задача 6")
array6 = [randint(0, 100) for _ in range(15)]
_max = -1
_min = 100
# ищем максимальный и минимальный элементы
for i in array6:
    if i > _max:
        _max = i
for i in array6:
    if i < _min:
        _min = i
inx_max = array6.index(_max)
inx_min = array6.index(_min)
result6 = 0
# считаем разницу индексов и минус один что бы не включать элементы
# и через цикл с кол-вом итераций равному кол_ву элементов между числами считаем
if inx_max > inx_min:
    z = inx_max - inx_min - 1
    iter = 1
    for i in range(z):
        result6 += array6[inx_min + iter]
        iter += 1
else:
    z = inx_min - inx_max - 1
    iter = 1
    for i in range(z):
        result6 += array6[inx_max + iter]
        iter += 1
print("В массиве -", array6)
print("сумму элементов, находящихся между минимальным(%d) и максимальным(%d) элементами - %d" % (_min, _max, result6))

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# сначала находим минимальное число, затем считаем кол-во его повторений, если больше одного значит выводим его дважды,
# если 1, то снова ищем минимальное число, но с условием что оно не равному ранее найденому
print("Задача 7")
array7 = [randint(0, 10) for _ in range(15)]
xx = 100
yy = 100
count = 0
for i in array7:
    if i < xx:
        xx = i

for i in array7:
    if i == xx:
        count += 1

if count > 1:
    yy = xx
else:
    for i in array7:
        if i < yy and i != xx:
            yy = i
print("В массиве -", array7)
print("два наименьших элемента: %d, %d" % (xx, yy))
# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
print("Задача 8")
array8 = []
for i in range(5):
    temp_array = []
    last = 0
    for j in range(3):
        w = int(input("Введите число для %d строки, %d эелемента" % (i + 1, j + 1)))
        temp_array.append(w)
    array8.append(temp_array)

for i in array8:
    last = 0
    for j in i:
        last += j
    i.append(last)


for i in array8:
    print(i)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# используется та же матрица что и в предыдущем задании
print("Задача 9")

array9 = []
for i in array8:
    min_row = 10000
    for j in i:
        if j < min_row:
            min_row = j
    array9.append(min_row)

result9 = -1000
for i in array9:
    if i > result9:
        result9 = i

print("Минимальные элементы столбцов матрицы -", array9)
print("максимальный из них: %d" % result9)
