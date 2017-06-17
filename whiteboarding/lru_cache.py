#!/usr/bin/python3
"""
Implement a LRU Cache with these functions
interface LRUCache() {
Get(key string) interface{}
Set(key string, value interface{})
Remove(key string)
Clear()
Size()
}
"""
class LruCache():
    def __init__(self, size=4):
        self.size = size
        self.cache = []

    def get(self, key):
        """
        The get function has to check item in the list
        """
        for i in range(len(self.cache)):
            if self.cache[i].get(key, None) != None:
                item = self.cache.pop(i)
                self.cache.insert(0, item)
                return item[key]
        for item in self.cache:
            if item.get(key, None) != None:
                return item[key]
        return None

    def set(self, key=None, value=None):
        """
        checks the size of the cache, and updates the value if need be
        """
        if key is None or value is None:
            return "missing key and/or value"
        key_exist = False
        for item in self.cache:
            if item.get(key, None) != None:
                item = self.cache.pop(i)
                item[key] = value
                self.cache.insert(0, item)
                update_item = True
        if key_exist is False:
            if len(self.cache) == self.size:
                self.cache.pop()
            self.cache.insert(0, {key:value})

    def remove(self, key=None):
        """
        Remove the item from the cache
        """
        if key is None:
            return "no key given"
        for i in range(len(self.cache)):
            if self.cache[i].get(key, None) != None:
                item.pop(i)
                return "item removed"
        return "item not in cache"

    def size(self):
        """
        return the size of the cache
        """
        return len(self.cache)

    def clear(self):
        """
        clear the cache
        """
        self.cache = []
