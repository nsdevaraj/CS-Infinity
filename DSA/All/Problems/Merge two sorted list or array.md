
[Leet Code #21](https://leetcode.com/problems/merge-two-sorted-lists/description/)


`Both normal list and linked list.. `


Merge Two Sorted Lists
•	Problem: Merge two sorted linked lists and return it as a new sorted list.
•	Example:
Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]



```python


# Approach: Concatenate and sort
# 1. Merge both lists into one.
# 2. Sort the merged list.
# Time complexity: O(n+m) + O((n+m)log(n+m)) = O((n+m)log(n+m))
# Space complexity: O(n+m)
def merge_two_sorted_lists1(list1, list2):
    list3 = list1 + list2
    return sorted(list3)


```


```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m,m+n):
            nums1[i]=nums2[i-m]
        nums1.sort()
```


```typescript
// Function to merge two sorted lists
function mergeTwoSortedLists(l1, l2) {
  let merged = [];
  let i = 0,
    j = 0;

  while (i < l1.length && j < l2.length) {
    if (l1[i] < l2[j]) {
      merged.push(l1[i]);
      i++;
    } else {
      merged.push(l2[j]);
      j++;
    }
  }

  // Add remaining elements from l1
  while (i < l1.length) {
    merged.push(l1[i]);
    i++;
  }

  // Add remaining elements from l2
  while (j < l2.length) {
    merged.push(l2[j]);
    j++;
  }

  return merged;
}
```



```python

# Approach: Two-pointer merge
# 1. Use two pointers, one for each list.
# 2. Compare elements at pointers and append the smaller one to result.
# 3. Move the respective pointer and continue until done.
# 4. Append any remaining elements.
# Time complexity: O(n+m)
# Space complexity: O(n+m)
def merge_two_sorted_lists2(list1, list2):
    [list1_ptr, list2_ptr] = [0, 0]
    [list1_len, list2_len] = [len(list1), len(list2)]
    sorted_list = []

    while list1_ptr < list1_len and list2_ptr < list2_len:
        [value1, value2] = [list1[list1_ptr], list2[list2_ptr]]
        if value1 < value2:
            sorted_list.append(value1)
            list1_ptr += 1
        else:
            sorted_list.append(value2)
            list2_ptr += 1

    # The sorted_list.extend() method is more efficient than sorted_list = sorted_list + list2[:]
    # as it avoids creating a new list during concatenation.
    sorted_list.extend(list1[list1_ptr:])
    sorted_list.extend(list2[list2_ptr:])
    return sorted_list


```


### inplace swapping


```python

# Approach: In-place merge with element swapping
# 1. Iterate through list1, comparing each element with the first in list2.
# 2. If list1's element is larger, swap it with the first element of list2.
# 3. Re-sort list2 by shifting the swapped element into place.
# 4. Repeat until all list1 elements are processed, then append list2's remainder.
# Time complexity: O(n * m) due to shifts in list2.
# Space complexity: O(1), no extra space used.
def merge_two_sorted_lists3(list1, list2):
    list1_ptr = 0
    [list1_len, list2_len] = [len(list1), len(list2)]

    while list1_ptr < list1_len and list2_len:
        value1, value2 = list1[list1_ptr], list2[0]

        if(value1 > value2):
            list1[list1_ptr] = value2
            list2[0] = value1
            iter_index = 0
            while( iter_index < list2_len-1 and  list2[iter_index]  > list2[iter_index+1] ):
                list2[iter_index],list2[iter_index+1] = list2[iter_index+1],list2[iter_index]
                iter_index += 1
        list1_ptr += 1

    list1.extend(list2)
    return list1



```



### Reverse filling

The "Merge Sorted Array" problem typically involves merging two sorted arrays into a single sorted array. The problem can be solved using an **in-place** approach by leveraging the end of one of the arrays to avoid extra space allocation. Below is a common solution that modifies the first array `nums1` to hold the merged result. This is done by working backwards from the end of both arrays.

