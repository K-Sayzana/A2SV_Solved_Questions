from collections import Counter

n, m=map(int, input().split())


a=list(map(int, input().split()))
b=list(map(int, input().split()))

count1=Counter(a)
count2=Counter(b)

ans=0
for k in count1:
    ans+= count1[k]*count2.get(k, 0)

print(ans)

    
