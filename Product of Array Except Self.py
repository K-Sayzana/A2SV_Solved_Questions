class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        for num in nums:
            prefix.append(prefix[-1]*num)
        
        suffix=[1]
        for num in nums[::-1]:
            suffix.append(suffix[-1]*num)
        suffix.reverse()

        ans=[]
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i+1])
        

        return ans