### Problem Statement:

You are given two sorted integer arrays `nums1` and `nums2`, where:

- `nums1` has a size of `m + n`, where the first `m` elements represent the elements in the array and the rest are empty, reserved for the `n` elements of `nums2`.
- `nums2` has a size of `n`.

You need to merge `nums2` into `nums1` in **non-decreasing order**. The merge should be done **in-place** without using extra space (other than the provided arrays).

### Approach:

1. Start from the end of both arrays (`nums1` and `nums2`), where the empty spaces in `nums1` are available for the merged result.
2. Compare the elements of `nums1` and `nums2` starting from the last valid elements, and insert the larger one at the end of `nums1`.
3. Continue moving backwards until you have processed all elements from `nums2` and potentially part of `nums1`.
4. If there are still remaining elements in `nums2` (meaning that all elements in `nums1` have already been placed), simply copy the remaining elements of `nums2` into `nums1`.

### Solution:

```python
def merge(nums1, m, nums2, n):
    # Start filling nums1 from the end (from index m + n - 1)
    i = m - 1  # last element in the valid part of nums1
    j = n - 1  # last element in nums2
    k = m + n - 1  # last index in nums1 (full size)

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are any remaining elements in nums2, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    # No need to copy the remaining elements of nums1 because they are already in place
```


### Explanation:

- We use three pointers:
    
    - `i` points to the last element of the valid part of `nums1`.
    - `j` points to the last element of `nums2`.
    - `k` points to the last index of the entire `nums1` array (after merging).
- We compare the elements of `nums1` and `nums2` starting from the end. The larger element between `nums1[i]` and `nums2[j]` is placed at `nums1[k]`, and we move the corresponding pointer (`i` or `j`) and decrement `k`.
    
- If there are still remaining elements in `nums2` (i.e., `nums2` is not fully merged), we copy them into `nums1` directly. If there are remaining elements in `nums1`, they are already in place, so we don't need to copy them.
    

### Time Complexity:

- **O(m + n)** where `m` is the number of elements in the valid part of `nums1`, and `n` is the number of elements in `nums2`. We traverse both arrays once.

### Space Complexity:

- **O(1)** since we are modifying `nums1` in place without using any extra space beyond the provided arrays.

### Example:

**Input:**

```python
nums1 = [1, 3, 5, 0, 0, 0]
m = 3
nums2 = [2, 4, 6]
n = 3
merge(nums1, m, nums2, n)
```

**Output:**

```python
nums1 = [1, 2, 3, 4, 5, 6]
```

In this example, the arrays `nums1` and `nums2` are merged in-place in `nums1` while maintaining the sorted order.


### Test

```python

def test_merge_two_sorted_lists(func):
    print(f"Testing function: {func.__name__}")

    merge_two_sorted_lists_test_cases = [
        # Case 1: General case with two lists containing similar elements
        {
            'input': ([1, 2, 4], [1, 3, 4]),
            'expected': [1, 1, 2, 3, 4, 4]
        },
        # Case 2: Both lists are empty
        {
            'input': ([], []),
            'expected': []
        },
        # Case 3: One list is empty
        {
            'input': ([1, 2, 3], []),
            'expected': [1, 2, 3]
        },
        {
            'input': ([], [1, 2, 3]),
            'expected': [1, 2, 3]
        },
        # Case 4: Both lists contain only one element each
        {
            'input': ([5], [3]),
            'expected': [3, 5]
        },
        # Case 5: Lists with different lengths
        {
            'input': ([1, 2], [1, 3, 5, 7]),
            'expected': [1, 1, 2, 3, 5, 7]
        },
        # Case 6: Lists with duplicate elements
        {
            'input': ([1, 1, 1], [1, 1, 1]),
            'expected': [1, 1, 1, 1, 1, 1]
        },
        # Case 7: One list contains negative numbers
        {
            'input': ([-5, -3, -1], [0, 2, 4]),
            'expected': [-5, -3, -1, 0, 2, 4]
        },
        # Case 8: Both lists contain negative numbers
        {
            'input': ([-10, -3, 2], [-8, -4, 1]),
            'expected': [-10, -8, -4, -3, 1, 2]
        },
        # Case 9: Large numbers in lists
        {
            'input': ([1000000, 1000001], [999999, 1000002]),
            'expected': [999999, 1000000, 1000001, 1000002]
        }
    ]

    for i, test_case in enumerate(merge_two_sorted_lists_test_cases, 1):
        l1, l2 = test_case['input']
        expected_output = test_case['expected']
        result = func(l1, l2)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
    print("Test cases completed!")




```


