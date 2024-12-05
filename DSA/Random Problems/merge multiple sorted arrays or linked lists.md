

referred {

https://www.youtube.com/watch?v=q5a5OiGbT6Q

https://www.youtube.com/shorts/EJ9BBc9Izts

}

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # def linkedListToArray(self, linkedList):
    #     ary = []
    #     head = linkedList
    #     while(head):
    #         ary.append(head.val)
    #         head = head.next
    #     return ary
    
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None):
        dummy = ListNode()
        tail = dummy

        while(list1 and list2):
            if(list1.val < list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if(list1):
            tail.next = list1
        if(list2):
            tail.next = list2
        
        return dummy.next

    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if(not lists or len(lists) == 0):
            return None

        while(len(lists) > 1):
            mergedLists = []
            for i in range(0,len(lists), 2):
                list1 = lists[i]
                list2 =  lists[i+1] if (i+1 < len(lists) ) else  None
                # print(i, self.linkedListToArray(list1), self.linkedListToArray(list2))
                mergedLists.append(self.mergeTwoLists(list1, list2))
            # print(self.linkedListToArray(mergedLists))
            lists = mergedLists
        
        return lists[0]
```





To merge multiple sorted lists into a single sorted list in JavaScript, you can use the following methods:

---

### **1. Using a Min-Heap (Efficient for Large Lists)**

This method uses a priority queue (min-heap) to efficiently merge multiple sorted lists.

#### **Code Example:**

```javascript
class MinHeap {
  constructor() {
    this.heap = [];
  }

  push(item) {
    this.heap.push(item);
    this.bubbleUp(this.heap.length - 1);
  }

  pop() {
    if (this.heap.length === 1) return this.heap.pop();
    const top = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown(0);
    return top;
  }

  bubbleUp(index) {
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[parentIndex].value <= this.heap[index].value) break;
      [this.heap[parentIndex], this.heap[index]] = [this.heap[index], this.heap[parentIndex]];
      index = parentIndex;
    }
  }

  bubbleDown(index) {
    const length = this.heap.length;
    while (true) {
      const leftChild = 2 * index + 1;
      const rightChild = 2 * index + 2;
      let smallest = index;

      if (leftChild < length && this.heap[leftChild].value < this.heap[smallest].value) {
        smallest = leftChild;
      }
      if (rightChild < length && this.heap[rightChild].value < this.heap[smallest].value) {
        smallest = rightChild;
      }
      if (smallest === index) break;
      [this.heap[smallest], this.heap[index]] = [this.heap[index], this.heap[smallest]];
      index = smallest;
    }
  }

  isEmpty() {
    return this.heap.length === 0;
  }
}

function mergeSortedLists(lists) {
  const heap = new MinHeap();
  const result = [];

  // Initialize heap with the first element of each list
  lists.forEach((list, index) => {
    if (list.length > 0) {
      heap.push({ value: list[0], listIndex: index, elementIndex: 0 });
    }
  });

  // Extract the smallest element and add the next element from the same list to the heap
  while (!heap.isEmpty()) {
    const { value, listIndex, elementIndex } = heap.pop();
    result.push(value);

    const nextIndex = elementIndex + 1;
    if (nextIndex < lists[listIndex].length) {
      heap.push({ value: lists[listIndex][nextIndex], listIndex, elementIndex: nextIndex });
    }
  }

  return result;
}

// Example Usage
const lists = [
  [1, 5, 8],
  [2, 3, 7],
  [4, 6, 9]
];
console.log(mergeSortedLists(lists)); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### **2. Using a Flatten and Sort Method (Simple but Inefficient for Large Lists)**

#### **Code Example:**

```javascript
function mergeSortedLists(lists) {
  return lists.flat().sort((a, b) => a - b);
}

// Example Usage
const lists = [
  [1, 5, 8],
  [2, 3, 7],
  [4, 6, 9]
];
console.log(mergeSortedLists(lists)); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Time Complexity:**

- Flattening: O(n)O(n) where nn is the total number of elements.
- Sorting: O(nlog⁡n)O(n \log n).  
    Overall: O(nlog⁡n)O(n \log n).

---

### **3. Iterative Pairwise Merge (Divide and Conquer)**

This approach repeatedly merges two sorted lists at a time.

#### **Code Example:**

```javascript
function mergeTwoLists(list1, list2) {
  let i = 0, j = 0;
  const result = [];

  while (i < list1.length && j < list2.length) {
    if (list1[i] < list2[j]) {
      result.push(list1[i++]);
    } else {
      result.push(list2[j++]);
    }
  }

  // Add remaining elements
  return result.concat(list1.slice(i)).concat(list2.slice(j));
}

