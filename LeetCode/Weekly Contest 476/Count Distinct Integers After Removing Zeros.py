class Solution:
    def countDistinct(self, n: int) -> int:
        n += 1
        n = str(n)

        ans = sum(9 ** i for i in range(1, len(n)))

        for i in range(len(n)):
            if n[i] == '0': break

            ans += (int(n[i]) - 1) * (9 ** (len(n) - i - 1))

        return ans