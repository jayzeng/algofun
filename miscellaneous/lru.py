import collections

from pyparsing import col

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
    
    # helper function to update the cache
    def update(self, key, value):
        if key in self.cache:
            del self.cache[key]
        
        self.cache[key] = value

    def get(self, key):
        if key not in self.cache:
            return -1
        
        val = self.cache[key]
        # maintain the order of the cache
        # e.g.: 
        # {1=1, 2=2} => after get(1) {2=2, 1=1}
        self.update(key, val)
        return val
    
    def put(self, key, value):
        if key not in self.cache and len(self.cache) == self.capacity:
            # remove the 1st element
            self.cache.popitem(last=False)
        
        self.update(key, value)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        node.prev, node.next = None, None

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.next, node.prev = None, None

class LRUCache2:
    def __init__(self, capacity):
        self.list = LinkedList()
        self.cache = {}
        self.capcity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1

        val = self.cache[key].val
        self.update(key, val)
        return val

    def put(self, key, val):
        if key not in self.cache and len(self.cache) == self.capcity:
            del self.cache[self.list.head.key]
            self.list.remove(self.list.head)
        
        self.update(key, val)

    def update(self, key, val):
        if key in self.cache:
            self.list.remove(self.cache[key])
        
        node = Node(key, val)
        self.list.append(node)
        self.cache[key] = node

if __name__ == "__main__":
    lRUCache = LRUCache2(2)
    lRUCache.put(1, 1) # cache is {1=1}
    lRUCache.put(2, 2) # cache is {1=1, 2=2}
    lRUCache.get(1)    # return 1
    lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2)    # returns -1 (not found)
    lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1)    # return -1 (not found)
    lRUCache.get(3)    # return 3
    print(lRUCache.get(4))    # return 4