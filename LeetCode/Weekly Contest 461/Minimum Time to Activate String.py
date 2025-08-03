from typing import List


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)

        def f(mid):
            st = list(s)
            for i in range(mid):
                st[order[i]] = "*"

            total = 0
            count = 0
            for ch in st:
                if ch == '*':
                    total += (count * (count + 1)) // 2
                    count = 0
                else:
                    count += 1
            if count > 0:
                total += (count * (count + 1)) // 2

            invalid = total

            all_substrings = n * (n + 1) // 2
            valid = all_substrings - invalid

            return valid >= k

            
        low, high = 0, n

        ans = -1
        while low <= high:
            mid = (low + high) >> 1

            if f(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans - 1 if ans != -1 else ans