class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels, max_vowel, count = 'aeiou', 0, 0
        l = 0
        for i in range(k-1):
            if s[i] in vowels:
                count += 1
        for r in range(k-1, len(s)):
            if s[r] in vowels:
                count += 1
            max_vowel = max(max_vowel, count)
            if s[l] in vowels:
                count -= 1
            l += 1
        return max_vowel
