class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi=-1, len(nums)

        while hi-lo>1:
            m=(hi+lo)//2

            if nums[m]>target:
                hi=m
            else:
                lo=m
        
        if lo!=-1 and nums[lo]==target:
            return lo
        else:
            return lo+1