class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, count = 0, defaultdict(int)
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len
