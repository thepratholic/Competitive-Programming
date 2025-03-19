def solve(n, k):
    if n >= k + 1:
        a = 1
        b = k + 1
        lcm = a * b
        gcd = 1
        if abs(lcm - gcd) >= 2 * k:
            return a, b
    
    if 2*k <= n:
        a = 2*k
        b = 3*k
        gcd = k
        lcm = 6*k
        if abs(lcm - gcd) >= 2*k and a <= n and b <= n:
            return a, b
    
    if n >= 2*k and n >= 3*k:
        a = 2*k
        b = 3*k
        lcm = a * b
        gcd = k
        if abs(lcm - gcd) >= 2*k:
            return a, b
    
    if n > k:
        a = n
        b = n - k
        gcd = gcd_calc(a, b)
        lcm = (a * b) // gcd
        if abs(lcm - gcd) >= 2*k:
            return a, b
    
    return -1, -1

def gcd_calc(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a, b = solve(n, k)
    print(f"{a} {b}")