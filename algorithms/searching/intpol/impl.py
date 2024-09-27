def interpolation_search(lst, x):
    """
    Функция интерполяционного поиска.

    Аргументы:
    lst -- упорядоченный список для поиска.
    x -- искомый элемент.

    Возвращает:
    True, если элемент найден, иначе False.
    """
    # Устанавливаем начальные границы поиска
    idx0 = 0
    idxn = len(lst) - 1
    found = False

    # Пока границы не пересеклись и элемент x находится в диапазоне текущего подсписка
    while idx0 <= idxn and x >= lst[idx0] and x <= lst[idxn]:
        # Вычисляем предполагаемую позицию элемента x
        mid = idx0 + int(((float(idxn - idx0) / (lst[idxn] - lst[idx0])) * (x - lst[idx0])))

        # Сравниваем элемент в предполагаемой позиции с искомым элементом x
        if lst[mid] == x:
            found = True
            return found
        if lst[mid] < x:
            # Если искомый элемент больше, смещаем нижнюю границу
            idx0 = mid + 1
        else:
            # Если искомый элемент меньше, смещаем верхнюю границу
            idxn = mid - 1

    return found



if __name__ == '__main__':
    sorted_list = [21, 22, 23, 24, 25, 26, 27]
    search_item = 23

    result = interpolation_search(sorted_list, search_item)
    print(result) # Вывод: True
