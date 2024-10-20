class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minLen = len(min(strs, key=len))

        if minLen <= 0:
            return ""

        common = strs[0][0]

        for index in range(1, minLen + 1):
            for word in strs:
                w = word[:index]
                if w != common:
                    print(common)
                    return common[:-1]

            common = w

        return common


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
