class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        order_map=defaultdict(int)
        for i in range(len(order)):
            order_map[order[i]]=i

        return  "".join(sorted(list(s), key=lambda x: order_map[x]))

        
