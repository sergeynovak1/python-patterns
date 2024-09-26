def shell_sort(lst):
    """
    Функция сортировки Шелла.

    Аргументы:
    lst -- список чисел для сортировки.

    Возвращает:
    Сортированный список.
    """
    n = len(lst)
    gap = n // 2

    # Начало сортировки с различными промежутками
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            # Сортировка элементов, находящихся на расстоянии gap
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        # Уменьшение промежутка
        gap //= 2

    return lst


if __name__ == '__main__':
    unsorted_list = [25, 21, 22, 24, 23, 27, 26]

    sorted_list = shell_sort(unsorted_list)
    print(sorted_list)  # Вывод: [21, 22, 23, 24, 25, 26, 27]