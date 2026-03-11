class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N=len(heights)
        stack=[]
        prev_less=[]

        for i in range(N):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()

            prev_less.append(stack[-1] if stack else -1)
            stack.append(i)
        
        next_less=[]
        stack=[]

        for i in range(N-1, -1, -1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()

            next_less.append(stack[-1] if stack else N)
            stack.append(i)
        next_less.reverse()
        
        ans=0
        for i in range(N):
            ans=max(ans, heights[i]* ((next_less[i]-1)-(prev_less[i]+1)+1))
        # print(next_less, prev_less)
        return ans


        
        

