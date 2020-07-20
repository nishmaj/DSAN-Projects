"""
    Double Linked List Node to keep the key and value of the entry
    in the cache memory.
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

"""
    LRUCache utilizes an internal doubly linked list
    to maintain the least-recently-used structure:
    the head stores the Node with the most recently used key,
    and the tail stores the Node with the least recently used key.
"""

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.current_size = 0
        self.cache = {}
        self.head = None
        self.tail = None

        #pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._set_head(node)
            return node.value
        else:
            return -1
        #pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.current_size == self.capacity:
            self._remove_LRU()
        new_node = Node(value)
        self.cache[key] = new_node
        self._set_head(new_node)
        self.current_size += 1
        #pass


    def _remove_LRU(self):
        node = self.tail
        del self.cache[node.value]
        self._remove_node(node)
        self.current_size -= 1


    def _set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next = node
            node.prev = self.head
            if self.head.prev == None:
                self.tail = self.head
            self.head = node
        
    def _remove_node(self, node):
        if self.current_size == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.prev
            self.head.next = None
        elif node == self.tail:
            self.tail.next.prev = None
            self.tail = self.tail.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
