class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        for i in range(4):
            for r in range(len(mat)):
                for c in range(len(mat[0])):
                    if c>r:
                        mat[r][c], mat[c][r]=mat[c][r], mat[r][c]
            
            for row in mat:
                row.reverse()
            
            if mat==target:
                return True
        

        return False
