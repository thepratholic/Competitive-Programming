def largest_area(N):
    max_area = 0
    # Loop over possible lengths L
    for L in range(1, N // 2):
        W = (N // 2) - L
        max_area = max(max_area, L * W)
    return max_area

def main():
    # Number of test cases
    T = int(input())
    
    # Process each test case
    for _ in range(T):
        N = int(input())
        print(largest_area(N))

# Example usage
if __name__ == "__main__":
    main()
