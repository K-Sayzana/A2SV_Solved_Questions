class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        count1=Counter(s1)
        count2=Counter(s2)

        if (count1.get('x', 0) + count2.get('x', 0))%2!=0:
            return -1
        if (count1.get('y', 0) + count2.get('y', 0))%2!=0:
            return -1
        
        l1=[]
        l2=[]

        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                l1.append(s1[i])
                l2.append(s2[i])
        
        s1="".join(sorted(l1))
        s2="".join(sorted(l2, reverse=True))


        ans=0
        for i in range(0, len(s1)-1, 2):
            if s1[i]==s1[i+1]:
                ans+=1
            else:
                ans+=2
        

        return ans



        


