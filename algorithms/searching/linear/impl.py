def linear_search(lst, item):
    """
    Функция линейного поиска.

    Аргументы:
    lst -- список для поиска.
    item -- искомый элемент.

    Возвращает:
    True, если элемент найден, иначе False.
    """
    index = 0
    found = False

    # Сравниваем значение с каждым элементом данных
    while index < len(lst) and not found:
        if lst[index] == item:
            found = True
        else:
            index += 1

    return found


if __name__ == '__main__':
    sample_list = [25, 21, 22, 24, 23, 27, 26]
    search_item = 23

    result = linear_search(sample_list, search_item)
    print(result) # Вывод: True
