#!/usr/bin/env python3
"""FIFO_Cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implements a FIFO cache"""

    def __init__(self):
        """Initializer"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > super().MAX_ITEMS:
                discard = next(iter(self.cache_data.keys()))
                self.cache_data.pop(discard)
                print(f"DISCARD: {discard}")

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key, None)
