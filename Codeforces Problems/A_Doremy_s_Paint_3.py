from collections import Counter


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    frequency_map = Counter(arr)

    if len(frequency_map) >= 3:
        print("No")
    else:
        freq_values = list(frequency_map.values())
        freq_1 = min(freq_values)
        freq_2 = max(freq_values)

        if freq_1 == freq_2:
            print("Yes")
        elif n % 2 == 1 and abs(freq_1 - freq_2) == 1:
            print("Yes")
        else:
            print("No")