from collections import OrderedDict

class LRUCache:
# create a cache with capacity 2

    cache = LRUCache(2)

# add two items to the cache
cache.put(1, 'one')
cache.put(2, 'two')

# retrieve an item from the cache
print(cache.get(1))  # Output: 'one'

# add a third item to the cache (evicts the least recently used item)
cache.put(3, 'three')

# try to retrieve the evicted item (should return -1)
print(cache.get(2))  # Output: -1
