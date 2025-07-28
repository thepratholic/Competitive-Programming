class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        prefix_l, suffix_t = [0] * n, [0] * n

        prefix_l[0] = 1 if s[0] == 'L' else 0
        for i in range(1, n):
            prefix_l[i] += prefix_l[i - 1]
            if s[i] == 'L':
                prefix_l[i] += 1

        suffix_t[n - 1] = 1 if s[n - 1] == 'T' else 0
        for i in range(n - 2, -1, -1):
            suffix_t[i] += suffix_t[i + 1]
            if s[i] == 'T':
                suffix_t[i] += 1

        ans, best, ansl, anst = 0, 0, 0, 0

        for i in range(n):
            p = prefix_l[i - 1] if i > 0 else 0
            suf = suffix_t[i + 1] if i + 1 < n else 0

            if s[i] == 'C':
                ans += p * suf
                ansl += (p + 1) * suf
                anst += p * (suf + 1)

            p = prefix_l[i]
            best = max(best, p * suf)

        return max(ans + best, ansl, anst)