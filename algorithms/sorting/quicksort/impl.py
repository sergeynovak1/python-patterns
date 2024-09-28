def quick_sort(arr):
    """
    Основная функция быстрой сортировки.

    Аргументы:
    arr -- список чисел для сортировки.

    Возвращает:
    Отсортированный список.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Опорный элемент
        left = [x for x in arr if x < pivot]  # Элементы меньше опорного
        middle = [x for x in arr if x == pivot]  # Элементы равные опорному
        right = [x for x in arr if x > pivot]  # Элементы больше опорного
        return quick_sort(left) + middle + quick_sort(right)  # Рекурсивный вызов для левой и правой части


if __name__ == '__main__':
    unsorted_list = [25, 21, 22, 24, 23, 27, 26]

    sorted_list = quick_sort(unsorted_list)
    print(sorted_list)  # Вывод: [21, 22, 23, 24, 25, 26, 27]