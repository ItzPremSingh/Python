roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

combine = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

# I: V and X, 4 and 9
# X: L and C, 40 and 90
# C: D and M, 400 and 900


def romanToInt(__str: str) -> int:
    number = 0
    strLen = len(__str)
    index = 0

    while index < strLen:
        if index < strLen:
            comb = __str[index : index + 2]
            if comb in combine:
                number += combine[comb]

            else:
                number += roman[__str[index]]

        index += 1

    return number


print(romanToInt("MCMXCIV"))
