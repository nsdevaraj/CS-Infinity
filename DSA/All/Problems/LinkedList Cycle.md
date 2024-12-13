
[LeetCode #141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)


 Linked List Cycle

**Easy**

## Description

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where the tail connects back to a node. If `pos` is `-1`, then there is no cycle.

**Note**: `pos` is just used to show the cycle in the input. It is **not** passed as a parameter.

## Examples

### Example 1:

**Input:** 
```plaintext
head = [3,2,0,-4], pos = 1
```

**Output:** 
```plaintext
true
```

**Explanation:** 
There is a cycle in the linked list, where the tail connects to the second node.

### Example 2:

**Input:** 
```plaintext
head = [1,2], pos = 0
```

**Output:** 
```plaintext
true
```

**Explanation:** 
There is a cycle in the linked list, where the tail connects to the first node.

### Example 3:

**Input:** 
```plaintext
head = [1], pos = -1
```

**Output:** 
```plaintext
false
```

**Explanation:** 
There is no cycle in the linked list.

## Constraints

- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list.

---

## Approach 1: Using a Hash Set

### Algorithm

The simplest way to detect a cycle is to use a hash set to store all nodes we have visited. If we encounter a node that is already in the hash set, then we have found a cycle.

### Steps:
1. Initialize an empty hash set.
2. Traverse the linked list:
   - If the current node is `None`, return `False` (end of the list without a cycle).
   - If the current node is already in the hash set, return `True` (cycle detected).
   - Otherwise, add the current node to the hash set and continue to the next node.
   
### Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False
```


```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dup = set()
        while head:
            if head in dup: return True
            dup.add(head)
            head = head.next
        return False
```



### Time Complexity: 
- \(O(n)\), where \(n\) is the number of nodes in the linked list. We visit each node at most once.

### Space Complexity: 
- \(O(n)\) due to the hash set used to store visited nodes.

---

## Approach 2: Two Pointers (Floyd’s Cycle Detection Algorithm)

### Algorithm

This is a more efficient approach that uses two pointers: one moving faster (`fast`), and the other moving slower (`slow`). If there is a cycle, the `fast` pointer will eventually meet the `slow` pointer.

### Steps:
1. Initialize two pointers, `slow` and `fast`, both starting at the head.
2. Move `slow` one step at a time and `fast` two steps at a time.
3. If the `fast` pointer reaches `None`, return `False` (no cycle).
4. If the `fast` pointer meets the `slow` pointer, return `True` (cycle detected).

### Code

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while fast != slow:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True
```

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

```



**Problem:** Determine if a linked list has a cycle.

```python
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```



?? to check

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        curr = head.next

        while curr:
            if curr is head:
                return True
            prev, curr = curr, curr.next
            prev.next = head

        return False

```


### Time Complexity: 
- \(O(n)\), where \(n\) is the number of nodes in the linked list. In the worst case, we may visit all nodes before detecting a cycle.

### Space Complexity: 
- \(O(1)\) since we are using a constant amount of extra space (no data structures like a hash set are used).

---

## Approach 3: Modifying Node Structure (Not Recommended)

This approach involves modifying the node structure to keep track of whether a node has been visited. It is not recommended because it violates the principle of immutability of the input data. However, for educational purposes:

### Steps:
1. Traverse the list and mark nodes as visited by modifying them (e.g., setting a flag).
2. If you encounter a node that has already been marked, return `True`.
3. If you reach the end of the list, return `False`.

### Code

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        current = head
        while current:
            if hasattr(current, 'visited'):
                return True
            current.visited = True
            current = current.next
        return False
```

### Time Complexity:
- \(O(n)\), where \(n\) is the number of nodes.

### Space Complexity:
- \(O(1)\) since we are not using extra data structures.

---

## Summary of Approaches:

| **Approach**               | **Time Complexity** | **Space Complexity** | **Remarks**                                                  |
| -------------------------- | ------------------- | -------------------- | ------------------------------------------------------------ |
| **Hash Set**               | \(O(n)\)            | \(O(n)\)             | Easy to understand but uses extra space for the hash set.    |
| **Two Pointers (Floyd's)** | \(O(n)\)            | \(O(1)\)             | Optimal in both time and space; commonly used in interviews. |
| **Modify Node Structure**  | \(O(n)\)            | \(O(1)\)             | Modifies the input, which is not ideal in most scenarios.    |

---

## Test Cases

### Python Test Function

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def test_hasCycle(func):
    def create_linked_list(values, pos):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        cycle_node = None
        if pos == 0:
            cycle_node = head
        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next
            if i == pos:
                cycle_node = current
        current.next = cycle_node
        return head

    test_cases = [
        {
            'name': 'Cycle exists',
            'input': create_linked_list([3, 2, 0, -4], 1),
            'expected': True,
        },
        {
            'name': 'No cycle',
            'input': create_linked_list([1, 2], -1),
            'expected': False,
        },
        {
            'name': 'Single node without cycle',
            'input': create_linked_list([1], -1),
            'expected': False,
        },
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = func(test_case['input'])
        assert result == test_case['expected'], f"Test case {i} failed: expected {test_case['expected']}, got {result}"

    print("All test cases passed!")

```

This article provides a complete explanation of different approaches to solving the "Linked List Cycle" problem. The most efficient method is the two-pointer approach, but the hash set method is also widely understood.



---