TO check things in below
### Extra


https://www.geeksforgeeks.org/python-ways-to-concatenate-two-lists/



Another efficient approach for merging two sorted lists is **in-place merging** when the lists are mutable (such as linked lists) and we want to avoid extra space usage for creating a new list. This approach is particularly useful when dealing with linked lists, but for arrays (or Python lists), the traditional method of merging into a new list is already optimal for time complexity.

However, if you want an alternative approach that avoids unnecessary copying, here are a few suggestions:

### **Alternative 1: Priority Queue (Heap)**

If the lists are very large, or you're merging more than two sorted lists, a **priority queue (min-heap)** can be useful. This is efficient when merging multiple sorted lists or streams:

```python
import heapq

def merge_two_sorted_lists_heap(list1, list2):
    return list(heapq.merge(list1, list2))
```

### Explanation:
- **Heap Merge**: The `heapq.merge()` function takes in multiple sorted iterables and merges them in sorted order.
- This uses a **min-heap** to efficiently merge, and the heap ensures the smallest element is always placed first.

### Time Complexity: O(n + m), where `n` and `m` are the lengths of `list1` and `list2` respectively.
### Space Complexity: O(n + m), for the new merged list.

---

### **Alternative 2: In-place Merge (For Linked Lists)**

This approach is only possible if the lists are linked lists. The idea is to reuse the nodes from the original lists, rather than creating a new list.

Here's how you might do this with **singly linked lists**:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_linked_lists(l1, l2):
    dummy = ListNode()  # A dummy node to start the merged list
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach the remaining nodes
    current.next = l1 if l1 else l2

    return dummy.next
```

### Explanation:
- **In-place merge**: This approach doesn’t use extra space for a new list. Instead, it just rearranges the pointers of the existing linked lists.
- A **dummy node** is used to simplify edge cases and build the resulting merged list.

### Time Complexity: O(n + m), where `n` and `m` are the lengths of the two linked lists.
### Space Complexity: O(1), as no extra space is used besides the dummy node.

---

### **Alternative 3: Itertools (Functional Approach)**

If you're looking for a more functional programming approach, Python’s `itertools.chain()` can be used to merge iterators efficiently:

```python
import itertools

def merge_two_sorted_lists_iter(list1, list2):
    return sorted(itertools.chain(list1, list2))
```

### Explanation:
- This uses `itertools.chain()` to lazily concatenate the two sorted lists and then sorts them.
- **Note**: While this method uses functional programming techniques, it requires an additional `sorted()` call, which increases time complexity to O((n + m) log(n + m)).

### Time Complexity: O((n + m) log(n + m)) due to the sorting step.
### Space Complexity: O(n + m).

---

### Conclusion:
- **In-place merging** is the best option if you are dealing with linked lists and want to save on space.
- **Heap merging** is more efficient when merging multiple sorted lists.
- For basic arrays or Python lists, the original approach using two pointers and extending the list remains the optimal solution in terms of time complexity (O(n + m)) and space complexity (O(n + m)).



## Sorted linked list

```typescript

