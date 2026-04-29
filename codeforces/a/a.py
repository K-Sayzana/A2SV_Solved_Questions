import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())

adj = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    adj[u].append(v)
    adj[v].append(u)


def dfs(node):
    stk = [(node, -1, 0)]
    ans = [0, node]

    while stk:
        v, p, d = stk.pop()
        if d > ans[0]:
            ans[0] = d
            ans[1] = v

        for ne in adj[v]:
            if ne != p:
                stk.append((ne, v, d + 1))

    return ans


print(3 * dfs(dfs(0)[1])[0])