function mergeSortedLists(lists) {
  while (lists.length > 1) {
    const merged = [];
    for (let i = 0; i < lists.length; i += 2) {
      const list1 = lists[i];
      const list2 = i + 1 < lists.length ? lists[i + 1] : [];
      merged.push(mergeTwoLists(list1, list2));
    }
    lists = merged;
  }
  return lists[0] || [];
}

// Example Usage
const lists = [
  [1, 5, 8],
  [2, 3, 7],
  [4, 6, 9]
];
console.log(mergeSortedLists(lists)); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Time Complexity:** O(nlog⁡k)O(n \log k), where nn is the total number of elements, and kk is the number of lists. This is because we repeatedly merge kk lists, halving the number of lists at each step.

---

### Which Method to Use?

- Use **Min-Heap** for optimal performance when merging many lists with a large number of elements.
- Use **Flatten and Sort** for simplicity if performance isn't critical.
- Use **Divide and Conquer** for a balanced approach.


----

## Merge k Sorted Lists (LeetCode #23)

---

### Problem Statement

You are given an array of `k` linked lists, where each linked list is sorted in **ascending order**. Merge all the linked lists into one sorted linked list and return it.

---

### Example:

**Example 1:**

```plaintext
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Explanation:
The linked lists are:
[
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]
Merging them into one sorted linked list:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

**Example 2:**

```plaintext
Input: lists = []
Output: []
```

**Example 3:**

```plaintext
Input: lists = [[]]
Output: []
```

---

### Constraints:

- k==lists.lengthk == \text{lists.length}
- 0≤k≤1040 \leq k \leq 10^4
- 0≤lists[i].length≤5000 \leq \text{lists[i].length} \leq 500
- −104≤lists[i][j]≤104-10^4 \leq \text{lists[i][j]} \leq 10^4
- `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` will not exceed 10410^4.

---

### Approach 1: Merge Two Lists Iteratively

The simplest approach to solve this problem is to repeatedly merge two sorted linked lists until only one list remains.

#### Steps:

1. Define a helper function to merge two sorted linked lists.
2. Iteratively merge each list in the input until only one merged list remains.

#### Code:

```python
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Dummy node to simplify code
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append the remaining nodes
    current.next = l1 if l1 else l2
    return dummy.next

def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    while len(lists) > 1:
        merged_lists = []
        # Merge pairs of lists
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(merge_two_lists(l1, l2))
        lists = merged_lists

    return lists[0]
```

---

#### Time Complexity:

- **Merging Two Lists**: O(n+m)O(n + m), where nn and mm are the lengths of the two lists.
- **Overall Complexity**: In the worst case, we merge all lists repeatedly, which takes O(k⋅n)O(k \cdot n), where kk is the number of lists and nn is the average length of a list.

#### Space Complexity:

- **Auxiliary Space**: O(1)O(1) (in-place merging).
- **Recursive Space**: O(log⁡k)O(\log k) due to recursive merging.

---

### Approach 2: Divide and Conquer


a **divide and conquer** approach. Instead of merging the lists one by one, we recursively divide the problem into smaller subproblems and merge the pairs of lists in a balanced manner. This significantly reduces the number of merges.

#### Steps:

1. Divide the array of linked lists into two halves.
2. Recursively merge each half.
3. Merge the two sorted halves.

This approach is similar to the merge step in **merge sort**.

#### Code:

```python
def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    # Divide the list into two halves
    mid = len(lists) // 2
    left = merge_k_sorted_lists(lists[:mid])
    right = merge_k_sorted_lists(lists[mid:])

    # Merge the two sorted halves
    return merge_two_lists(left, right)
```

---

#### Time Complexity:

- At each level of recursion, we merge kk lists in pairs, taking O(n)O(n) time per merge.
- The depth of the recursion tree is log⁡k\log k because we divide the lists into halves at each step.
- **Total Complexity**: O(n⋅log⁡k)O(n \cdot \log k), where nn is the total number of nodes across all lists.

#### Space Complexity:

- **Recursive Space**: O(log⁡k)O(\log k) due to the recursion depth.

---

### Approach 3: Using a Min-Heap (Priority Queue)

We can use a **min-heap** to efficiently merge the k sorted linked lists. A min-heap allows us to quickly extract the smallest element among the k lists at each step.

#### Steps:

1. Add the first node of each list to a min-heap. Use the node's value as the key for comparison.
2. Repeatedly extract the smallest element from the heap, add it to the result list, and push the next node from the same list into the heap.
3. Continue until the heap is empty.

This approach minimizes the number of comparisons by leveraging the heap's properties.

#### Code:

```python
import heapq

