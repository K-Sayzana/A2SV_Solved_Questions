class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        

        min_q=deque()
        max_q=deque()

        l=0
        ans=0
        for r, num in enumerate(nums):

            while max_q and nums[max_q[-1]] < num:
                max_q.pop()
            
            while min_q and nums[min_q[-1]] > num:
                min_q.pop()

            max_q.append(r)
            min_q.append(r)

            while nums[max_q[0]]-nums[min_q[0]]>limit:
                if max_q[0]==l:
                    max_q.popleft()
                if min_q[0]==l:
                    min_q.popleft()
                l+=1
            
            ans=max(ans, r-l+1)
        

        return ans




