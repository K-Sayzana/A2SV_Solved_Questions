from collections import Counter


t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))

    if l >= r:
        max_s = Counter(socks[:l])
        min_s = Counter(socks[l:])
    else:
        min_s = Counter(socks[:l])
        max_s = Counter(socks[l:])

    for k, v in min_s.items():
        if max_s[k] > 0:
            x = min(min_s[k], max_s[k])
            min_s[k] -= x
            max_s[k] -= x

    take = abs(r - l) // 2
    ans = 0

    for k, v in max_s.items():
        if take == 0:
            break

        ans += min(take, v // 2)
        take -= min(take, v // 2)

    print(ans + (2 * take) + sum(min_s.values()))