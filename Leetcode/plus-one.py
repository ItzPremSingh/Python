def plusOne(digit: list[int]) -> list[int]:
    strDigit = [str(n) for n in digit]
    strDigit = "".join(strDigit)

    intDigit = int(strDigit) + 1
    listDigit = [int(n) for n in str(intDigit)]

    return listDigit


def plusOneSlow(digit: list[int]) -> list[int]:
    digitLen = len(digit)

    for index in range(1, digitLen + 1):
        lastDigitOne = digit[-index] + 1
        digit[-index] = lastDigitOne

        if lastDigitOne < 10:
            return digit

        else:
            digit[-index] = 0

    if digit[0] == 0:
        digit.insert(0, 1)

    return digit


def plusOneFast(digit: list[int]) -> list[int]:
    digit = digit[::-1]
    digitLen = len(digit)

    for index in range(digitLen):
        lastDigitOne = digit[index] + 1
        digit[index] = lastDigitOne

        if lastDigitOne < 10:
            return digit[::-1]

        else:
            digit[index] = 0

    if digit[-1] == 0:
        digit.append(1)

    return digit[::-1]
