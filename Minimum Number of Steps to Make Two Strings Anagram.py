class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count=Counter(s)
        # t_count=Counter(t)


        ans=0
        for ch in t:
            if not s_count.get(ch, 0):
                ans+=1
            else:
                s_count[ch]-=1
        
        return ans
