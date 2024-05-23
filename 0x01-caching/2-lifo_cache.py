#!/usr/bin/env python3
"""LIFO_Cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implements a LIFO cache"""

    def __init__(self):
        """Initializer"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            if key in self.stack:
                self.stack.remove(key)
            elif len(self.cache_data) >= super().MAX_ITEMS:
                last = self.stack.pop()
                self.cache_data.pop(last)
                print(f"DISCARD: {last}")

            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key, None)
