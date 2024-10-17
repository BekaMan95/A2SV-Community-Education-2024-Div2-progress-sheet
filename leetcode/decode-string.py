class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                sub, digit = '', ''
                while stack and stack[-1] != '[':
                    sub = stack.pop() + sub
                if stack and stack[-1] == '[':
                    stack.pop()
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                if digit:
                    stack.append(sub * int(digit))
                else:
                    stack.append(sub)
            else:
                stack.append(c)

        return ''.join(stack)
