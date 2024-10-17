def final_position_of_sushil(T, test_cases):
    results = []
    
    for i in range(T):
        N = test_cases[i][0]  # Number of people in the queue
        A = test_cases[i][1]  # Array of wealth of people
        
        sushil_wealth = A[N-1]  # Sushil's wealth is the last element in the array
        pos = N - 1  # Sushil starts at the last position (0-based index)
        
        # Process to bully people directly in front
        while pos > 0:
            if A[pos-1] <= sushil_wealth / 2:
                # Bully the person in front, move to the next one
                pos -= 1
            else:
                # No more bullying possible, break the loop
                break
        
        # Store the result as 1-based index
        results.append(pos + 1)
    
    return results


# Example usage:
T = int(input())  # Number of test cases
test_cases = []
for _ in range(T):
    N = int(input())  # Number of people in the queue
    A = list(map(int, input().split()))  # Wealth of each person
    test_cases.append((N, A))

results = final_position_of_sushil(T, test_cases)

# Output the results
for res in results:
    print(res)
