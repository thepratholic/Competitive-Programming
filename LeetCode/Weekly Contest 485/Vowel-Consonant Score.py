class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        v, c = 0, 0

        for i in range(n):
            if s[i] in vowels:
                v += 1

            elif s[i].isalpha() and s[i] not in vowels:
                c += 1

        if c > 0:
            return v // c
        return 0