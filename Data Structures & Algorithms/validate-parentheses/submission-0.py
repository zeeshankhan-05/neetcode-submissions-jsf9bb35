class Solution:
    def isValid(self, s: str) -> bool:
        opener = ["(", "{", "["]
        closer = [")", "}", "]"]
        stack = []

        for char in s:
            if char in opener:
                stack.append(char)
            else:
                if not stack or opener.index(stack[-1]) != closer.index(char):
                    return False
                else:
                    stack.pop()

        return not stack