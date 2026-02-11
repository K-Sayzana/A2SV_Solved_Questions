t=int(input())

for _ in range(t):
    n, x, k=map(int, input().split())
    s=input()

    prefix=[0 for _ in range(n+1)]

    a=-1
    for i in range(n):
        prefix[i+1]+=prefix[i]
        prefix[i+1]+= 1 if s[i]=='R' else -1

        if prefix[i+1]==0:
            a=i+1
            break
    

    ans=0
    # print(a)
    for i in range(n):
        x += 1 if s[i]=='R' else -1

        if x==0:
            ans = 1 + ((k-(i+1))//a if a!=-1 else 0)
            break
            
    
    print(ans)
