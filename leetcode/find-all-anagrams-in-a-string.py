class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        out, count, check = [], defaultdict(int), defaultdict(int)
        for c in p:
            check[c] += 1
        for i in range(len(p)-1):
            count[s[i]] += 1
        l = 0
        for r in range(len(p)-1, len(s)):
            count[s[r]] += 1
            if count == check:
                out.append(l)
            if count[s[l]] == 1:
                del count[s[l]]
            else:
                count[s[l]] -= 1
            l += 1
        return out
