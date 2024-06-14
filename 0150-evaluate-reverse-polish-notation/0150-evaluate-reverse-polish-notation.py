class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    result = num2 + num1
                elif token == "-":
                    result = num2 - num1
                elif token == "*":
                    result = num2 * num1
                else:  # token == "/"
                    result = int(num2 / num1)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]
