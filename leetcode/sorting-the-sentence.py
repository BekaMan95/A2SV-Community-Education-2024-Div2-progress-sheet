class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join([t for _, t in sorted([[int(word[-1]), word[:-1]] for word in s.split(' ')])])
