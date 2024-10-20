class Solution:
    def reverseString(self, s: list[str]) -> None:
        stringLen = len(s)
        index = 0

        while index < stringLen // 2:
            start = s[index]
            end = s[-(index + 1)]

            s[-(index + 1)] = start
            s[index] = end

            index += 1


Solution().reverseString(list("hello"))
