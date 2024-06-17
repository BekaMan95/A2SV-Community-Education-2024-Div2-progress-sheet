class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l, max_len, count = 0, 0, defaultdict(int)
        for r in range(len(answerKey)):
            count[answerKey[r]] += 1
            while min(count['T'], count['F']) > k:
                count[answerKey[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len
