def solve_test_case():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    freq_a = {}
    freq_b = {}
    for x in a:
        freq_a[x] = freq_a.get(x, 0) + 1
    for x in b:
        freq_b[x] = freq_b.get(x, 0) + 1

    if any(v < 2 for v in freq_a.values()) or any(v < 2 for v in freq_b.values()):
        return "NO"

    if len(freq_a) == 1 and len(freq_b) == 1:
        return "NO"

    if len(freq_a) == 1 or len(freq_b) == 1:

        if len(freq_a) >= 3 or len(freq_b) >= 3:
            return "YES"
        return "NO"
    return "YES"

def main():
    t = int(input())
    for _ in range(t):
        print(solve_test_case())

if __name__ == "__main__":
    main()