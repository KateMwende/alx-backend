#!/usr/bin/env python3
"""
Least recently used algorithm
"""
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """Remove least recently used"""
    def __init__(self):
        """Initialize but with BaseCaching"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """Used to discard key"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            while self.queue:
                least_used = self.queue.popleft()
                if least_used in self.cache_data:
                    del self.cache_data[least_used]
                    break

            print("DISCARD: {}".format(least_used))
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Returns key in cached data"""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
