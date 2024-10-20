class Solution:
    def reverseOnlyLetters(self, string: str) -> str:
        letter = set("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        start = 0
        last = len(string) - 1
        s = list(string)

        while start < last:
            sWord = s[start]
            lWord = s[last]

            if sWord in letter and lWord in letter:
                s[start] = lWord
                s[last] = sWord

            else:
                if lWord not in letter:
                    last -= 1

                else:
                    start += 1

                continue

            last -= 1
            start += 1

        return "".join(s)


print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))
