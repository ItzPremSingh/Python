__list = [3, 2, 4]


def sum(__list: list[int], target: int) -> list[int] | None:
    listLen = len(__list)

    for i in range(listLen):
        for j in range(listLen):
            if __list[i] + __list[j] == target and i != j:
                return [i, j]


print(sum(__list, 6))
