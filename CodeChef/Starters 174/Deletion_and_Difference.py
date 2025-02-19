def min_length_after_operations(N, A):
    # Count frequencies of each number
    freq = {}
    for x in A:
        freq[x] = freq.get(x, 0) + 1
    
    # Keep performing operations while possible
    while True:
        # Try to find pairs
        any_pairs = False
        new_freq = {}
        
        # First, handle non-zero numbers
        for num in freq:
            count = freq[num]
            # Handle unpaired elements
            if count % 2 == 1:
                new_freq[num] = new_freq.get(num, 0) + 1
            # Handle pairs
            pairs = count // 2
            if pairs > 0:
                any_pairs = True
                # Add difference (0) to new frequency
                new_freq[0] = new_freq.get(0, 0) + pairs
        
        # If no pairs were found, we're done
        if not any_pairs:
            return sum(new_freq.values())
            
        # Update frequency dictionary for next iteration
        freq = new_freq

# Process input
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(min_length_after_operations(N, A))