class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sLen = s.__len__()
        longest = ""
        for i in range(sLen):
            for j in range(i + 1, sLen + 1):
                substring = s[i:j]
                if substring.__len__() > longest.__len__():
                    longest = substring

        return longest.__len__()


print(Solution().lengthOfLongestSubstring("abcabcbb"))