const mergedTwoSortedLinkedList = (
  list1Head: linkedListNode | null,
  list2Head: linkedListNode | null,
) => {
  let [head1, head2] = [list1Head, list2Head];

  if (!head1) return head2;
  if (!head2) return head1;

  let newListHead: linkedListNode | null = null;
  let pointerHead: linkedListNode | null = newListHead;
  while (head1 && head2) {
    if (head1.value < head2.value) {
      const newItem = new linkedListNode(head1.value);
      head1 = head1.next;
      if (pointerHead) {
        pointerHead.next = newItem;
      } else {
        newListHead = newItem;
      }
      pointerHead = newItem;
    } else {
      const newItem = new linkedListNode(head2.value);
      head2 = head2.next;
      if (pointerHead) {
        pointerHead.next = newItem;
      } else {
        newListHead = newItem;
      }
      pointerHead = newItem;
    }
  }

  while (head1) {
    const newItem = new linkedListNode(head1.value);
    if (pointerHead) {
      pointerHead.next = newItem;
    }
    pointerHead = newItem;
    head1 = head1.next;
  }

  while (head2) {
    const newItem = new linkedListNode(head2.value);
    if (pointerHead) {
      pointerHead.next = newItem;
    }
    pointerHead = newItem;
    head2 = head2.next;
  }

  return newListHead;
};

```



```typescript
// create dummy to minimize handlings and do things inplace

class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val: number = 0, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

function mergeTwoSortedLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    // Create a dummy node to simplify the merge process
    const dummy = new ListNode(0);
    let current = dummy;

    // While both lists have nodes
    while (l1 !== null && l2 !== null) {
        if (l1.val < l2.val) {
            current.next = l1;
            l1 = l1.next; // Move to the next node in l1
        } else {
            current.next = l2;
            l2 = l2.next; // Move to the next node in l2
        }
        current = current.next; // Move the current pointer
    }

    // If one list is not yet exhausted, link the remainder of it
    if (l1 !== null) {
        current.next = l1;
    } else if (l2 !== null) {
        current.next = l2;
    }

    // Return the merged list, which starts after the dummy node
    return dummy.next;
}

// Example usage:

// Helper function to create a linked list from an array
function createLinkedList(arr: number[]): ListNode | null {
    if (arr.length === 0) return null;
    const head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
}

// Helper function to print a linked list
function printLinkedList(head: ListNode | null): void {
    let current = head;
    const values: number[] = [];
    while (current !== null) {
        values.push(current.val);
        current = current.next;
    }
    console.log(values.join(" -> "));
}

// Example linked lists
const list1 = createLinkedList([1, 2, 4]);
const list2 = createLinkedList([1, 3, 4]);

const mergedList = mergeTwoSortedLists(list1, list2);
printLinkedList(mergedList); // Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4


```

### Test linkedList

```typescript
class linkedListNode {
  public value: number;
  public next: linkedListNode | null;
  constructor(value: number, next: linkedListNode | null = null) {
    this.value = value;
    this.next = next;
  }
}

const getArrayToLinkedList = (ary: number[]): linkedListNode | null => {
  const aryLen = ary.length;
  if (aryLen < 1) return null;

  const head = new linkedListNode(ary[0]);
  let prevNode = head;
  for (let i = 1; i < aryLen; i++) {
    const newNode = new linkedListNode(ary[i]);
    prevNode.next = newNode;
    prevNode = newNode;
  }
  return head;
};

const getLinkedListToAry = (head: linkedListNode | null): number[] => {
  const linkedListAry = [];
  while (head) {
    linkedListAry.push(head.value);
    head = head.next;
  }
  return linkedListAry;
};

