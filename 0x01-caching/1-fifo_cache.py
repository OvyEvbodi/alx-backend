#!/usr/bin/env python3

""" Inherits from BaseCaching and is a FIFO caching system
"""

BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_item = next(iter(self.cache_data))
                del self.cache_data[discarded_item]
                print('DISCARD: {}'.format(discarded_item))

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
        
