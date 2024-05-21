#!/usr/bin/env python3
"""Basic_Cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implements a basic cache"""

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key, None)
