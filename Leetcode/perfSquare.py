def factor(number: int) -> list[int]:
    divisor = 3
    factors = []

    while number % 2 == 0:
        number //= 2
        factors.append(2)

    while number > 1:
        if number % divisor != 0:
            divisor += 2

        else:
            number //= divisor
            factors.append(divisor)

    return factors


def isPerfectSquare(number: int) -> bool:
    numberFactor = factor(number)
    factorLen = numberFactor.__len__()

    if factorLen % 2 != 0:
        return False

    index = 0

    for _ in range(factorLen // 2):
        if numberFactor[index] != numberFactor[index + 1]:
            return False

        index += 2

    return True


print(isPerfectSquare(2000105819))
