class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N=len(nums)

        for i in range(N):
            while nums[i] < N and  nums[i] > 0 and nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
                di=nums[i]-1
                nums[i], nums[di]=nums[di], nums[i]
        
        for i in range(N):
            if i+1 != nums[i]:
                return i + 1

        return N+1




