def addDigit(digit: int) -> int:
    if digit < 10:
        return digit

    _sum = sum([int(number) for number in str(digit)])
    return addDigit(_sum)


print(addDigit(10))
