class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        freq = {}
        first = {}

        for i, ch in enumerate(s):
            if ch in vowels:
                freq[ch] = freq.get(ch, 0) + 1
                if ch not in first:
                    first[ch] = i


        order = sorted(freq.keys(), key = lambda x : (-freq[x], first[x]))

        a = []
        for ch in order:
            a.extend(ch * freq[ch])

        ans = list(s)
        j = 0

        for i in range(len(ans)):
            if ans[i] in vowels:
                ans[i] = a[j]
                j += 1

        return "".join(ans)