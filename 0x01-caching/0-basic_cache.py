#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system"""
    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
