class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:  

        n=len(nums)
        count=[0] * n

        for req in requests:
            l, r = req
            count[l]+=1
            if r+1 < n:
                count[r+1]-=1
        
        for i in range(1, n):
            count[i]+=count[i-1]
        
        count.sort(reverse=True)
        nums.sort(reverse=True)
        
        ans=0

        for i in range(len(nums)):
            ans+=((nums[i]*count[i]))
        return ans  % 1000000007
