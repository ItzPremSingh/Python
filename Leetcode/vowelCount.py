def subString(string: str) -> list[str]:
    def _subString(string: str) -> list[str]:
        start = 0
        count = 1
        _list = []
        strLen = len(string) + 1

        while count < strLen:
            _list.append(string[start:count])
            count += 1

        return _list

    _list = []
    index = 0
    strlen = len(string) - 1

    while index < strlen:
        _list.append(_subString(string[index:]))
        index += 1

    return _list


print(subString("aba"))


class Solution:
    def vowelsCount(self, string: str) -> int:
        return 0


print(Solution().vowelsCount("abc"))
