class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ['?'] * n

        cnt = [0] * 26

        for i in s:
            cnt[ord(i) - ord('a')] += 1

        # middle element
        for i in range(26):
            if cnt[i] & 1:
                ans[n // 2] = chr(ord('a') + i)
                break

        for k in range(26):
            cnt[k] //= 2

        j = 0
        for i in range(26):
            while cnt[i] > 0:
                ans[j] = ans[n - j - 1] = chr(ord('a') + i)
                cnt[i] -= 1
                j += 1

        return "".join(ans)
        