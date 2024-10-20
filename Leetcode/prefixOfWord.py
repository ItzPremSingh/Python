class Solution:
    def isPrefixOfWord(self, sentence: str, wordsearch: str) -> int:
        for index, word in enumerate(sentence.split(" ")):
            if word.startswith(wordsearch):
                return index + 1
        return -1


print(Solution().isPrefixOfWord("i love eating burger", "burg"))
