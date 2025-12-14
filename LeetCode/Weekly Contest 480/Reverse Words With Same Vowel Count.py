class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)

        vowels = {'a', 'e', 'i', 'o', 'u'}

        strs = s.split(" ")

        def countVowels(s):
            cnt = 0
            for ch in s:
                if ch in vowels: cnt += 1

            return cnt

        ans = ""
        first_word_vowels = countVowels(strs[0])
        for i in range(1, len(strs)):
            cnt_vowels = countVowels(strs[i])
            if cnt_vowels == first_word_vowels:
                strs[i] = strs[i][::-1]

        return " ".join(strs)