class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses = []
        closing_to_opening = {")" : "(", "}" : "{", "]" : "["}
        
        for char in s:
            if char in closing_to_opening:
                if valid_parentheses and valid_parentheses[-1] == closing_to_opening[char]:
                    valid_parentheses.pop()
                else:
                    return False
            else:
                valid_parentheses.append(char)
        
        return True if not valid_parentheses else False