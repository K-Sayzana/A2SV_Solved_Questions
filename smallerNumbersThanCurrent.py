class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_=[x for x in nums]

        nums.sort()
        count={}
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                count[nums[i]]=i
        
        for i in range(len(nums)):
            nums_[i]=count[nums_[i]]
        
        return nums_
