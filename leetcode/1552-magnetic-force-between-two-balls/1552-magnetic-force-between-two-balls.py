class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        lo, hi= 0 , max(position)

        def check(x):
            prev=position[0]
            c=1
            for p in position[1:]:
                if p>=prev+x:
                    prev=p
                    c+=1
            return c>=m




        while hi-lo>1:
            mid=(hi+lo)//2
            if check(mid):
                lo=mid
            else:
                hi=mid
        

        return lo