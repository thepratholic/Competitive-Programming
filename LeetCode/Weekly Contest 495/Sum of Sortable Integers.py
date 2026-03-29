class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = 0

        def f(a, b):
            s1 = ",".join(map(str, a))
            s2 = ",".join(map(str, b))

            return s2 in (s1 + "," + s1)

        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)

                if i != (n // i):
                    divisors.append(n // i)

        
        for k in divisors:
            ok = True

            for i in range(0, n, k):
                a = nums[i : i + k]
                b = sorted_nums[i : i + k]

                if not f(a, b):
                    ok = False
                    break

            
            if ok:
                ans += k

        return ans