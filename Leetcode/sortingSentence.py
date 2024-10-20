class Solution:
    def sortSentence(self, s: str) -> str:
        sList = s.split(" ")
        stringIndex = {}

        for string in sList:
            _string = ""
            index = ""

            for char in string:
                if not char.isdigit():
                    _string += char
                    continue

                index += char

            stringIndex.setdefault(index, _string)

        return " ".join([stringIndex[i.__str__()] for i in range(1, len(sList) + 1)])


print(Solution().sortSentence("Myself2 Me1 I4 and3"))
