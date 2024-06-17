class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, count, cache = 0, defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            cache[s1[i]] += 1
            if i != len(s1)-1:
                count[s2[i]] += 1
        for r in range(len(s1)-1, len(s2)):
            count[s2[r]] += 1
            if count == cache:
                return True
            if count[s2[l]] == 1:
                del count[s2[l]]
            else:
                count[s2[l]] -= 1
            l += 1
        return False
