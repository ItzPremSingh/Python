class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start < end:
            sWord = s[start]
            lWord = s[end]

            if not sWord.isalpha():
                start += 1
                continue

            if not lWord.isalpha():
                end -= 1
                continue

            if sWord != lWord:
                return False

            start += 1
            end -= 1

        return True


print(Solution().isPalindrome("0P"))
