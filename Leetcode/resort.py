def isEven(number: int) -> bool:
    if number % 2 == 0:
        return True

    return False


def reorder(data: list[int]) -> None:
    even = 0
    odd = len(data) - 1

    while (odd - even) != 1:
        if isEven(data[even]):
            even += 1

        else:
            atEven = data[even]
            data[even] = data[odd]
            data[odd] = atEven
            odd -= 1


__list = [i for i in range(1000)]
reorder(__list)
print(__list)
