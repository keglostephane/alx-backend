#!/usr/bin/python3
""" LFUUCache module
"""
from collections import defaultdict, OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFU CLASS
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.freq_item = defaultdict(OrderedDict)
        self.key_freq = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_freq(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict()
            self.cache_data[key] = item
            self.key_freq[key] = 1
            self.freq_item[1][key] = True

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self._update_freq(key)
        return self.cache_data[key]

    def _update_freq(self, key):
        """ Update the frequency of a key """
        freq = self.key_freq[key]
        del self.freq_item[freq][key]
        if not self.freq_item[freq]:
            del self.freq_item[freq]
        self.key_freq[key] = freq + 1
        self.freq_item[freq + 1][key] = True

    def _evict(self):
        """ Evict the least frequently used item """
        min_freq = min(self.freq_item)
        lfu_keys = self.freq_item[min_freq]
        lru_key, _ = lfu_keys.popitem(last=False)
        if not self.freq_item[min_freq]:
            del self.freq_item[min_freq]
        del self.cache_data[lru_key]
        del self.key_freq[lru_key]
        print("DISCARD: " + lru_key)
