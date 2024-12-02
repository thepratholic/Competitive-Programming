
class Solution:
    def findMax(self, k : int, n : int, m : int) -> int:
        # code here
        if (k * m) < n: return -1

        left, right = 0, min(n, k)

        max_alone = 0
        while left <= right:
            mid = (left + right) // 2
            rem_students = n - mid
            rem_benches = k - mid

            if rem_students <= rem_benches * m:
                max_alone = mid
                left = mid + 1
            else:
                right = mid - 1

        return max_alone