def solve():
    import sys
    input = sys.stdin.readline
    mod = 998244353
    MAX = 500000
    fact = [1]*(MAX+1)
    invfact = [1]*(MAX+1)
    for i in range(2, MAX+1):
        fact[i] = fact[i-1]*i % mod
    invfact[MAX] = pow(fact[MAX], mod-2, mod)
    for i in range(MAX, 0, -1):
        invfact[i-1] = invfact[i]*i % mod
    t = int(input())
    res = []
    for _ in range(t):
        c = list(map(int, input().split()))
        L = sum(c)
        O = (L+1)//2
        E = L//2
        dp = [0]*(O+1)
        dp[0] = 1
        for cnt in c:
            if cnt == 0: continue
            new_dp = [0]*(O+1)
            for s in range(O+1):
                if dp[s]:
                    new_dp[s] = (new_dp[s] + dp[s]) % mod
                    ns = s + cnt
                    if ns <= O:
                        new_dp[ns] = (new_dp[ns] + dp[s]) % mod
            dp = new_dp
        ways_assign = dp[O]
        prod = 1
        for x in c:
            prod = prod * fact[x] % mod
        ways_arr = fact[O] * fact[E] % mod * pow(prod, mod-2, mod) % mod
        res.append(str(ways_assign * ways_arr % mod))
    sys.stdout.write("\n".join(res))
    
if __name__ == '__main__':
    solve()
