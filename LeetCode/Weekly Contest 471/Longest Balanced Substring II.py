class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        maxi, cur = 1, 1

        def help(c1, c2, skip):
            max_len = 0
            i = 0

            while i < n:
                while i < n and s[i] == skip:
                    i += 1
                if i >= n:
                    break

                p = i
                while i < n and s[i] != skip:
                    i += 1
                q = i - 1

                x = y = 0
                mpp = {0: p - 1}

                for j in range(p, q + 1):
                    ch = s[j]
                    if ch == c1:
                        x += 1
                    elif ch == c2:
                        y += 1

                    key = x - y
                    if key in mpp:
                        max_len = max(max_len, j - mpp[key])
                    else:
                        mpp[key] = j

            return max_len

        # this loop is only for one char
        for i in range(1, n):

            if s[i] == s[i - 1]:
                cur += 1
            else:
                cur = 1

            maxi = max(maxi, cur)


        # now for three chars
        mpp = {}
        mpp[(0, 0)] = -1

        a, b, c = 0, 0, 0

        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else: c += 1


            diff1 = a - b
            diff2 = a - c
            key = (diff1, diff2)

            if key in mpp:
                maxi = max(maxi, i - mpp[key])
            else:
                mpp[key] = i

        maxi = max(maxi, help('a', 'b', 'c'))
        maxi = max(maxi, help('a', 'c', 'b'))
        maxi = max(maxi, help('b', 'c', 'a'))
        return maxi