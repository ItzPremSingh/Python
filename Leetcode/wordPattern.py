class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(" ")
        _dict = {}
        index = 0

        for char in pattern:
            if word[index] in _dict:
                if _dict[word[index]] != char:
                    return False

            else:
                _dict[word[index]] = char

            index += 1
            print(_dict)

        return True


print(Solution().wordPattern("abba", "dog cat cat fish"))
