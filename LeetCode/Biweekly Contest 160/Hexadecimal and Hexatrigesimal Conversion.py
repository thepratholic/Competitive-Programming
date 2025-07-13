class Solution:
    def convert(self, n, base, symbols):
        if n == 0:
            return "0"

        d = []
        while n > 0:
            d.append(symbols[n % base])
            n //= base

        return "".join(reversed(d))

    def concatHex36(self, n: int) -> str:
        hexa = "0123456789ABCDEF"
        hexa_tri = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        nsq = n ** 2
        ncu = n ** 3

        ans1 = self.convert(nsq, 16, hexa)
        ans2 = self.convert(ncu, 36, hexa_tri)

        return ans1 + ans2