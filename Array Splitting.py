n, k =map(int, input().split())

nums=list(map(int, input().split()))
nums.sort()

diff=[]

for i in range(n-1):
    diff.append(nums[i+1]-nums[i])

diff.sort(reverse=True)
total=sum(diff)

x=sum(diff[:k-1])
print(total-x)
