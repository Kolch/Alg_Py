from random import randint
import timeit

# так как алгоритмы из предыдущих уроков показались мне немного скучными и простыми для анализа, я решил написать
# несколько сортировок и проанализировать их

array1 = [randint(-100,100) for _ in range(0, 30)]
array2 = array1
array3 = array1

# cортировка пузырьком
n = len(array1)
print("Начальный массив -", array1)


def bubble_sort(array, n):
    i = 0
    while i < n-1:
        j = n-1
        while j > i:
            if array[j] < array[j - 1]:
                array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1


bubble_sort(array1, n)
print("Сортировка пузырьком")
print(array1)

"""
Оценка сложности:
лучший случай - O (n)
общий случай - O (n ^ 2)
наихудший случай - O (n ^ 2)
"""

# сортировка шейкером


def shaker_sort(array):
    for i in range(len(array) - 1, 0, -1):
        swapped = False

        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swapped = True

        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            return array


shaker_sort(array2)
print("Сортировка шейкером")
print(array2)

"""
В общем то шейкерная сортировка от "пузырька" не отличается по сложности
"""

# быстрая сортировка 


def quick_sort(array):
    n = len(array)
    if n <= 1:
        return array
    else:
        pivot = array[0]
        bigger = [element for element in array[1:] if element > pivot]
        smaller = [element for element in array[1:] if element <= pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(bigger)


quick_sort(array3)
print("Быстрая сортировка")
print(array3)

"""
Оценка сложности:
лучший случай - O (n * log(n))
общий случай - O (n * log(n))
наихудший случай - O (n ^ 2)
"""








