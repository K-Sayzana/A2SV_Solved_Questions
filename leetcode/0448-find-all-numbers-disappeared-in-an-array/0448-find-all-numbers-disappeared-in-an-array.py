class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N=len(nums)

        for i in range(N):
            while i+1!=nums[i] and nums[nums[i]-1]!=nums[i]:
                di=nums[i]-1
                nums[i], nums[di]=nums[di], nums[i]
        


        ans=[]
        for i in range(N):
            if nums[i]!=i+1:
                ans.append(i+1)


        return ans
        