const mergeTwoSortedListsTestCases = [
  // Case 1: General case with two lists containing similar elements
  {
    input: [
      [1, 2, 4],
      [1, 3, 4],
    ],
    expected: [1, 1, 2, 3, 4, 4],
  },
  // Case 2: Both lists are empty
  {
    input: [[], []],
    expected: [],
  },
  // Case 3: One list is empty
  {
    input: [[1, 2, 3], []],
    expected: [1, 2, 3],
  },
  {
    input: [[], [1, 2, 3]],
    expected: [1, 2, 3],
  },
  // Case 4: Both lists contain only one element each
  {
    input: [[5], [3]],
    expected: [3, 5],
  },
  // Case 5: Lists with different lengths
  {
    input: [
      [1, 2],
      [1, 3, 5, 7],
    ],
    expected: [1, 1, 2, 3, 5, 7],
  },
  // Case 6: Lists with duplicate elements
  {
    input: [
      [1, 1, 1],
      [1, 1, 1],
    ],
    expected: [1, 1, 1, 1, 1, 1],
  },
  // Case 7: One list contains negative numbers
  {
    input: [
      [-5, -3, -1],
      [0, 2, 4],
    ],
    expected: [-5, -3, -1, 0, 2, 4],
  },
  // Case 8: Both lists contain negative numbers
  {
    input: [
      [-10, -3, 2],
      [-8, -4, 1],
    ],
    expected: [-10, -8, -4, -3, 1, 2],
  },
  // Case 9: Large numbers in lists
  {
    input: [
      [1000000, 1000001],
      [999999, 1000002],
    ],
    expected: [999999, 1000000, 1000001, 1000002],
  },
  {
    input: [
      [-9, 3],
      [5, 7],
    ],
    expected: [-9, 3, 5, 7],
  },
];

// Test function
function runTests(func: Function) {
  for (let i = 0; i < mergeTwoSortedListsTestCases.length; i++) {
    const { input, expected } = mergeTwoSortedListsTestCases[i];
    const input1 = getArrayToLinkedList(input[0]);
    const input2 = getArrayToLinkedList(input[1]);
    const resultTemp = func(input1, input2);

    const result = getLinkedListToAry(resultTemp);

    console.assert(
      JSON.stringify(result) === JSON.stringify(expected),
      `Test case ${i + 1} failed: expected ${JSON.stringify(expected)}, got ${JSON.stringify(result)}`,
    );
  }
  console.log("Test cases completed!");
}

const mergedTwoSortedLinkedList = (
  list1Head: linkedListNode | null,
  list2Head: linkedListNode | null,
) => {
  let [head1, head2] = [list1Head, list2Head];

  if (!head1) return head2;
  if (!head2) return head1;

  let newListHead: linkedListNode | null = null;
  let pointerHead: linkedListNode | null = newListHead;
  while (head1 && head2) {
    if (head1.value < head2.value) {
      const newItem = new linkedListNode(head1.value);
      head1 = head1.next;
      if (pointerHead) {
        pointerHead.next = newItem;
      } else {
        newListHead = newItem;
      }
      pointerHead = newItem;
    } else {
      const newItem = new linkedListNode(head2.value);
      head2 = head2.next;
      if (pointerHead) {
        pointerHead.next = newItem;
      } else {
        newListHead = newItem;
      }
      pointerHead = newItem;
    }
  }

  while (head1) {
    const newItem = new linkedListNode(head1.value);
    if (pointerHead) {
      pointerHead.next = newItem;
    }
    pointerHead = newItem;
    head1 = head1.next;
  }

  while (head2) {
    const newItem = new linkedListNode(head2.value);
    if (pointerHead) {
      pointerHead.next = newItem;
    }
    pointerHead = newItem;
    head2 = head2.next;
  }

  return newListHead;
};

// Run the tests
runTests(mergedTwoSortedLinkedList);

```



to check {

https://leetcode.com/problems/merge-two-sorted-lists/description/

https://leetcode.com/discuss/interview-question/4530120/Merge-Two-Sorted-Lists-In-Reverse-Order-or-4-Solutions-or-BruteOptimal-or-Self-Explanatory-Comments/


}