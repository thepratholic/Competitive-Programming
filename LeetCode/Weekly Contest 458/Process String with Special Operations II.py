class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        length = 0

        for c in s:
            if c.islower():
                length += 1

            elif c == '*' and length > 0:
                length -= 1

            elif c == '#':
                length *= 2

            
        if k >= length:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            if ch.islower():
                if k == length - 1:
                    return ch
                length -= 1

            elif ch == '*':
                length += 1

            elif ch == '#':
                length //= 2

                if k >= length:
                    k -= length

            elif ch == '%':
                k = length - 1 - k

        return '.'