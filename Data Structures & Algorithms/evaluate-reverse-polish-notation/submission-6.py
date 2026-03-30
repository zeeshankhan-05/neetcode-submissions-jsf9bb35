class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for token in tokens:
            if token in "+-*/":
                b = nums.pop()
                a = nums.pop()

                if token == "+":
                    result = a + b
                    nums.append(result)
                elif token == "-":
                    result = a - b
                    nums.append(result)
                elif token == "*":
                    result = a * b
                    nums.append(result)
                elif token == "/":
                    result = int(a / b)
                    nums.append(result)
            else:
                nums.append(int(token))
        
        return nums[0]