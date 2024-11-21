def max_sweets(N, K, A):
    total_calories = 0
    count = 0

    for i in range(N):

        if total_calories + A[i] <= K:
            total_calories += A[i]
            count += 1
        else:
            break
    return count


def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())

        A = list(map(int, input().split()))

        print(max_sweets(N, K, A))

if __name__ == "__main__":
    main()
