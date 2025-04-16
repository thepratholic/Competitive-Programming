# cook your dish here
def max_plucks(N, K, D, regrowth_times):
    if K == N:
        return 0

    available_to_pluck = N - K
    

    regrowth_times.sort()
    
    total_plucks = 0
    for i in range(available_to_pluck):
        T = regrowth_times[i]
        plucks_for_flower = (D - 1) // T + 1  
        total_plucks += plucks_for_flower
        
    return total_plucks

def process_test_cases():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(input_data[index])
        K = int(input_data[index+1])
        D = int(input_data[index+2])
        index += 3
        regrowth_times = list(map(int, input_data[index:index+N]))
        index += N
        results.append(max_plucks(N, K, D, regrowth_times))
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    process_test_cases()
