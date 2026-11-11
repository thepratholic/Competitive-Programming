import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input().strip()
    a = list(map(int, input().split()))
    
    allA = all(ch == 'A' for ch in s)
    
    for val in a:
        if allA:
            print(val)
            continue
        
        i = 0
        steps = 0
        while val > 0:
            if s[i] == 'A':
                val -= 1
            else:
                val //= 2
            i = (i + 1) % n
            steps += 1
        print(steps)
