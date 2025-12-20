from collections import deque
from typing import Counter, List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        q = deque(nums)

        freq = Counter(nums)

        ans = 0
        if len(freq) == n:
            return 0

            
        while len(q) >= 3:
            f = q.popleft()
            s = q.popleft()
            t = q.popleft()

            freq[f] -= 1
            if freq[f] == 0: del freq[f]
            freq[s] -= 1
            if freq[s] == 0: del freq[s]
            freq[t] -= 1
            if freq[t] == 0: del freq[t]
            ans += 1

            if len(freq) == len(q):
                return ans

        while q:
            v = q.popleft()
            freq[v] -= 1
            ans += 1
            if freq[v] == 0: del freq[v]
            if len(freq) == len(q):
                return ans
        return ans