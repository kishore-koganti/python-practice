class ListNode:
    def __init__(self, key: None, value: None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity:int):
        self.key = None
        self.cache = None

    
        