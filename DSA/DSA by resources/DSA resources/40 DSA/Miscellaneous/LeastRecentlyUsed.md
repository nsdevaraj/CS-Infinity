

Implement a LRU (Least Recently Used) cache.


## What is an LRU Cache?

An **LRU (Least Recently Used) Cache** is a data structure that stores a limited number of items and automatically evicts the least recently used item when the cache reaches its capacity. The LRU cache is often implemented to optimize resource usage in situations where memory is limited, allowing frequently accessed items to be stored for quick retrieval.

### How LRU Cache Works

1. **Capacity**: It has a maximum capacity set at initialization.
2. **Storage**: Uses a combination of a dictionary (for O(1) access) and a doubly linked list (to track the order of usage).
3. **Eviction Policy**: When the cache exceeds its capacity, the least recently accessed item is removed.

### Example

Imagine a scenario where you have a web application that frequently accesses user data. You want to cache user profiles to reduce database queries.

1. **Initialize Cache**: Set up an LRU cache with a capacity of 2.
   - **Operations**:
     - Add user profile for User A: `{A: ProfileA}`
     - Add user profile for User B: `{A: ProfileA, B: ProfileB}`
     - Access User A: `{B: ProfileB, A: ProfileA}` (User A is now the most recently used)
     - Add user profile for User C: `{A: ProfileA, C: ProfileC}` (User B is evicted as it was the least recently used)

### Usage

- **Web Browsers**: To cache web pages, images, and other resources.
- **Database Systems**: To cache query results for faster access.
- **Operating Systems**: To manage memory and cache frequently accessed files.
- **Applications**: Any scenario where quick access to data is critical, such as machine learning models, APIs, etc.

### Pros and Cons

#### Pros

1. **Efficiency**: Fast O(1) time complexity for both `get` and `put` operations.
2. **Memory Management**: Automatically evicts the least recently used items, optimizing memory usage.
3. **Performance**: Reduces latency for frequently accessed items, improving overall performance.

#### Cons

1. **Overhead**: Requires additional memory for the linked list structure.
2. **Complexity**: More complex to implement compared to simple caching strategies (like FIFO or static caches).
3. **Potential for Thrashing**: If the access patterns are not stable, frequently used items can be evicted if they are not accessed soon enough.

### Summary

An LRU Cache is a practical solution for managing limited resources effectively by keeping track of the usage patterns of items. Its implementation is commonly used in various applications to ensure efficient data retrieval while managing memory constraints. However, the overhead and complexity should be considered based on the application's needs.


## Implementation

Implementing an LRU (Least Recently Used) cache in Python can be efficiently done using a combination of a dictionary and a doubly linked list. The dictionary allows for O(1) access to cache items, while the linked list keeps track of the order of usage.

Here’s how to implement an LRU Cache:

### LRU Cache Implementation

```python
class Node:
    """A node in the doubly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        """Add a node right after the head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """Return the value of the key if the key exists, otherwise return -1."""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """Update the value of the key if the key exists, otherwise add the key-value pair."""
        if key in self.cache:
            self._remove(self.cache[key])

        new_node = Node(key, value)
        self._add_to_head(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            # Remove the least recently used item (the node before the tail)
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

# Example usage
lru_cache = LRUCache(2)
lru_cache.put(1, 1)      # cache is {1=1}
lru_cache.put(2, 2)      # cache is {1=1, 2=2}
print(lru_cache.get(1))   # returns 1
lru_cache.put(3, 3)      # LRU key was 2, remove key 2, cache is {1=1, 3=3}
print(lru_cache.get(2))   # returns -1 (not found)
lru_cache.put(4, 4)      # LRU key was 1, remove key 1, cache is {4=4, 3=3}
print(lru_cache.get(1))   # returns -1 (not found)
print(lru_cache.get(3))   # returns 3
print(lru_cache.get(4))   # returns 4
```

### Explanation:

1. **Node Class**: Represents a single node in the doubly linked list with `key`, `value`, `prev`, and `next` pointers.

2. **LRUCache Class**:
   - **Initialization**: Sets the cache capacity, initializes a dictionary for quick access, and sets up a doubly linked list with dummy head and tail nodes.
   - **_remove(node)**: Removes a node from the linked list.
   - **_add_to_head(node)**: Adds a node right after the head of the linked list.
   - **get(key)**: If the key exists, it retrieves the value, removes the node from its current position, and adds it to the head (marking it as recently used). If not found, it returns -1.
   - **put(key, value)**: Adds or updates a key-value pair. If adding a new key exceeds capacity, it removes the least recently used item (the node before the tail).

### Usage:
You can create an instance of `LRUCache` and use the `put` and `get` methods to interact with the cache as shown in the example usage section.




ToDo:
Least Frequestly used - implementation
