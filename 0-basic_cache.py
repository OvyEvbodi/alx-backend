#!/usr/bin/env python3

""" Inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    
    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key) if key and key in self.cache_data else None
        