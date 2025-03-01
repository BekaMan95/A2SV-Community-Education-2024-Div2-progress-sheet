class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(idx: int, address: list):
            if idx == len(s):
                if len(address) == 4:
                    res.append('.'.join(address))
                return
            
            for i in range(idx, len(s)):
                if int(s[idx:i+1]) < 256 and str(int(s[idx:i+1])) == s[idx:i+1]:
                    address.append(s[idx:i+1])
                    dfs(i+1, address)
                    address.pop()

        res = list()

        dfs(0, [])

        return res
