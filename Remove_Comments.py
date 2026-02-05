class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        in_block = False
        new_line = []
        
        for line in source:
            i = 0
            if not in_block:
                new_line = []
            
            while i < len(line):
                if not in_block and line[i:i+2] == '/*':
                    in_block = True
                    i += 1
                elif in_block and line[i:i+2] == '*/':
                    in_block = False
                    i += 1
                elif not in_block and line[i:i+2] == '//':
                    break
                elif not in_block:
                    new_line.append(line[i])
                i += 1
            
            if not in_block and len(new_line)>0:
                ans.append("".join(new_line))
                
        return ans
