from collections import defaultdict

class Solution:
    def maxSubstrings(self, word: str) -> int:
        pos = defaultdict(list)

        for i, ch in enumerate(word):
            pos[ch].append(i)

        candidates = []

        for indices in pos.values():
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    start = indices[i]
                    end = indices[j]
                    if end - start + 1 >= 4:
                        candidates.append((start, end))
                        break 

        candidates.sort(key=lambda x: x[1])

        ans = 0
        last_end = -1
        for start, end in candidates:
            if start > last_end:
                ans += 1
                last_end = end

        return ans
