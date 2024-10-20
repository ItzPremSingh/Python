# divisible by 3, 5 and 7


def sumOfMuliple(number: int) -> int:
    if number < 3:
        return 0

    _sum = 0
    for num in range(3, number + 1):
        if num % 3 == 0:
            _sum += num

        elif num % 5 == 0:
            _sum += num

        elif num % 7 == 0:
            _sum += num

    return _sum


print(sumOfMuliple(9))
