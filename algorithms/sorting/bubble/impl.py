def bubble_sort(lst):
    """
    Функция сортировки пузырьком.

    Аргументы:
    lst -- список чисел для сортировки.

    Возвращает:
    Сортированный список.
    """
    # Индекс последнего элемента списка
    last_element_index = len(lst) - 1

    # Внешний цикл - проходы по списку
    for pass_no in range(last_element_index, 0, -1):
        # Внутренний цикл - сравнение соседних элементов
        for idx in range(pass_no):
            if lst[idx] > lst[idx + 1]:
                # Обмен элементов местами, если текущий элемент больше следующего
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
    return lst


if __name__ == '__main__':
    unsorted_list = [25, 21, 22, 24, 23, 27, 26]

    sorted_list = bubble_sort(unsorted_list)
    print(sorted_list) # Вывод: [21, 22, 23, 24, 25, 26, 27]

