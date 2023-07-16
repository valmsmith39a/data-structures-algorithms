
class LRUCache:
    """
    Problem: LRU Cache #146

    Key Insight:
    1. Use Hash Map to map key to nodes containing a key and value and connected in a doubly linked list 
    2. Use dummy left node to track least recently used node and dummy right node to track most recently used node 

    Time Complexity: 
    1. insert (into linked list): O(1) 
    2. remove (from linked list): O(1)
    3. get: 
        a. Get from cache is O(1)
        b. remove / insert from / to doubly linked list is O(1)
    4. put: 
        a. Put in cache is O(1), bc bounded by capacity 
        b. remove / insert from / to doubly linked list is O(1)

    Space Complexity: 
    1. insert: O(1)
    2. remove: O(1)
    3. get: O(1)
    4. put: O(1)
    """

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev 

        self.right.prev.next = node 
        self.right.prev = node 
    
    def remove(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev 

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val 
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap: 
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.next = self.prev = None