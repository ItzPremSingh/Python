def sort(list1: list[int], list2: list[int]) -> list[int]:
    insertIndex = 0
    index = 0

    for element in list2:
        if list1[index] < element:
            insertIndex += 1

        list1.insert(insertIndex, element)
        insertIndex += 1

    return list1


print(sort([1, 4, 8], [2, 3, 5]))
