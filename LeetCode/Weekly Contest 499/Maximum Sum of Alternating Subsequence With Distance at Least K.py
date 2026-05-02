class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * self.n)

    def query(self, idx, l, r, start, end):
        if r < start or l > end:
            return 0

        if l >= start and r <= end:
            return self.tree[idx]

        mid = (l + r) >> 1
        left = self.query(2 * idx + 1, l, mid, start, end)
        right = self.query(2 * idx + 2, mid + 1, r, start, end)

        return max(left, right)

    def update(self, idx, l, r, u_idx, u_val):
        if l == r:
            self.tree[idx] = max(self.tree[idx], u_val)
            return 

        mid = (l + r) >> 1

        if u_idx <= mid:
            self.update(2 * idx + 1, l, mid, u_idx, u_val)

        else:
            self.update(2 * idx + 2, mid + 1, r, u_idx, u_val)

        self.tree[idx] = max(self.tree[2 * idx + 1], self.tree[2 * idx + 2])


class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums)) # coordinate compression

        mp = {}
        for i, v in enumerate(vals):
            mp[v] = i

        dp = [[0, 0] for _ in range(n)]

        m = len(vals)
        seg_low = SegmentTree(m)
        seg_high = SegmentTree(m)

        for i in range(n):

            if i - k >= 0:
                old_val = nums[i - k]
                pos = mp[old_val]

                seg_low.update(0, 0, m - 1, pos, dp[i - k][0])
                seg_high.update(0, 0, m - 1, pos, dp[i - k][1])

            cur = nums[i]
            pos = mp[cur]

            best_high = 0
            if pos + 1 <= m - 1:
                best_high = seg_high.query(0, 0, m - 1,pos + 1, m - 1)

            dp[i][0] = cur + best_high


            best_low = 0
            if pos - 1 >= 0:
                best_low = seg_low.query(0, 0, m - 1, 0,pos - 1)

            dp[i][1] = cur + best_low

        ans = 0
        for low, high in dp:
            ans = max(ans, low, high)

        return ans