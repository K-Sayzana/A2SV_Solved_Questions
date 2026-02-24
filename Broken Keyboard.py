

t=int(input())


for _ in range(t):
    s=input()


    ans=[0]*26
    i=0
    while i<len(s):
        if i < len(s)-1 and s[i]==s[i+1]:
            i+=2
        else:
            ans[ord(s[i])-ord('a')]=1
            i+=1
    

    res=[ chr(ord('a')+i) for i in range(len(ans)) if ans[i]==1]

    print("".join(res))
