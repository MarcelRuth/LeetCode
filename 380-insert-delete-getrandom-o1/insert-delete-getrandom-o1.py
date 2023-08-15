class RandomizedSet:

    def __init__(self):
        self.s_map = {} # check for values
        # checking in map is faster than in list
        self.s = [] # store values
    def insert(self, val: int) -> bool:
        if val in self.s_map:
            return False
        else:
            self.s_map[val] = len(self.s) # index of value
            self.s.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.s_map:
            del self.s_map[val]
            self.s.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.s)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()