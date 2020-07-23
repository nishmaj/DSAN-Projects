# Problem 1  -- LRU cache

The LRU cache utilizes an internal doubly linked list (DLL) with two pointers ( head, tail ) to maintin the least-recently-used structure and a hash map or dictionary to retrieve items in the cache.

Hash map is being to store the cached values for instant retrieval of the node and value. Doubly linked list is to keep track of the most recently used values and size. This allows to quickly set the head(most recently used) and pop that back for removal.

Time complexity of get() is O(1) 
Since there is no loops hence constant time.

Space complexity of get() is O(1) 
Since only one variable is allocated

Time complexity of set() is O(1) 
Since there is no loops hence constant time

Space complexity of set() is O(n) 
Since the dictionary is as large as the amount of n keys.