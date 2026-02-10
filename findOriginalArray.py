class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if len(changed)==1 or len(changed)%2!=0:
            return []
        
        count=dict(Counter(changed))
        changed.sort()


        ans=[]
        for num in changed:
            if count[num]<=0:
                continue

            if count.get(num*2, 0):
                count[num]-=1
                count[num*2]-=1

                if count[num]>=0:
                    ans.append(num)
            else:
                return []

        return ans
