class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phoneNumber = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        wordList = []
        letterList = [phoneNumber[integer] for integer in digits]
        letterLen = len("".join(letterList))

        index = 0
        runTime = 1
        while runTime < letterLen:
            wordList.append(word[index])

        return wordList


print(Solution().letterCombinations("23"))
