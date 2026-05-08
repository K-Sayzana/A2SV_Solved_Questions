class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res=[]
        N, M=len(nums1), len(nums2)


        if not nums1 or not nums2 or not k:
            return res
        
        pq=[(nums1[0]+nums2[1], 0, 0)]
        heapify(pq)
        visited=set((0, 0))

        while pq and len(res) < k:
            _ , i, j=heappop(pq)
            res.append([nums1[i], nums2[j]])

            if i + 1 < N and (i+1, j) not in visited:
                heappush(pq, (nums1[i+1]+nums2[j], i+1, j))
                visited.add((i+1, j))
            if j + 1 < M and (i, j+1) not in visited:
                heappush(pq, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))
        
        return res



        