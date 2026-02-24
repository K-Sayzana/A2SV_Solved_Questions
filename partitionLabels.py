class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        max_r=-1
        ans=[]
        for i in range(len(s)):
            max_r=max(max_r, s.rindex(s[i]))

            if max_r==i:
                ans.append(i+1-sum(ans))

        return ans
