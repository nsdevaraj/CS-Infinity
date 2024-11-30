


Here's the problem statement for the LRU Cache, organized clearly:

## LRU Cache

### Problem Statement

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

### Class Definition

Implement the `LRUCache` class:

```python
class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the LRU cache with positive size capacity.
        pass

    def get(self, key: int) -> int:
        # Return the value of the key if the key exists, otherwise return -1.
        pass

    def put(self, key: int, value: int) -> None:
        # Update the value of the key if the key exists. 
        # Otherwise, add the key-value pair to the cache.
        # If the number of keys exceeds the capacity from this operation,
        # evict the least recently used key.
        pass
```

### Constraints

- \( 1 \leq \text{capacity} \leq 3000 \)
- \( 0 \leq \text{key} \leq 10^4 \)
- \( 0 \leq \text{value} \leq 10^5 \)
- At most \( 2 \times 10^5 \) calls will be made to `get` and `put`.


```python
# Constraints
capacity = 3000  # 1 <= capacity <= 3000
key = 10000      # 0 <= key <= 10^4
value = 100000   # 0 <= value <= 10^5
max_calls = 200000  # At most 2 * 10^5 calls will be made to `get` and `put`.
```
### Example

#### Input

```plaintext
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
```

#### Output

```plaintext
[null, null, null, 1, null, -1, null, -1, 3, 4]
```

#### Explanation

1. `LRUCache lRUCache = new LRUCache(2);`
2. `lRUCache.put(1, 1);` // cache is {1=1}
3. `lRUCache.put(2, 2);` // cache is {1=1, 2=2}
4. `lRUCache.get(1);`    // returns 1
5. `lRUCache.put(3, 3);` // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
6. `lRUCache.get(2);`    // returns -1 (not found)
7. `lRUCache.put(4, 4);` // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
8. `lRUCache.get(1);`    // returns -1 (not found)
9. `lRUCache.get(3);`    // returns 3
10. `lRUCache.get(4);`   // returns 4

### Key Points

- The `get` and `put` methods must run in O(1) average time complexity.
- The cache should evict the least recently used item when it reaches its capacity limit.

This arrangement clearly outlines the problem, class structure, constraints, and example usage for the LRU Cache problem.


### Soln


```js
class Node:
    method __init__(key: Optional[int], value: Optional[int]):
        // Initialize node properties

class LRU_Err(Exception):
    method __init__(args: object):
        // Initialize error with args

    static method capacity_invalid(capacity):
        // Return capacity error message

class LRUCache:
    method __init__(capacity: int):
        // Initialize cache with capacity and set up linked list

    method _print():
        // Print current cache state

    method _remove(node: Node):
        // Remove node from linked list

    method _add_to_tail(node: Node):
        // Add node to the tail of the linked list

    method put(key: int, value: int):
        // Add or update value for key in cache
        // If capacity exceeded, remove least recently used item
        // Print cache state

    method get(key: int) -> int:
        // Retrieve value for key, move node to tail if found
        // Return -1 if not found

```


we can use linkedList or orderedDict based on our preferences
### Ordered Dict

`OrderedDict` is a specialized dictionary class from the `collections` module in Python that maintains the order of keys based on the order they were added. This means that when you iterate over the keys, values, or items of an `OrderedDict`, they will be returned in the order they were inserted.

### Key Features of `OrderedDict`:

1. **Order Preservation**: Unlike a regular dictionary (prior to Python 3.7, where insertion order is also preserved), an `OrderedDict` guarantees that the order of items is maintained.

2. **Performance**: It provides the same average time complexity for lookups, insertions, and deletions as a regular dictionary, which is O(1).

3. **Additional Methods**: `OrderedDict` includes some extra methods that are useful for maintaining order, such as:
   - `move_to_end(key)`: Moves an existing key to the end of the dictionary, marking it as most recently used.
   - `popitem(last=True)`: Removes and returns a `(key, value)` pair from the dictionary. If `last` is `True`, it removes the last item; if `False`, it removes the first item.

### Example Usage:

Here’s a simple example demonstrating how to use `OrderedDict`:

```python
from collections import OrderedDict

# Create an OrderedDict
od = OrderedDict()

# Add some key-value pairs
od['a'] = 1
od['b'] = 2
od['c'] = 3

# Iterate over the OrderedDict
for key, value in od.items():
    print(f"{key}: {value}")

# Output:
# a: 1
# b: 2
# c: 3

# Move 'a' to the end
od.move_to_end('a')

# Show the updated order
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Pop the first item
first_item = od.popitem(last=False)
print(first_item)  # Output: ('b', 2)
```


