class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum=sum(filter(lambda x: x%2==0, nums))


        ans=[]
        for q in queries:
            if nums[q[1]]%2==0:
                even_sum-=nums[q[1]]
            nums[q[1]]+=q[0]

            if nums[q[1]]%2==0:
                even_sum+=nums[q[1]]
            
            ans.append(even_sum)
        

        return ans
            

       
