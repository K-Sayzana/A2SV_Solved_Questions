from collections import defaultdict, Counter

t=int(input())

for _ in range(t):
    n=int(input())
    s=input()

    ans=-1
    if len(s)<2:
        ans=-1
    elif 'aa' in s:
        ans=2
    elif 'aba' in s or 'aca' in s:
        ans=3
    elif 'abca' in s or 'acba' in s:
        ans=4

    elif 'abbacca' in s or 'accabba' in s:
        ans=7
        
        

    print(ans)
