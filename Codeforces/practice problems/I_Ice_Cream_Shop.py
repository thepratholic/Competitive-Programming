from math import ceil

def main():
    n, m = map(int, input().split())
    
    rewards = list(map(int, input().split()))
    
    x_values = sorted(list(map(int, input().split())))
    
    first_segment_end = ceil(x_values[0] / 100)
    best_sum = sum(rewards[:first_segment_end])
    
    for i in range(len(x_values) - 1):
        window_start = x_values[i] // 100 + 1
        
        if window_start >= n:
            break

        window_size = int(((x_values[i+1] - x_values[i]) / 2) // 100 + 1)
        
        window_end = min(ceil(x_values[i+1] / 100), n)
        
        if window_start + window_size <= window_end:
            current_window_sum = sum(rewards[window_start:window_start + window_size])
            best_sum = max(best_sum, current_window_sum)
        else:
            current_window_sum = 0
        
        while window_start + window_size < window_end:
            current_window_sum -= rewards[window_start]
            if window_start + window_size < n:
                current_window_sum += rewards[window_start + window_size]
            best_sum = max(best_sum, current_window_sum)
            window_start += 1

    final_segment_start = x_values[-1] // 100 + 1
    final_segment_sum = sum(rewards[final_segment_start:])
    best_sum = max(best_sum, final_segment_sum)
    
    print(best_sum)

if __name__ == '__main__':
    main()
