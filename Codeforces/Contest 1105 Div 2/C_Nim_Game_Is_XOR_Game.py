
from sys import stdin, stdout


input = stdin.readline

MOD = 998244353

def solve():
    # Write your solution here
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return
        
    x = 0
    for v in a:
        x ^= v
    
    cnt = 0
    if x == 0:
        print(1)
        return
    
    else:
        h = x.bit_length() - 1
        mask = 1 << h
        for v in a:
            if v & mask:
                cnt += 1
    
    print(cnt % MOD)

t = int(input())
for _ in range(t):
    solve()