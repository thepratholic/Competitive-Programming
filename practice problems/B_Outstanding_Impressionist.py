import sys

def solve():
    n = int(sys.stdin.readline().strip())
    
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    sum_values = [0] * (2 * n + 1)  
    cnt = [0] * (2 * n + 1)  

    # Read input and mark fixed values
    for i in range(1, n + 1):
        l[i], r[i] = map(int, sys.stdin.readline().split())
        if l[i] == r[i]:  
            sum_values[l[i]] = 1  
            cnt[l[i]] += 1  

    for i in range(2, 2 * n + 1):
        sum_values[i] += sum_values[i - 1]

    result = []
    for i in range(1, n + 1):
        if l[i] == r[i]:  
            result.append("1" if cnt[l[i]] == 1 else "0")
        else:
            total_fixed_in_range = sum_values[r[i]] - sum_values[l[i] - 1]
            range_size = r[i] - l[i] + 1
            result.append("1" if total_fixed_in_range < range_size else "0")

    print("".join(result))

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        solve()
