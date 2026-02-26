n, s=map(int, input().split())
nums=list(map(int, input().split()))

total=0
l=0

ans=0

for r in range(n):
    total+=nums[r]

    while total-nums[l]>=s:
        total-=nums[l]
        l+=1
    if total >=s:
        ans+=l+1
    

print(ans)

