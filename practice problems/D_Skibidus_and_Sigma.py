def solve():
    n, m = map(int, input().split())

    arrays = [list(map(int, input().split())) for _ in range(n)]

    sorted_matrix = sorted(arrays, key = sum, reverse=True)

    flatten = [num for row in sorted_matrix for num in row]

    prefix = [0] * (n * m)

    prefix[0] = flatten[0]

    for i in range(1, n*m):
        prefix[i] = prefix[i-1] + flatten[i]

    print(sum(prefix))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()