class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        lo, hi=-1, len(matrix)


        while hi-lo>1:
            m=(hi+lo)//2
            idx=bisect_left(matrix[m], target)
            if idx==len(matrix[0]):
                lo=m
            elif matrix[m][idx]!= target:
                hi=m
            else:
                return True


        return False



