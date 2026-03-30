class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        num_stack = []
        decoded_string = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == "[":
                string_stack.append(decoded_string)
                num_stack.append(k)
                decoded_string = ""
                k = 0
            elif char == "]":
                repeat_count = num_stack.pop()
                prev_str = string_stack.pop()
                decoded_string = prev_str + repeat_count * decoded_string
            else:
                decoded_string += char

        return decoded_string