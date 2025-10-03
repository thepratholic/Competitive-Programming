from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(1)
        continue

    freq = Counter(a)
    cnt = 0
    ans = 0
    for k, v in freq.items():
        if cnt == 0:
            ans += 1
            cnt += 1
        else:
            ans += 2
            cnt += 1

    print(ans)
