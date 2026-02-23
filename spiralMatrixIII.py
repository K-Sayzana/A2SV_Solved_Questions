class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        r, c = rStart, cStart
        step_size = 1
        
        while len(res) < rows * cols:
            # Move Right
            for _ in range(step_size):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            # Move Down
            for _ in range(step_size):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            step_size += 1
            
            # Move Left
            for _ in range(step_size):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
                    
            # Move Up
            for _ in range(step_size):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            
            step_size += 1
            
        return res
