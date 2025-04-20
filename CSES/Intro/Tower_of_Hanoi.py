def f(n, s, a, d, moves):
    if n == 1:
        moves.append((s, d))
 
    else:
        f(n-1, s, d, a, moves)
        moves.append((s, d))
        f(n-1, a, s, d, moves)
 
def solve(n):
    moves = []
    f(n, 1, 2, 3, moves)
    print(len(moves))
    for i, j in moves:
        print(i, j)
 
if __name__ == "__main__":
    n = int(input())
    solve(n)