from collections import defaultdict
from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        n = len(responses)

        d = defaultdict(int)

        for i in range(n):
            s = set(responses[i])
            for k in s:
                d[k] += 1


        ans = ""
        freq = float("-inf")
        for k, v in d.items():
            if v > freq:
                freq = max(freq, v)
                ans = k

            elif v == freq:
                if k < ans:
                    ans = k

        return ans
