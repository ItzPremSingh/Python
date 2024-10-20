class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tIndex = 0
        sIndex = 0
        tLen = len(t)
        sLen = len(s) - 1

        if sLen < 0:
            return True

        if tLen < 1:
            return False

        while tIndex < tLen:
            if t[tIndex] == s[sIndex]:
                if sIndex == sLen:
                    return True

                sIndex += 1

            tIndex += 1

        return False


print(Solution().isSubsequence("abc", "ahbgdc"))
