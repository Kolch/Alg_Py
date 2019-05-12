from random import randint

# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).


array1 = [randint(-100, 100) for _ in range(0, 30)]
n = len(array1)
print("Начальный массив -", array1)


def bubble_sort_backward(array, n):
    i = 0
    while i < n-1:
        j = n-1
        while j > i:
            if array[j] > array[j - 1]:
                array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1


bubble_sort_backward(array1, n)
print("Конечный массив -", array1)

