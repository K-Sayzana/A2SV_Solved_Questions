t=int(input())

for _ in range(t):
    n, k=map(int, input().split())
    s=input()

    black=0
    white=0

    for i in range(k):
        if s[i]=='B':
            black+=1
        else:
            white+=1
    
    l=0
    ans=white
    for i in range(k, n):
        if s[i]=='B':
            black+=1
        else:
            white+=1
        
        if s[l]=='B':
            black-=1
        else:
            white-=1
        l+=1
        
        ans=min(ans, white)

    print(ans)
