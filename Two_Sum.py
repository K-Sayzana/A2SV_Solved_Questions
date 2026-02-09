class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        nums=list(enumerate(nums))
        nums=sorted(nums, key=lambda x: x[1])

        i=0
        j=len(nums)-1

        while j>i:

            sum_=nums[i][1]+nums[j][1]
            if sum_==target:
                return [nums[i][0], nums[j][0]]
            elif sum_>target:
                j-=1
            else:
                i+=1
       
        
            
