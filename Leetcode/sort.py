from timeit import timeit

__list = [element for element in range(1000)]


def isOdd(number: int) -> bool:
    if number % 2 != 0:
        return True
    return False


def isEven(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


def sorterO(__list: list) -> list:
    for index in range(len(__list)):
        element = __list[index]
        if isOdd(element):
            __list.pop(index)
            __list.append(element)

    return __list


def sorterE(__list: list) -> list:
    for index in range(len(__list)):
        element = __list[index]
        if isEven(element):
            __list.pop(index)
            __list.insert(0, element)

    return __list


print(timeit(stmt="sorterO(__list)", globals=globals(), number=10000))
print(timeit(stmt="sorterE(__list)", globals=globals(), number=10000))
