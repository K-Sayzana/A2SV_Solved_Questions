class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N=len(nums)

        for i in range(N):

            while i+1 != nums[i] and nums[nums[i]-1]!=nums[i]:
                di=nums[i]-1
                nums[i], nums[di]=nums[di], nums[i]
        

        for i in range(N):
            if i+1!=nums[i]:
                return[nums[i], i+1]