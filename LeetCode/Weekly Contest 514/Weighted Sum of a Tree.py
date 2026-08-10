from collections import defaultdict

class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:

        tree = defaultdict(list)

        for child, parent in enumerate(parent):
            if child == 0: continue
            tree[parent].append(child)

        height = 0
        def get_height(node, h):
            nonlocal height

            height = max(height, h)

            for child in tree[node]:
                get_height(child, h + 1)

        get_height(0, 1)

        def f(node, depth):
            cur = nums[node] * (height - depth + 1)

            for child in tree[node]:
                cur += f(child, depth + 1)

            return cur

        return f(0, 1)