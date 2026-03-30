class Solution:
    def isValid(self, s: str) -> bool:
        closeOpen = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in closeOpen.values():
                stack.append(char)
            elif char in closeOpen:
                if not stack or stack.pop() != closeOpen[char]:
                    return False
            else:
                return False

        return not stack