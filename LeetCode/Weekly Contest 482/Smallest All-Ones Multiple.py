from collections import deque


class Solution:
    def minAllOneMultiple(self, k: int) -> int:

        if k % 2 == 0 or k % 5 == 0:
            return -1

        q = deque()
        q.append((1 % k, 1))

        vis = set()
        vis.add(1 % k)

        while q:
            cur, sz = q.popleft()

            if cur == 0:
                return sz

            else:
                next_ = (cur * 10 + 1) % k
                if next_ not in vis:
                    vis.add((cur * 10 + 1) % k)
                    q.append((next_, sz + 1))

        return -1