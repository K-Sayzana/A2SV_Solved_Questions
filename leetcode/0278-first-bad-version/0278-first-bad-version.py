# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi=-1, n

        while hi-lo>1:
            m=(hi+lo)//2

            if isBadVersion(m):
                hi=m
            else:
                lo=m
        

        return hi

        