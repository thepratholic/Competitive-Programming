def solve_test_case():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # k/2 is number of even-indexed subarrays that will form b
    # Plus 1 for the 0 that gets added at the end
    max_b_length = k//2 + 1
    
    # Count frequencies of small numbers (we only need numbers up to k/2)
    freq = {}
    for x in a:
        if x <= k//2:  # Only count numbers we might actually need
            freq[x] = freq.get(x, 0) + 1
    
    # For each position in b (except last which will be 0)
    # we need number i+1 to have cost > i
    for i in range(1, k//2 + 1):
        if i not in freq:
            return i
    
    # If we get here, we can make b[0]=1, b[1]=2, ..., b[k/2-1]=k/2
    # The last element is 0, so cost will be k/2 + 1
    return k//2 + 1

def main():
    t = int(input())
    for _ in range(t):
        print(solve_test_case())

if __name__ == "__main__":
    main()