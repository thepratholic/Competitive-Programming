class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        while s and s[-1] in vowels:
                s.pop()

        return "".join(s)