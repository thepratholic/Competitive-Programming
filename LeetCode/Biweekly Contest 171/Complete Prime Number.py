class Solution:
    def completePrime(self, num: int) -> bool:

        def isPrime(n):
            if n < 2:
                return False
            if n % 2 == 0:
                return n == 2
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True
                    
        s = str(num)

        for i in range(len(s)):
            if not isPrime(int(s[:i + 1])):
                return False


        for i in range(len(s) - 1, -1, -1):
            if not isPrime(int(s[i : ])):
                return False

        return True