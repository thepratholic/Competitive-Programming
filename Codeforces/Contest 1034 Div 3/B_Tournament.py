import sys

def solve():
    n, j, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    player_j = a[j - 1]
    
    maxi = 0
    for x in a:
        if x > maxi:
            maxi = x
    

    if player_j == maxi:
        sys.stdout.write("YES\n")
    else:
        if k == 1:
            sys.stdout.write("NO\n")

        else:
            sys.stdout.write("YES\n")

num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()