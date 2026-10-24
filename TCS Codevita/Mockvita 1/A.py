import sys


def settle(grid, side):
    m, n = len(grid), len(grid[0])
    if side == 1:
        return ['.' * (n - r.count('*')) + '*' * r.count('*') for r in grid]
    if side == 3:
        return ['*' * r.count('*') + '.' * (n - r.count('*')) for r in grid]

    cols = [''.join(c) for c in zip(*grid)]
    if side == 0:
        cols = ['.' * (m - c.count('*')) + '*' * c.count('*') for c in cols]
    else:
        cols = ['*' * c.count('*') + '.' * (m - c.count('*')) for c in cols]
    return [''.join(r) for r in zip(*cols)]


def rotate_right(grid):
    return [''.join(col) for col in zip(*grid[::-1])]


def main():
    tokens = sys.stdin.read().split()
    m, n = int(tokens[0]), int(tokens[1])
    cells = tokens[2:2 + m * n]
    grid = [''.join(cells[i * n:(i + 1) * n]) for i in range(m)]

    k = int(tokens[2 + m * n])
    moves = tokens[3 + m * n:3 + m * n + k]

    side = 0       
    grid = settle(grid, side)
    settled = {side} 

    for move in moves:
        side = (side + 1) % 4 if move == "right" else (side - 1) % 4
        if side in settled:
            continue
        new_grid = settle(grid, side)
        if new_grid == grid:
            settled.add(side)
        else:
            grid = new_grid
            settled = {side}

    for _ in range(side): 
        grid = rotate_right(grid)

    print("\n".join(" ".join(row) for row in grid))


main()