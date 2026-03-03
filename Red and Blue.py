t = int(input())

for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))

    for k in range(1, len(red)):
        red[k] = red[k] + red[k - 1]
    for k in range(1, len(blue)):
        blue[k] = blue[k] + blue[k - 1]

    print(max(0, max(blue) + max(red), max(blue), max(red)))
