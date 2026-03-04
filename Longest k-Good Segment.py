from collections import defaultdict


n, k=map(int, input().split())
nums=list(map(int, input().split()))
l=0

ans=[-1, -1]
count=defaultdict(int)
long=0
for r in range(n):
    count[nums[r]]+=1

    while len(count)>k:
        count[nums[l]]-=1
        if count[nums[l]]==0:
            del count[nums[l]]
        l+=1

    if r-l+1 > long:
        long=r-l+1
        ans[0]=l+1
        ans[1]=r+1
    

print(*ans)



 
