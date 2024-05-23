"""MRU_Cache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implements a MRU cache"""

    def __init__(self):
        """Initializer"""
        super().__init__()
        # list of keys from least recent to most recent
        self.recently_used = []

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            if key in self.recently_used:
                self.recently_used.remove(key)
            elif len(self.cache_data) >= super().MAX_ITEMS:
                discard = self.recently_used.pop()
                self.cache_data.pop(discard)
                print(f"DISCARD: {discard}")

            self.cache_data[key] = item
            self.recently_used.append(key)

    def get(self, key):
        """Get an item by key
        """
        if key in self.recently_used:
            self.recently_used.remove(key)
            self.recently_used.append(key)
        return self.cache_data.get(key, None)
