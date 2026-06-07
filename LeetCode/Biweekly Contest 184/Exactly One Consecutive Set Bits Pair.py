class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        l = list(bin(n)[2:])
        cnt = 0
        for i in range(len(l) - 1):
            if l[i] == '1' and l[i + 1] == '1':
                cnt += 1

        return cnt == 1