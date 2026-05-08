class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
         N=len(matrix)
         ans=[]
         heapq.heapify(ans)

         for i in range(N):
            for j in range(N):
                heapq.heappush(ans, -1 * matrix[i][j])

                if len(ans) > k:
                    heapq.heappop(ans)
         return -1 * ans[0]
