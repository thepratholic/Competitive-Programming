class Solution:
    def minSelection(self, avail: List[List[int]], target: List[List[int]]) -> int:
        t = sorted(target)
        merge = []
        l, r = t[0]
        for x, y in t[1:]:
            if x <= r:
                r = max(r, y)
            else:
                merge.append([l, r])
                l, r = x, y
        merge.append([l, r])

        a = sorted(avail)
        n = len(a)
        i = 0
        ans = 0
        reach = float('-inf')
        best = float('-inf')

        for l, r in merge:
            while reach < r:
                need = l if reach < l else reach

                while i < n and a[i][0] <= need:
                    best = max(best, a[i][1])
                    i += 1

                if best < l or best <= reach:
                    return -1

                ans += 1
                reach = best
        return ans