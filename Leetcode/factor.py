def factor(number: int) -> list[int]:
    _factor = []
    divisor = 2
    while number >= 1:
        if number % divisor != 0:
            divisor += 1

        number /= divisor
        _factor.append(divisor)

    return _factor


print(factor(10))
