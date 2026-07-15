from heapq import heappop, heappush

class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = (10 ** 9) + 7
        n = len(value)

        def check(threshold):
            count = 0

            for v, d in zip(value, decay):
                if v >= threshold:
                    count += (v - threshold) // d + 1

            return count <= m

        low = 0
        high = 10 ** 9 + 1
        point = high

        while low <= high:
            mid = (low + high) >> 1

            if check(mid):
                point = mid # <= m values mil gayi, toh dekho aur kitni values le skte ho by dec. of threshold
                high = mid - 1

            else:
                low = mid + 1

        def get(num):
            return num * (num - 1) >> 1

        ans = 0
        taken = 0
        pq = []

        for i in range(n):
            v = value[i]
            d = decay[i]

            times = 0

            if v >= point:
                times += (v - point) // d + 1 # iss index ki sequence mein se kitni values utha skte hai

            taken += times

            ans += (times * v) - (d * get(times)) # derive ki hai yeh
            ans %= MOD

            nxt_val = v - (times * d)
            heappush(pq, (-nxt_val, i))

        rem = m - taken # boundary se taken values leli, but still kuch rem values hai, jo heap se leni hai

        while rem > 0 and pq:
            cur, idx = heappop(pq)
            cur = -cur

            if cur <= 0:
                break

            ans += cur
            ans %= MOD

            nxt_val = cur - decay[idx]
            heappush(pq, (-nxt_val, idx))

            rem -= 1

        return ans