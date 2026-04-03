from bisect import bisect_left, bisect_right

t = int(input())


def getIdx(val):
    return bisect_left(b, val)


for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    if a == sorted(a):
        print("YES")
        continue

    a[0] = min(a[0], b[0] - a[0])
    flag = 1
    for i in range(1, n):
        idx = getIdx(a[i - 1] + a[i])

        if idx == m and a[i] < a[i - 1]:
            flag = 0
            break

        if idx == m:
            continue
        elif a[i] >= a[i - 1]:
            a[i] = min(a[i], b[idx] - a[i])
        else:
            a[i] = b[idx] - a[i]

    if flag:
        print("YES")
    else:
        print("NO")