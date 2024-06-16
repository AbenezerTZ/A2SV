class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                first_item = stack[-1]
                if first_item == "(":
                    stack.pop()
                    
                    if len(stack) > 0 and isinstance(stack[-1], int):
                        new_item = 1 + stack.pop()
                        stack.append(new_item)
                    else:
                        stack.append(1)
                elif isinstance(first_item, int):
                    stack.pop()
                    stack.pop()
                    if len(stack) > 0 and isinstance(stack[-1], int):
                        new_item = (2 * first_item) + stack.pop()
                        stack.append(new_item)
                    else:
                        stack.append(2 * first_item)
        return stack[0]        