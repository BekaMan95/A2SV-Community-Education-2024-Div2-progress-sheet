class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, directories = [], [name for name in path.split('/') if name]
        for name in directories:
            if name == '.':
                continue
            elif name == '..':
                if stack: stack.pop()
            else:
                stack.append(name)
        return '/' + '/'.join(stack)
