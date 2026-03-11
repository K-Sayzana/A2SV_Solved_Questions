class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n-2):
            if nums[i]==0:
                nums[i]=1
                nums[i+1]=1-nums[i+1]
                nums[i+2]=1-nums[i+2]
                c+=1

        return c if (nums[-1]==nums[-2]==1) else -1