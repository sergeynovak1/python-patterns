MIN_RUN = 32


def insertion_sort(lst, left, right):
    """
    Сортировка вставками для подмассива lst[left:right+1].

    Аргументы:
    lst -- список чисел для сортировки
    left -- начальный индекс подмассива
    right -- конечный индекс подмассива
    """
    for i in range(left + 1, right + 1):
        key = lst[i]
        j = i - 1
        # Сдвиг элементов списка lst[left:right+1], которые больше ключа, на одну позицию вправо
        while j >= left and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        # Вставка ключа в правильное место
        lst[j + 1] = key


def merge(lst, l, m, r):
    """
    Слияние двух отсортированных подмассивов lst[l:m+1] и lst[m+1:r+1].

    Аргументы:
    lst -- список чисел для сортировки
    l -- начальный индекс первого подмассива
    m -- конечный индекс первого подмассива и начальный индекс второго подмассива
    r -- конечный индекс второго подмассива
    """
    # Создание временных подсписков для левой и правой половины
    left = lst[l:m + 1]
    right = lst[m + 1:r + 1]
    i = j = 0
    k = l

    # Объединение временных подсписков обратно в lst[l:r+1]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    # Копирование оставшихся элементов левой половины (если есть)
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    # Копирование оставшихся элементов правой половины (если есть)
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1


def timsort(lst):
    """
    Основная функция сортировки Тимсорт.

    Аргументы:
    lst -- список чисел для сортировки
    """
    n = len(lst)
    # Разделение списка на подсписки длиной MIN_RUN и сортировка каждого из них сортировкой вставками
    for i in range(0, n, MIN_RUN):
        insertion_sort(lst, i, min(i + MIN_RUN - 1, n - 1))

    size = MIN_RUN
    # Объединение отсортированных подсписков с увеличением размера подсписков в два раза на каждой итерации
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n - 1, start + size - 1)
            end = min(n - 1, start + size * 2 - 1)
            if mid < end:
                merge(lst, start, mid, end)
        size *= 2


if __name__ == '__main__':
    unsorted_list = [25, 21, 22, 24, 23, 27, 26]

    sorted_list = timsort(unsorted_list)
    print(sorted_list)  # Вывод: [21, 22, 23, 24, 25, 26, 27]
