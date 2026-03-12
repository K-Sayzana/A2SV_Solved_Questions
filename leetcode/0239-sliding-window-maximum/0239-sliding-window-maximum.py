class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N=len(nums)
        win=deque()
        ans=[]
        for i in range(N):
            
            if win and win[0] <= i - k:
                win.popleft()
            while win and nums[win[-1]] <= nums[i]:
                win.pop()
            
            win.append(i)

            if i >= k-1:
                ans.append(nums[win[0]])
        

        return ans
        

            
            
