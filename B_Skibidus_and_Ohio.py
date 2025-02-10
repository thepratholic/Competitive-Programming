def min_length(s):
    n = len(s)
    if n == 1:
        return 1

    adjacent_pairs = sum(s[i] == s[i + 1] for i in range(n - 1))

    return max(1, n - adjacent_pairs)

# Read number of test cases
t = int(input())
for _ in range(t):
    s = input().strip()
    print(min_length(s))
