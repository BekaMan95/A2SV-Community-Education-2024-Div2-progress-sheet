class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) <= len(s):
            t_count, s_count = defaultdict(int), defaultdict(int)
            for c in t:
                t_count[c] += 1
            have, need = 0, len(t_count)
            l, a, b = 0, 0, len(s)
            for r in range(len(s)):
                s_count[s[r]] += 1
                if s_count[s[r]] == t_count[s[r]]:
                    have += 1
                while have == need:
                    if r-l < b-a:
                        a, b = l, r
                    s_count[s[l]] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        have -= 1
                    l += 1
            if b < len(s):
                return s[a:b+1]
        return ''
