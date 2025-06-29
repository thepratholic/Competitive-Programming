from typing import List
from collections import Counter


class Solution:
    def longest_common_prefix(self, a, b):
        i = 0
        while i < min(len(a), len(b)) and a[i] == b[i]:
            i += 1
        return i
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n == 1:
            return [0]
    
        lcp = [0] * (n - 1)
        for i in range(n - 1):
            lcp[i] = self.longest_common_prefix(words[i], words[i + 1])
    
        lcp_counter = Counter(lcp)
        max_lcp = max(lcp_counter)
    
        answer = []
    
        for i in range(n):
            removed = []
    
            if i > 0:
                l = lcp[i - 1]
                lcp_counter[l] -= 1
                if lcp_counter[l] == 0 and l == max_lcp:
                    max_lcp = max([key for key in lcp_counter if lcp_counter[key] > 0], default=0)
                removed.append((i - 1, l))
    
            if i < n - 1:
                l = lcp[i]
                lcp_counter[l] -= 1
                if lcp_counter[l] == 0 and l == max_lcp:
                    max_lcp = max([key for key in lcp_counter if lcp_counter[key] > 0], default=0)
                removed.append((i, l))
    
            new_lcp = 0
            if 0 < i < n - 1:
                new_lcp = self.longest_common_prefix(words[i - 1], words[i + 1])
                lcp_counter[new_lcp] += 1
                max_lcp = max(max_lcp, new_lcp)
    
            answer.append(max_lcp)
    
            for index, l in removed:
                lcp_counter[l] += 1
                max_lcp = max(max_lcp, l)
            if 0 < i < n - 1:
                lcp_counter[new_lcp] -= 1
                if lcp_counter[new_lcp] == 0 and new_lcp == max_lcp:
                    max_lcp = max([key for key in lcp_counter if lcp_counter[key] > 0], default=0)
    
        return answer