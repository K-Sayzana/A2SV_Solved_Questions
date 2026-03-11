class DataStream:

    def __init__(self, value: int, k: int):
        self.queue=deque()
        self.k=k
        self.value=value
        self.c=0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if len(self.queue)>self.k:
            if self.queue[0]==self.value:
                self.c-=1
            self.queue.popleft()
        
        if num==self.value:
            self.c+=1


        return self.c==self.k
        
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)