![[lru_cache.py]]


### When to Use `OrderedDict`:

- Use `OrderedDict` when you need to maintain the order of items as they are added, especially if you plan to access or manipulate them based on their order.
- It is particularly useful in situations like implementing caches (e.g., LRU Cache) where the order of access matters. 

With the introduction of Python 3.7, regular dictionaries also maintain insertion order, but `OrderedDict` provides some additional functionality that can be useful in specific scenarios.









{
more: by chatGPT

The LRU (Least Recently Used) Cache problem can be solved using various approaches, each with its own trade-offs. Here are some common approaches:

### 1. **Hash Map + Doubly Linked List**
- **Description**: Use a hash map to store key-value pairs for O(1) access time, and a doubly linked list to maintain the order of usage.
- **Advantages**:
  - Fast O(1) time complexity for both `get` and `put`.
  - Efficiently manage the order of usage.
- **Disadvantages**:
  - More complex implementation due to the need for managing the linked list.

### 2. **Ordered Dictionary (Python's `collections.OrderedDict`)**
- **Description**: Utilize an ordered dictionary which maintains the order of keys based on insertion.
- **Advantages**:
  - Simple to implement with built-in data structures.
  - O(1) time complexity for `get` and `put`.
- **Disadvantages**:
  - Limited to specific languages or libraries that support ordered dictionaries.

### 3. **Array + Hash Map**
- **Description**: Maintain an array for the cache entries and a hash map for quick lookups. When an item is accessed or added, update the array to reflect the order.
- **Advantages**:
  - Simpler logic for maintaining order.
- **Disadvantages**:
  - O(n) time complexity for some operations when reordering the array.

### 4. **Segment Tree**
- **Description**: Use a segment tree to manage the cache with the least recently used segments.
- **Advantages**:
  - Efficient in some scenarios where the cache size is dynamic or varies frequently.
- **Disadvantages**:
  - More complex to implement and understand compared to simpler structures.

### 5. **Queue + Hash Map**
- **Description**: Use a queue to maintain the order of usage, along with a hash map for quick access.
- **Advantages**:
  - Clear separation of order management and access.
- **Disadvantages**:
  - Might require additional operations to keep the queue in sync with the hash map, leading to increased complexity.

### 6. **Custom Data Structure**
- **Description**: Implement a specialized data structure that combines features of arrays, linked lists, or trees to meet specific requirements of the problem.
- **Advantages**:
  - Tailored to specific use cases or performance needs.
- **Disadvantages**:
  - Requires more effort in design and implementation, and can lead to less maintainable code.

### Summary
The choice of approach often depends on specific requirements such as simplicity, performance, memory usage, and ease of implementation. The hash map combined with a doubly linked list is the most common and efficient method for implementing an LRU cache, especially in environments like interviews or competitive programming.


Sure! Here are code implementations for various approaches to solve the LRU Cache problem.

### 1. **Hash Map + Doubly Linked List**

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_tail(node)
        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]
```

### 2. **Ordered Dictionary (Python's `collections.OrderedDict`)**

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # Move to end to show it's recently used
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove the first (least recently used)
```

### 3. **Array + Hash Map**

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.pop(0)  # Remove least recently used
            del self.cache[oldest]
        self.cache[key] = value
        self.order.append(key)
```

### 4. **Segment Tree**
*(More complex, usually not practical for LRU caches)*

```python
# Segment trees are generally not used for LRU caches directly,
# as they are better suited for range queries and updates.
# Implementing an LRU Cache with segment trees would be atypical.
```

### 5. **Queue + Hash Map**

```python
from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.popleft()  # Remove least recently used
            del self.cache[oldest]
        self.cache[key] = value
        self.order.append(key)
```

### 6. **Custom Data Structure**
*(This will depend on specific requirements and is often similar to the hash map + linked list solution)*

```python
# This approach can vary greatly based on requirements,
# usually leading back to a hash map and linked list.
```

### Summary
The **Hash Map + Doubly Linked List** method is the most efficient and commonly used approach for implementing an LRU Cache, but other methods can be useful depending on the context and requirements. Each implementation has its pros and cons, so choose based on your needs!





}

for more : refer
LRU Cache: https://leetcode.com/problems/lru-cache/description/





