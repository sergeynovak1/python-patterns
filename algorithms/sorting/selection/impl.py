def selection_sort(lst):
    """
    Функция сортировки выбором.

    Аргументы:
    lst -- список чисел для сортировки.

    Возвращает:
    Сортированный список.
    """
    for fill_slot in range(len(lst) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if lst[location] > lst[max_index]:
                max_index = location
        # Меняем местами максимальный элемент и элемент в текущей позиции fill_slot
        lst[fill_slot], lst[max_index] = lst[max_index], lst[fill_slot]
    return lst


if __name__ == '__main__':
    unsorted_list = [25, 21, 22, 24, 23, 27, 26]

    sorted_list = selection_sort(unsorted_list)
    print(sorted_list)  # Вывод: [21, 22, 23, 24, 25, 26, 27]