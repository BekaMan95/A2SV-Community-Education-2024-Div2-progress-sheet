class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(idx: int, splits: list):
            if idx == len(s):
                return True if len(splits) > 1 else False
            
            res = False

            for i in range(idx, len(s)):
                if not splits:
                    splits.append(int(s[idx:i+1]))
                    res |= dfs(i+1, splits)
                    splits.pop()
                else:
                    if splits[-1] - 1 == int(s[idx:i+1]):
                        splits.append(int(s[idx:i+1]))
                        res |= dfs(i+1, splits)
                        splits.pop()
            
            return res

        return dfs(0, [])
