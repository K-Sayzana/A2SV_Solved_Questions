t=int(input())

for _ in range(t):
    n=int(input())

    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    ans=[]
    c=0

    
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j+1], a[j]=a[j], a[j+1]
                ans.append((1, j+1))
                c+=1

    
    for i in range(n):
        for j in range(n-i-1):
            if b[j]>b[j+1]:
                b[j+1], b[j]=b[j], b[j+1]
                ans.append((2, j+1))
                c+=1

    for i in range(n):
        if a[i]>b[i]:
            a[i], b[i]=b[i], a[i]
            ans.append((3, i+1))
            c+=1

    # print(a, b)
    print(c)
    for a in ans:
        print(a[0], a[1])