def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Min-heap to store (node value, list index, node reference)
    min_heap = []

    # Initialize the heap with the first node of each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))

    dummy = ListNode()
    current = dummy

    while min_heap:
        # Extract the smallest element
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        # Push the next node from the same list into the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next
```

---

#### Time Complexity:

- **Heap Operations**: Inserting and extracting from the heap takes O(log⁡k)O(\log k).
- We perform these operations nn times (once for each node in all lists).
- **Total Complexity**: O(n⋅log⁡k)O(n \cdot \log k).

#### Space Complexity:

- The heap can hold up to kk elements at any time.
- **Space Complexity**: O(k)O(k) for the heap.

---

### Comparison of Approaches

|Approach|Time Complexity|Space Complexity|Use Case|
|---|---|---|---|
|Iterative Pairwise Merge|O(n⋅k)O(n \cdot k)|O(1)O(1) or O(log⁡k)O(\log k)|Simple, but inefficient for large kk.|
|Divide and Conquer|O(n⋅log⁡k)O(n \cdot \log k)|O(log⁡k)O(\log k)|Balanced and efficient for large kk.|
|Min-Heap|O(n⋅log⁡k)O(n \cdot \log k)|O(k)O(k)|Best for handling large kk efficiently.|

---

### Test Cases

```python
def test_merge_k_sorted_lists(func):
    print(f"Testing function: {func.__name__}")

    # Helper function to create a linked list from a list
    def list_to_linked_list(arr):
        dummy = ListNode()
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Helper function to convert a linked list to a list
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Test cases
    test_cases = [
        {
            "name": "Example 1",
            "input": [[1, 4, 5], [1, 3, 4], [2, 6]],
            "expected": [1, 1, 2, 3, 4, 4, 5, 6],
        },
        {
            "name": "Empty List",
            "input": [],
            "expected": [],
        },
        {
            "name": "Single Empty List",
            "input": [[]],
            "expected": [],
        },
        {
            "name": "Single Non-Empty List",
            "input": [[1, 2, 3]],
            "expected": [1, 2, 3],
        },
        {
            "name": "Multiple Single Element Lists",
            "input": [[1], [3], [2]],
            "expected": [1, 2, 3],
        },
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        case_name = test_case["name"]

        # Convert input lists to linked lists
        linked_lists = [list_to_linked_list(lst) for lst in input_data]

        # Get the merged linked list
        result_node = func(linked_lists)

        # Convert result back to a list
        result_list = linked_list_to_list(result_node)

        assert result_list == expected_output, \
            f"Test case {i} ({case_name}) failed: expected {expected_output}, got {result_list}"

    print("All test cases passed!")

# Example usage:
test_merge_k_sorted_lists(merge_k_sorted_lists)
```

---

### Conclusion

The **Min-Heap** and **Divide and Conquer** approaches are the most efficient solutions for merging k sorted lists. While the divide-and-conquer approach leverages recursion, the min-heap solution directly utilizes efficient heap operations to reduce the number of comparisons.

Choose the best approach based on your use case:

- Use **Min-Heap** for large kk and scenarios where a priority queue is suitable.
- Use **Divide and Conquer** for balanced recursive merging.




Heap soln:


```python
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         a = []
        
#         for head in lists:
#             while head:
                
#                 heapq.heappush(a, head.val)
#                 head = head.next
                
#         head = ListNode()
#         dummy = head
        
#         while a:
#             dummy.next = ListNode(heapq.heappop(a))
#             dummy = dummy.next
            
#         return head.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        
        result = ListNode()
        dummy = result

        main_head = lists[0]
        # print_list(main_head)

        for i in range(1, len(lists)):
            curr_list = lists[i]
            main_head = self.mergeTwoLists(main_head, curr_list)
            
            
        return main_head

    
    def mergeTwoLists(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next

        while l1:
            dummy.next = l1
            dummy = dummy.next
            l1 = l1.next
        while l2:
            dummy.next = l2
            dummy = dummy.next
            l2 = l2.next

        return res.next

class Solution:
    f = open("user.out", 'w')
    print(sys.stdin)
    for s in sys.stdin:
        # print(s)
        print('[', ','.join(
            map(str, sorted(int(v) for v in s.rstrip().replace('[', ',').replace(']', ',').split(',') if v))), ']', sep='', file=f)
    exit()
```



### Categories:

- **Difficulty**: Hard in LeetCode
- **Problem Type**: Linked List, Sorting, Divide and Conquer
- **Techniques Used**: Merge Sort, Heap (Priority Queue)


Similar:
[[Merge k sorted lists (k-way merge algorithms)]]


to check {

heap soln: https://www.youtube.com/shorts/qzT_6R6yXys

\
https://www.youtube.com/watch?v=DvnxDGkjMDM


}