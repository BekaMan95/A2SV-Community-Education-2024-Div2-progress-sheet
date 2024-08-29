class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == ')':
                score = 0
                while stack and stack[-1] != '(':
                    score += stack.pop()
                stack.pop()
                if score: stack.append(2 * score)
                else: stack.append(1)
            else:
                stack.append(c)
        return sum(stack)
