class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        lo, hi=0, 1001
        N=len(citations)
        def check(x):
            idx=bisect_left(citations, x)
            return (N-idx)>=x

        while hi-lo>1:
            m=(hi+lo)//2
            if check(m):
                lo=m
            else:
                hi=m
        

        return lo