class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo, hi=0, max(candies)+1


        def check(x):
            ans=0
            for c in candies:
                ans+=(c//x)
            
            return ans>=k

        while hi-lo>1:
            m=(hi+lo)//2

            if check(m):
                lo=m
            else:
                hi=m
        

        return lo