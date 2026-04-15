class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N=len(nums)

        for i in range(N):

            while i != nums[i] and nums[i] < N:
                ci=nums[i]
                nums[i], nums[ci]=nums[ci], nums[i]
            
        for i in range(N):
            if i!=nums[i]:
                return i
            
        return N



