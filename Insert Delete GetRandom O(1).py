import random

class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        self.indices[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        last_val = self.data[-1]
        idx_to_remove = self.indices[val]

        self.data[idx_to_remove] = last_val
        self.indices[last_val] = idx_to_remove

        self.data.pop()
        del self.indices[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
