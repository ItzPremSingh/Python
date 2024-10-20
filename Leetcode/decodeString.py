class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = 0
        currenrStr = ""

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)

            elif char == "[":
                stack.append((currenrStr, number))
                number, currenrStr = 0, ""

            elif char == "]":
                lastStr, num = stack.pop()
                currenrStr = lastStr + num * currenrStr

            else:
                currenrStr += char

        return currenrStr


print(Solution().decodeString("10[ab12[cd]ef2[g]]"))
