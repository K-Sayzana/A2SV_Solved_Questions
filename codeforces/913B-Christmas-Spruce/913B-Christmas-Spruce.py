from itertools import count


n = int(input())
child = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    child[int(input())].append(i)


def solve(node):
    if len(child[node]) == 0:
        return True

    count = 0
    for c in child[node]:
        count += 1 if (len(child[c]) == 0) else 0

    if count < 3:
        return False

    for ch in child[node]:
        if not solve(ch):
            return False

    return True


if solve(1):
    print("Yes")
else:
    print("No")