#!/usr/bin/python3
from lru_cache import LruCache

lru = LruCache(3)
lru.set("test1", {1:2})
lru.set("test2", {2:4})
lru.set("test3", {3:5})
print("Inside the cache {}".format(lru.cache))
lru.set("test4", {1:2})
print("Inside the cache {}".format(lru.cache))
print(lru.get("test2"))
print("Inside the cache {}".format(lru.cache))
lru.set("test5", {5:6})
print("Inside the cache {}".format(lru.cache))
