class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"(": ")", "{": "}", "[": "]"}
        paren = []

        for char in s:
            if char in {"(", "{", "["}:
                paren.append(char)

            elif paren:
                if closing[paren.pop()] != char:
                    return False

            else:
                return False

        return not paren.__len__()


print(
    Solution().isValid(
        "{{{{{{{{{{{{{{{{{{[[[[[[[[[[[(((((((((((((((())))))))))))))))]]]]]]]]]]]}}}}}}}}}}}}}}}}}}"
    )
)
