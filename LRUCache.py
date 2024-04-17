from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value
    
    def put(self, key:int, value:int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


cache = LRUCache(3)
cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))
cache.put(3,3)

print(cache.get(2))
cache.put(4, 4)

print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

