class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(w):
            total=0
            ans=1
            for we in weights:
                if we>w:
                    return False
                if (total + we) > w:
                    ans+=1
                    total=0
                total+=we
            
            return ans <= days

        lo, hi=0, sum(weights)
        print(check(2))
        while hi-lo>1:
            m=(hi+lo)//2

            if check(m):
                hi=m
            else:
                lo=m
        

        return hi