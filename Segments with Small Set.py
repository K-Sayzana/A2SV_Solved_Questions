from collections import defaultdict

n, k=map(int, input().split())
nums=list(map(int, input().split()))

count=defaultdict(int)

l=0
ans=0
for r in range(n):
    count[nums[r]]+=1

    while len(count)>k:
        count[nums[l]]-=1
        if count[nums[l]]==0:
            del count[nums[l]]
        l+=1
    
    ans+=r-l+1


print(ans)
    
    
