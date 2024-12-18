# cook your dish here
def poster_perimeter(N, M, K):
    min_diff = float('inf')

    for L in range(1, N + 1): 
        for W in range(1, M + 1):  
            perimeter = 2 * (L + W) 
            diff = abs(perimeter - K)  
            min_diff = min(min_diff, diff)  

    return min_diff

for _ in range(int(input())):
    N, M, K = map(int, input().split())
    result = poster_perimeter(N, M, K)
    print(result)