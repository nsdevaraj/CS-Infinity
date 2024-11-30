from typing import Optional

class Node:
    def __init__(self, key:Optional[int], value:Optional[int]):
        self.key:Optional[int] = key
        self.value:Optional[int] = value
        self.prev: Optional[Node]  = None
        self.next: Optional[Node] = None

class LRU_Err(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    @staticmethod
    def capacity_invalid(capacity):
        return LRU_Err(f"Invalid capacity({capacity}) - should be above 0")


class LRUCache:
    def __init__(self, capacity:int):
        if(capacity < 1):
            raise LRU_Err.capacity_invalid(capacity)
        self.capacity = capacity
        self.keyMap = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _print(self):
        current = self.head.next  # Start from the first real node
        elements = []
        while current and current != self.tail:  # Stop before the tail
            elements.append(f"{current.key}={current.value}")
            current = current.next
        print(f"[ {', '.join(elements)} ]")


    def _remove(self, node:Node):
        node_prev = node.prev
        node_next = node.next

        if node_prev is not None:
            node_prev.next = node_next

        if node_next is not None:
            node_next.prev = node_prev

        if(self.head.next == node):
            self.head.next = node_next


    def _add_to_tail(self, node:Node):
        node.prev = self.tail.prev
        node.next = self.tail

        if node.prev is not None:
            node.prev.next = node
        self.tail.prev = node


    def put(self, key:int, value:int):

        node = self.keyMap.get(key)
        if(node):
            node.value = value
            if(self.tail.prev != node):
                self._remove(node)
                self._add_to_tail(node)
        else:
            node = Node(key,value)
            self.keyMap[key] = node
            self._add_to_tail(node)

            if len(self.keyMap) > self.capacity:
                lru_node = self.head.next
                if lru_node is not None:
                    self._remove(lru_node)
                    del self.keyMap[lru_node.key]
        self._print()

    def get(self, key:int)->int:
        node = self.keyMap.get(key)
        if node:
            if(not self.tail.prev == node):
                self._remove(node)
                self._add_to_tail(node)
            return node.value
        else:
            return -1


# lru_cache = LRUCache(2)
# lru_cache.put(1, 1)      # cache is {1=1}
# print(lru_cache.get(1))  # return 1
# lru_cache.put(2, 2)      # cache is {1=1, 2=2}
# print(lru_cache.get(1))   # returns 1
# lru_cache.put(3, 3)      # LRU key was 2, remove key 2, cache is {1=1, 3=3}
# print(lru_cache.get(2))   # returns -1 (not found)
# lru_cache.put(4, 4)      # LRU key was 1, remove key 1, cache is {4=4, 3=3}
# print(lru_cache.get(1))   # returns -1 (not found)
# print(lru_cache.get(3))   # returns 3
# print(lru_cache.get(4))   # returns 4


# lru_cache = LRUCache(3)
# lru_cache.put(1, 10)      # cache is {1=10}
# lru_cache.put(2, 20)      # cache is {1=10, 2=20}
# lru_cache.put(3, 30)      # cache is {1=10, 2=20, 3=30}
# print(lru_cache.get(2))   # returns 20
# lru_cache.put(4, 40)      # LRU key was 1, remove key 1, cache is {2=20, 3=30, 4=40}
# print(lru_cache.get(1))   # returns -1 (not found)
# print(lru_cache.get(3))   # returns 30
# print(lru_cache.get(4))   # returns 40
# lru_cache.put(5, 50)      # LRU key was 2, remove key 2, cache is {3=30, 4=40, 5=50}
# print(lru_cache.get(2))   # returns -1 (not found)


# lru_cache = LRUCache(2)
# lru_cache.put(10, 100)    # cache is {10=100}
# lru_cache.put(20, 200)    # cache is {10=100, 20=200}
# print(lru_cache.get(10))   # returns 100
# lru_cache.put(30, 300)    # LRU key was 20, remove key 20, cache is {10=100, 30=300}
# print(lru_cache.get(20))   # returns -1 (not found)
# lru_cache.put(40, 400)    # LRU key was 10, remove key 10, cache is {30=300, 40=400}
# print(lru_cache.get(10))   # returns -1 (not found)
# print(lru_cache.get(30))   # returns 300
# print(lru_cache.get(40))   # returns 400


# lru_cache = LRUCache(5)
# lru_cache.put(1, 1)        # cache is {1=1}
# lru_cache.put(2, 2)        # cache is {1=1, 2=2}
# lru_cache.put(3, 3)        # cache is {1=1, 2=2, 3=3}
# lru_cache.put(4, 4)        # cache is {1=1, 2=2, 3=3, 4=4}
# lru_cache.put(5, 5)        # cache is {1=1, 2=2, 3=3, 4=4, 5=5}
# lru_cache.put(6, 6)        # LRU key was 1, remove key 1, cache is {2=2, 3=3, 4=4, 5=5, 6=6}
# print(lru_cache.get(1))     # returns -1 (not found)
# print(lru_cache.get(2))     # returns 2
# print(lru_cache.get(3))     # returns 3
# lru_cache.put(7, 7)        # LRU key was 4, remove key 4, cache is {2=2, 3=3, 5=5, 6=6, 7=7}
# print(lru_cache.get(4))     # returns -1 (not found)


# lru_cache = LRUCache(1)
# lru_cache.put(1, 10)       # cache is {1=10}
# print(lru_cache.get(1))     # returns 10
# lru_cache.put(2, 20)       # LRU key was 1, remove key 1, cache is {2=20}
# print(lru_cache.get(1))     # returns -1 (not found)
# print(lru_cache.get(2))     # returns 20


lru_cache = LRUCache(1)

# Initially putting a key-value pair
lru_cache.put(1, 100)       # cache is {1=100}
print(lru_cache.get(1))     # returns 100

# Putting a new key-value pair, should evict the previous one
lru_cache.put(2, 200)       # LRU key was 1, remove key 1, cache is {2=200}
print(lru_cache.get(1))     # returns -1 (not found)
print(lru_cache.get(2))     # returns 200

# Putting another key-value pair, evicting the current one
lru_cache.put(3, 300)       # LRU key was 2, remove key 2, cache is {3=300}
print(lru_cache.get(2))     # returns -1 (not found)
print(lru_cache.get(3))     # returns 300

# Try to put a key that is already present
lru_cache.put(3, 350)       # updates the value of key 3
print(lru_cache.get(3))     # returns 350

# Adding another key-value, which will evict the current one
lru_cache.put(4, 400)       # LRU key was 3, remove key 3, cache is {4=400}
print(lru_cache.get(3))     # returns -1 (not found)
print(lru_cache.get(4))     # returns 400
