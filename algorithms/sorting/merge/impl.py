def merge_sort(lst):
    """
    Функция сортировки слиянием.

    Аргументы:
    lst -- список чисел для сортировки.

    Возвращает:
    Сортированный список.
    """
    if len(lst) > 1:
        # Находим середину списка
        mid = len(lst) // 2
        # Делим список на две половины
        left = lst[:mid]
        right = lst[mid:]

        # Рекурсивно сортируем каждую половину
        merge_sort(left)
        merge_sort(right)

        a = b = c = 0

        # Объединяем отсортированные половины
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                lst[c] = left[a]
                a += 1
            else:
                lst[c] = right[b]
                b += 1
            c += 1

        # Собираем оставшиеся элементы
        while a < len(left):
            lst[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            lst[c] = right[b]
            b += 1
            c += 1

    return lst

if __name__ == '__main__':
    unsorted_list = [25, 21, 22, 24, 23, 27, 26]

    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)  # Вывод: [21, 22, 23, 24, 25, 26, 27]