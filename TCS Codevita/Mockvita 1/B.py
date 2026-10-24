import sys


def sign(v):
    return (v > 0) - (v < 0)


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pts = [(int(data[1 + 2 * i]) * 10, int(data[2 + 2 * i]) * 10) for i in range(n)]

    changed = True
    while changed:
        changed = False
        for i in range(len(pts)):
            a, b, c = pts[i - 1], pts[i], pts[(i + 1) % len(pts)]
            if (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]) == 0:
                pts.pop(i)
                changed = True
                break

    m = len(pts)
    area2 = sum(pts[i][0] * pts[(i + 1) % m][1] - pts[(i + 1) % m][0] * pts[i][1]
                for i in range(m))
    if area2 < 0:
        pts.reverse()

    normals = []
    for i in range(m):
        dx = pts[(i + 1) % m][0] - pts[i][0]
        dy = pts[(i + 1) % m][1] - pts[i][1]
        normals.append((-sign(dy), sign(dx)))

    best = 0
    for h in range(1, 300):
        new = []
        for i in range(m):
            n1, n2 = normals[i - 1], normals[i]
            new.append((pts[i][0] + h * (n1[0] + n2[0]),
                        pts[i][1] + h * (n1[1] + n2[1])))

        valid = True
        for i in range(m):
            ox = pts[(i + 1) % m][0] - pts[i][0]
            oy = pts[(i + 1) % m][1] - pts[i][1]
            nx = new[(i + 1) % m][0] - new[i][0]
            ny = new[(i + 1) % m][1] - new[i][1]
            if ox * nx + oy * ny <= 0 or abs(nx) + abs(ny) < 1:
                valid = False
                break
        if not valid:
            continue

        a2 = sum(new[i][0] * new[(i + 1) % m][1] - new[(i + 1) % m][0] * new[i][1]
                 for i in range(m))
        if a2 <= 0:
            continue
        best = max(best, a2 * h / 2000)

    print(f"{best:.2f}")


main()