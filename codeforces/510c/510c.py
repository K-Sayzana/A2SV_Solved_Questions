from collections import deque


n = int(input())

names = []
for _ in range(n):
    names.append(input())

ins = [0] * 26
adj = [[] for _ in range(26)]

flag = 1
for i in range(1, n):
    a = names[i]
    b = names[i - 1]
    if len(b) > len(a) and b[: len(a)] == a:
        flag = 0
        break

    if a[: len(b)] == b:
        continue

    for j in range(min(len(a), len(b))):
        if a[j] != b[j]:
            adj[ord(b[j]) - ord("a")].append(ord(a[j]) - ord("a"))
            ins[ord(a[j]) - ord("a")] += 1
            break

qu = deque()

for i in range(26):
    if ins[i] == 0:
        qu.append(i)

ans = []
while qu:
    ch = qu.popleft()
    ans.append(chr(ord("a") + ch))

    for ne in adj[ch]:
        ins[ne] -= 1
        if ins[ne] == 0:
            qu.append(ne)

if len(ans) != 26 or not flag:
    print("Impossible")
else:
    print("".join(ans))