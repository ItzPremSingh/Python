class Solution:
    def numDecodings(self, number: str) -> int:
        if number[0] == "0":
            return 0

        index = 1
        numberLen = len(number)
        lastNumber = int(number[0])
        totalLen = 1

        while index < numberLen:
            integer = int(number[index])
            if lastNumber < 3 and lastNumber > 0:
                integer = lastNumber * 10 + int(number[index])
                if integer < 27 and integer > 0:
                    totalLen += 1

                totalLen += 1

            lastNumber = integer

            index += 1

        return totalLen


print(Solution().numDecodings("26"))
