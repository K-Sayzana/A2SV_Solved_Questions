n, s=map(int, input().split())
nums=list(map(int, input().split()))

total=0
l=0

ans=0
for r in range(n):
    total+=nums[r]

    while total>s:
        total-=nums[l]
        l+=1
    
    ans+=r-l+1


print(ans)
