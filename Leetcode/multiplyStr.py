def atoi(number: str) -> int:
    intOrd = {48: 0, 49: 1, 50: 2, 51: 3, 52: 4, 53: 5, 54: 6, 55: 7, 56: 8, 57: 9}

    realInt = 0
    numLen = len(number) - 1

    for _int in number:
        num = intOrd[ord(_int)]
        realInt += 10**numLen * num

        numLen -= 1

    return realInt


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(atoi(num1) * atoi(num2))


print(Solution().multiply("10", "5"))
