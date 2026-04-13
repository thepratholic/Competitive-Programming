from math import gcd


class SegmentTree:
    def __init__(self, arr, p):
        self.n = len(arr)
        self.arr = arr
        self.p = p
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def get_val(self, x):
        if x % self.p == 0:
            return x // self.p
        return 0

    def build(self, idx, l, r):
        if l == r:
            self.tree[idx] = self.get_val(self.arr[l])
            return

        mid = (l + r) >> 1
        self.build(2 * idx + 1, l, mid)
        self.build(2 * idx + 2, mid + 1, r)

        self.tree[idx] = gcd(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def update(self, idx, l, r, u_idx, u_val):
        if l == r:
            self.arr[l] = u_val
            self.tree[idx] = self.get_val(u_val)
            return

        mid = (l + r) >> 1

        if u_idx <= mid:
            self.update(2 * idx + 1, l, mid, u_idx, u_val)

        else:
            self.update(2 * idx + 2, mid + 1, r, u_idx, u_val)

        self.tree[idx] = gcd(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def query(self, idx, l, r, start, end):
        if r < start or l > end:
            return 0

        if l >= start and r <= end:
            return self.tree[idx]

        mid = (l + r) >> 1

        return gcd(self.query(2 * idx + 1, l, mid, start, end), self.query(2 * idx + 2, mid + 1, r, start, end))


class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        n = len(nums)

        st = SegmentTree(nums, p)

        cnt = sum(1 for x in nums if x % p == 0)

        ans = 0

        for idx, val in queries:
            if nums[idx] % p == 0:
                cnt -= 1

            st.update(0, 0, n - 1, idx, val)
            nums[idx] = val

            if nums[idx] % p == 0:
                cnt += 1

            if cnt > 0 and st.tree[0] == 1:

                if cnt < n:
                    ans += 1 # case 1 : saare elements nahi hai, so valid subseq ban skta hai

                else: # case 2 : cnt == n, lekin humein < n elements chahiye for subseq, so ek element remove karna padega

                    ok = False

                    for i in range(n):
                        g = 0

                        if i > 0:
                            g = gcd(g, st.query(0, 0, n - 1, 0, i - 1))

                        if i < n - 1:
                            g = gcd(g, st.query(0, 0, n - 1, i + 1, n - 1))

                        if g == 1:
                            ok = True
                            break

                    if ok:
                        ans += 1

        return ans