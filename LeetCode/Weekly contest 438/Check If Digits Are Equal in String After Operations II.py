class Solution:
    def mod5(self, n, k):
        fact = [1, 1, 2, 6, 24]
        fact = [x % 5 for x in fact]
        
        res = 1
        while n or k:
            m, j = n % 5, k % 5
            if j > m:
                return 0
            
            num = fact[m]
            den = (fact[j] * fact[m - j]) % 5
            
            invDen = 1
            for x in range(1, 5):
                if (den * x) % 5 == 1:
                    invDen = x
                    break
            
            cur = (num * invDen) % 5
            res = (res * cur) % 5
            n //= 5
            k //= 5
        
        return res

    def mod10(self, n, k):
        a = 1 if (n & k) == k else 0
        b = self.mod5(n, k)
        
        for x in range(10):
            if x % 2 == a and x % 5 == b:
                return x
        return 0

    def hasSameDigits(self, s):
        n = len(s)
        m = n - 2
        A = B = 0
        
        for i in range(m + 1):
            temp = self.mod10(m, i)
            A = (A + temp * (int(s[i]))) % 10
        
        for i in range(m + 1):
            temp1 = self.mod10(m, i)
            B = (B + temp1 * (int(s[i + 1]))) % 10
        
        return A == B