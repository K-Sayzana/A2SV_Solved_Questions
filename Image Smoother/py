class Solution:

    def smooth(self, img, r, c):
        ans=0
        for i in range(max(0, r-1), min(r+2, len(img))):
            for j in range(max(0, c-1), min(c+2, len(img[0]))):
                ans+=img[i][j]

        row=min(len(img), r+2)-max(0, r-1)
        col=min(len(img[0]), c+2)-max(0, c-1)

        return ans//(col*row)

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        ans=[]
        for i in range(len(img)):
            row=[]
            for j in range(len(img[0])):
                row.append(self.smooth(img, i, j))
            ans.append(row)
        

        return ans
            

