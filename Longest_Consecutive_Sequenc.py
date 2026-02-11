class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_=set(nums)

        ans=0
        for num in nums_:
            if num-1 not in nums_:
                len_=0
            
                while num in nums_:
                    len_+=1
                    num+=1
                ans=max(ans, len_)


        return ans   

