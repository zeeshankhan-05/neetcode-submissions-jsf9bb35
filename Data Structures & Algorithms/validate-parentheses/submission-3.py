class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_braces = {")" : "(", "}" : "{", "]" : "["}

        for char in s:
            if char in close_open_braces:
                if stack and stack[-1] == close_open_braces[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        
        return True