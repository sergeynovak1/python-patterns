def insertion_sort(lst):
    """
    Функция сортировки вставками.

    Аргументы:
    lst -- список чисел для сортировки.

    Возвращает:
    Сортированный список.
    """
    # Проходим по списку начиная со второго элемента
    for i in range(1, len(lst)):
        # Элемент, который будет перемещаться в отсортированную часть списка
        next_element = lst[i]
        # Индекс предыдущего элемента
        j = i - 1

        # Перемещение элементов списка, которые больше next_element, на одну позицию вправо
        while j >= 0 and lst[j] > next_element:
            lst[j + 1] = lst[j]
            j -= 1

        # Вставка next_element на его правильное место
        lst[j + 1] = next_element

    return lst


if __name__ == '__main__':
    unsorted_list = [25, 21, 22, 24, 23, 27, 26]

    sorted_list = insertion_sort(unsorted_list)
    print(sorted_list) # Вывод: [21, 22, 23, 24, 25, 26, 27]