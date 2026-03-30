class Solution:
    def isValid(self, s: str) -> bool:
        braces = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for char in s:
            if char not in braces:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != braces[char]:
                        return False
        
        return not stack