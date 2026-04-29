from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [a - 1 for a in arr]

    ins = [0] * n

    adj = [[] for _ in range(n)]
    for i in range(n):
        adj[i].append(arr[i])
        ins[arr[i]] += 1

    qu = deque([(i, 1) for i, cnt in enumerate(ins) if cnt == 0])

    max_d = 0
    while qu:

        v, d = qu.popleft()
        max_d = max(max_d, d)
        for ne in adj[v]:
            ins[ne] -= 1
            if ins[ne] == 0:
                qu.append((ne, d + 1))

    print(max_d + 2)