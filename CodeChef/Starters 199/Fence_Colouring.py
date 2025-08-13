import sys
from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = defaultdict(int)
    for c in a:
        freq[c] += 1
    
    max_freq = max(freq.values())
    
    mini_c = n 
    
    for c, count in freq.items():
        if count == max_freq:
            if c == 1:
                cost = n - count
            else:
                cost = 1 + (n - count)
            mini_c = min(mini_c, cost)
    
    print(mini_c)

t = int(input())
for _ in range(t):
    solve()