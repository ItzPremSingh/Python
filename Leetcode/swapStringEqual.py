class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1[::-1] == s2 or s1 == s2:
            return True

        return False


print(Solution().areAlmostEqual("prem", "merp"))
