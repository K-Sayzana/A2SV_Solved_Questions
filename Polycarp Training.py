n=int(input())

nums=list(map(int, input().split()))
nums.sort()


i=1
ans=0
for num in nums:
    if num>=i:
        ans+=1
        i+=1
   


print(ans)
