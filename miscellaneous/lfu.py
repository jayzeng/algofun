import collections

# LFU cache
# from: https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.dummy = Node(None, None)
        self.dummy.next = self.dummy.prev = self.dummy
        self.size = 0
    
    def __len__(self):
        return self.size

    # O(1)
    def append(self, node):
        # append node to the end of the list
        # node.prev -> node -> node.next
        # self.dummy -> node -> self.dummy.next
        node.next = self.dummy.next
        node.prev = self.dummy
        node.next.prev = node

        self.dummy.next = node
        self.size += 1
    
    # O(1)
    def remove(self, node = None):
        if self.size == 0:
            return

        if not node:
            node = self.dummy.prev

        # node.prev -> node -> node.next
        node.prev.next = node.next 
        node.next.prev = node.prev
        self.size -= 1
        return node

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.node_map = {}
        self.min_freq = 0
        self.freq = collections.defaultdict(DoublyLinkedList)

    def _update(self, node):
        # keep track of the freq
        freq = node.freq
        self.freq[freq].remove(node)

        if self.min_freq == freq and not self.freq[freq]:
            self.min_freq += 1
        
        node.freq += 1
        freq = node.freq
        self.freq[freq].append(node)

    def get(self, key):
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return
        
        if key in self.node_map:
            node = self.node_map[key]
            self._update(node)
            node.val = value
            return
        
        if self.size == self.capacity:
            # remove the least frequently used node
            node = self.freq[self.min_freq].remove()
            del self.node_map[node.key]
            self.size -= 1
        
        # construct new node
        node = Node(key, value)
        self.node_map[key] = node
        node_freq = 1
        self.freq[node_freq].append(node)
        self.min_freq = 1
        self.size += 1
    
if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
    lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
    lfu.get(1)      # return 1
                    # cache=[1,2], cnt(2)=1, cnt(1)=2
    lfu.put(3, 3)   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                    # cache=[3,1], cnt(3)=1, cnt(1)=2
    lfu.get(2)      # return -1 (not found)
    lfu.get(3)      # return 3
                    # cache=[3,1], cnt(3)=2, cnt(1)=2
    lfu.put(4, 4)   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                    # cache=[4,3], cnt(4)=1, cnt(3)=2
    lfu.get(1)      # return -1 (not found)
    lfu.get(3)      # return 3
                    # cache=[3,4], cnt(4)=1, cnt(3)=3
    print(lfu.get(4))      # return 4
                    # cache=[4,3], cnt(4)=2, cnt(3)=3