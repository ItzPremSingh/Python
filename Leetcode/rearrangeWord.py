class Solution:
    def arrangeWords(self, text: str) -> str:
        stext = text.split(" ")
        stext.sort(key=len)
        return " ".join(stext).capitalize()


print(Solution().arrangeWords("Keep calm and code on"))
