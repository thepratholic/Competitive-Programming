import heapq

def perform_operations(A, K):
    # Convert A into a heap (min-heap by default)
    min_heap = A[:]
    heapq.heapify(min_heap)
    
    # Create a max-heap by pushing negative values into a min-heap
    max_heap = [-a for a in A]
    heapq.heapify(max_heap)
    
    for _ in range(K):
        # Get the minimum and maximum values
        X = heapq.heappop(min_heap)
        Y = -heapq.heappop(max_heap)
        
        # Calculate their sum
        S = X + Y
        
        # Insert the sum into both heaps
        heapq.heappush(min_heap, S)
        heapq.heappush(max_heap, -S)
    
    # Convert the heap back to a sorted list for output
    final_array = sorted(min_heap)
    
    return final_array

# Read the number of test cases
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Perform the operations and get the final array
    result = perform_operations(A, K)
    
    # Print the result as a space-separated string
    print(" ".join(map(str, result)))
