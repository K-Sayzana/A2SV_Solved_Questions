t=int(input())

for _ in range(t):
    n=int(input())
    p=list(map(int, input().split()))

    if n==2:
        print(n)
        print(*p)
        continue

    ans=[p[0]]

    for i in range(1, n):
        a= p[i]>p[i-1] and i < n-1 and  p[i+1]>p[i]
        b=p[i]<p[i-1] and i < n-1 and  p[i+1]<p[i]

        if a or b:
            continue
        ans.append(p[i])
    
    print(len(ans))
    print(*ans)

