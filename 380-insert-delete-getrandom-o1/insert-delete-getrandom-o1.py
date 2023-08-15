class RandomizedSet:

    def __init__(self):
        self.s = []

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        else:
            self.s.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.s[random.randint(0, len(self.s)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()