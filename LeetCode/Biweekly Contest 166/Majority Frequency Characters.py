from collections import Counter, defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = Counter(s)

        groups = defaultdict(list)
        for ch, f in freq.items():
            groups[f].append(ch)

        best_k, best_group = -1, []
        for k, chars in groups.items():
            if len(chars) > len(best_group) or (len(chars) == len(best_group) and k > best_k):
                best_k, best_group = k, chars

        return "".join(best_group)
