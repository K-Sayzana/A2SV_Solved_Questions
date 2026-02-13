class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans=[]

        upper=defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                    upper[r+c].append(mat[r][c])
    
        
        for k, v in upper.items():
            if k % 2!=0:
                ans.extend(v)
            else:
                ans.extend(v[::-1])
        

        return ans
