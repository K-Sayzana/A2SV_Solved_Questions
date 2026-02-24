te=int(input())

for _ in range(te):
    s=input()
    t=input()

    count=[0]*26
    for ch in t:
        count[ord(ch)-ord('a')]+=1
    
    
    flag=1
    for ch in s:
        if count[ord(ch)-ord('a')]==0:
            flag=0
            break
        count[ord(ch)-ord('a')]-=1
    
    if not flag or len(t)<len(s):
        print("Impossible")
        continue
    
    j=0
    ans=[]
    for ch in s:
        while chr(ord('a')+j) < ch:   
            ans.extend([chr(ord('a')+j)]*count[j])
            j+=1
        ans.append(ch)
    
    while j < 26:
        ans.extend([chr(ord('a')+j)]*count[j])
        j+=1

    print("".join(ans))


    
