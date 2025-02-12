def find_repeating_element():
    t = int(input())
    for _ in range(t):
        n = int(input())
        v = list(map(int, input().split()))

        freq = {}
        for num in v:
            freq[num] = freq.get(num, 0) + 1

        ans = -1
        for key, value in freq.items():
            if value >= 2:
                ans = key

        if ans > 0:
            print(1)
            print(ans)
        else:
            print(ans)

# Run the function
find_repeating_element()
