n, k, q = map(int, input().split())
coffee = [0] * 200002

for _ in range(n):
    l, r = map(int, input().split())
    coffee[l] += 1
    coffee[r + 1] -= 1


for i in range(1, len(coffee)):
    coffee[i] = coffee[i - 1] + coffee[i]

for i in range(len(coffee)):
    coffee[i] = 1 if coffee[i] >= k else 0

for i in range(1, len(coffee)):
    coffee[i] = coffee[i - 1] + coffee[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(coffee[b] - coffee[a - 1])
