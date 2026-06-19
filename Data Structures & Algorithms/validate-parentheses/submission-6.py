class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Create a hashmap that maps the braces together
        # 2. Iterate through the string
        # 3. Check if the character is a closing brace
            # If it is, check if the top of the stack is equal to the
            # corresponding type of the closing brace
                # If it is, pop from the stack
                # Return False
            # Append to the stack
        # 4. If the stack is empty, return True. Return False if not

        close_to_open = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack