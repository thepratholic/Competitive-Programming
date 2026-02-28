from typing import Counter, DefaultDict


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        n = len(nums)
        freq = Counter(nums)

        ans = [-1, -1]

        if len(set(freq.values())) < 2:
            return ans


        mpp = DefaultDict(list)

        for k, v in freq.items():
            mpp[v].append(k)

        for f in mpp:
            mpp[f].sort()

        vals = sorted(freq.keys())
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                if freq[vals[i]] != freq[vals[j]]:
                    return [vals[i], vals[j]]

        return ans