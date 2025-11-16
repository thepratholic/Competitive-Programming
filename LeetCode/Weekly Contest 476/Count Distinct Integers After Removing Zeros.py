class Solution:
    def countDistinct(self, n: int) -> int:
        if n < 10:
            return n
        
        s = str(n)
        sz = len(s)

        ans = 0
        p = 9
        for i in range(1, sz):
            ans += p
            p *= 9

        kdc = 0
        for i, ch in enumerate(s):
            
            d = int(s[i]) 
            if d == 0: 
                break
                
            small = d - 1
            rem = sz - 1 - i
            
            kdc += small * (9 ** rem)

            if i == sz - 1:
                kdc += 1 
        
        ans += kdc
        return ans