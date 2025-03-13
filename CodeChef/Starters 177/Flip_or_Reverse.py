def solve():
    n = int(input().strip())
    a = input().strip()
    b = input().strip()
    
    diff_positions = [i for i in range(n) if a[i] != b[i]]
    
    i = 0
    ans = []
    
    while i < len(diff_positions):
        j = i + 1
        while j < len(diff_positions) and diff_positions[j] == diff_positions[j - 1] + 1:
            j += 1
        ans.append((diff_positions[i], diff_positions[j - 1]))
        i = j
    
    print(len(ans))
    for start, end in ans:
        print(1, start + 1, end + 1)

def main():
    t = int(input().strip())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
