r, c = map(int, input().split())


dom = []
for _ in range(r):
    dom.append(list(input()))


grid1 = [([0] * (c + 1)) for _ in range(r + 1)]
for i in range(r):
    for j in range(c):
        if dom[i][j] == "." and (j + 1 < c) and dom[i][j + 1] == ".":
            grid1[i + 1][j + 1] = 1

for i in range(1, len(grid1)):
    for j in range(1, len(grid1[0])):
        grid1[i][j] += grid1[i - 1][j] + grid1[i][j - 1] - grid1[i - 1][j - 1]

# print(grid1)

grid2 = [([0] * (c + 1)) for _ in range(r + 1)]
for i in range(r):
    for j in range(c):
        if dom[i][j] == "." and i + 1 < r and dom[i + 1][j] == ".":
            grid2[i + 1][j + 1] = 1
for i in range(1, len(grid2)):
    for j in range(1, len(grid2[0])):
        grid2[i][j] += grid2[i - 1][j] + grid2[i][j - 1] - grid2[i - 1][j - 1]

# print(grid2)
q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    h = (
        grid1[r2][c2 - 1]
        - grid1[r1 - 1][c2 - 1]
        - grid1[r2][c1 - 1]
        + grid1[r1 - 1][c1 - 1]
    )
    v = (
        grid2[r2 - 1][c2]
        - grid2[r1 - 1][c2]
        - grid2[r2 - 1][c1 - 1]
        + grid2[r1 - 1][c1 - 1]
    )

    print(h + v)
