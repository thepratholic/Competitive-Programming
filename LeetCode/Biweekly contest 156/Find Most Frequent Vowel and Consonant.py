from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = defaultdict(int)

        vowels = set(['a', 'e', 'i', 'o', 'u'])

        max_vowel = 0
        max_consonant = 0

        for i in s:
            freq[i] += 1

        for k, v in freq.items():
            if k in vowels:
                max_vowel = max(max_vowel, v)
            else:
                max_consonant = max(max_consonant, v)

        return max_vowel + max_consonant