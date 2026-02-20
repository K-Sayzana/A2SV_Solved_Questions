t=int(input())


for _ in range(t):

    casino=[]
    n, x =map(int, input().split())
    for _ in range(n):
        l, r, k=map(int, input().split())
        casino.append((l, r, k))
    casino.sort(key=lambda x: (x[0], -x[1], -x[2]))



    for cas in casino:
        if x >= cas[0] and x<=cas[1]:
            x=max(x, cas[2])
    
    print(x)




    
