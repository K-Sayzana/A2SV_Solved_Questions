class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=dict(Counter(nums))

        max_eles=[]

        for ke, v in count.items():
            if len(max_eles)<k:
                max_eles.append(ke)
            else:
                idx=0
                for i in range(1, len(max_eles)):
                    if count[max_eles[i]]<count[max_eles[idx]]:
                        idx=i
                if v>count[max_eles[idx]]:
                    max_eles[idx]=ke
                
        

        return max_eles




