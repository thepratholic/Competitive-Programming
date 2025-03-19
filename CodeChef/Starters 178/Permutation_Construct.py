def solve():
    n, k = map(int, input().split())
    
    if n == 1:
        return [-1]
    
    mod_groups = [[] for _ in range(k)]
    for i in range(1, n+1):
        mod_groups[i % k].append(i)
    
    for group in mod_groups:
        if len(group) == 1:
            return [-1]
    
    permutation = [0] * (n+1) 
    
    for group in mod_groups:
        if not group:
            continue
            
        for i in range(len(group)):
            permutation[group[i]] = group[(i + 1) % len(group)]
    
    return permutation[1:]

t = int(input())
for _ in range(t):
    result = solve()
    if result[0] == -1:
        print("-1")
    else:
        print(" ".join(map(str, result)))