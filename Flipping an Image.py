class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            image[i]=list(map(lambda x: int(not x), reversed(image[i])))

        return image
