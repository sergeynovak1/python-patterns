def BinarySearch(list, item):
    first = 0
    last = len(list) - 1
    found = False


    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


if __name__ == '__main__':
    unsorted_list = [21, 22, 23, 24, 25, 26, 27]
    sorted_list = BinarySearch(unsorted_list, 252)
    print(sorted_list)
