class Solution:
    def myAtoti(self, s: str) -> float:
        number = ""
        sign = 1

        for char in s:
            if char.isdigit() or char == ".":
                number += char

            elif char == "-":
                sign = -1

        return float(number) * sign


print(Solution().myAtoti("-004193 with words"))
