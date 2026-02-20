class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)

        ans=0
        citations.sort()
        for i in range(1, n+1):
            for j in range(n):
                if citations[j]>=i:
                    if n-j>=i:
                        ans=i
                        break
        return ans




