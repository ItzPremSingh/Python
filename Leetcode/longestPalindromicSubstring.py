def isPalindromic(s):
    start, end = 0, s.__len__() - 1

    while start <= end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if isPalindromic(substring) and len(longest) < len(substring):
                    longest = substring

        return longest


print(Solution().longestPalindrome("cfhsbab"))
