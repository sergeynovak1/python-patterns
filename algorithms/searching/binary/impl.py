def binary_search(lst, item):
    """
    Функция бинарного поиска.

    Аргументы:
    lst -- упорядоченный список для поиска.
    item -- искомый элемент.

    Возвращает:
    True, если элемент найден, иначе False.
    """
    # Устанавливаем начальные границы поиска
    first = 0
    last = len(lst) - 1
    found = False

    # Пока границы не пересеклись и элемент не найден
    while first <= last and not found:
        # Определяем средний элемент
        midpoint = (first + last) // 2
        # Если средний элемент равен искомому, то мы нашли элемент
        if lst[midpoint] == item:
            found = True
        else:
            # Если искомый элемент меньше среднего, сдвигаем верхнюю границу
            if item < lst[midpoint]:
                last = midpoint - 1
            # Если искомый элемент больше среднего, сдвигаем нижнюю границу
            else:
                first = midpoint + 1

    return found


if __name__ == '__main__':
    sorted_list = [21, 22, 23, 24, 25, 26, 27]
    search_item = 23

    result = binary_search(sorted_list, search_item)
    print(result) # Вывод: True
