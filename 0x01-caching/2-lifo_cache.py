#!/usr/bin/env python3
"""
Class FIFOCache that inherits from BaseCaching
"""

from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """Class that implements FIFO on cache data"""
    def __init__(self):
        """Initialize the class FIFOCache but with BaseCaching"""
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """Put the item in self.cache_data[key]"""
        if item is None or key is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                new_key = self.queue.pop()
                del self.cache_data[new_key]
                print("DISCARD: {}".format(new_key))
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get value of key in self.cache_data"""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
