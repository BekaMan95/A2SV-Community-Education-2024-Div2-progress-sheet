class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if not c.isdigit() and len(c) == 1:
                b, a = stack.pop(), stack.pop()
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(a - b)
                elif c == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(c))
        return stack[0]
