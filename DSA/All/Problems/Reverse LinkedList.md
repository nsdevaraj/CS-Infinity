
[Leet Code #206](https://leetcode.com/problems/reverse-linked-list/description/)


### Problem Statement: Reverse a Linked List**

Given a singly linked list, write a function to reverse the list in place.

**Input:**
- A singly linked list represented by its head node.

**Output:**
- The head node of the reversed linked list.

**Example:**
- Input: `1 -> 2 -> 3 -> 4 -> 5`
- Output: `5 -> 4 -> 3 -> 2 -> 1`

**Constraints:**
- The linked list may be empty (head is `null`).
- The list may contain up to `n` nodes, where `1 ≤ n ≤ 10^4`.



### Soln:


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while(current):
            current_next = current.next
            current.next = previous
            previous = current
            current = current_next
        return previous

```

#### Iteration

```ts

// Approach - by iteration
// Time : O(n) - loops through whole linkedList
// Space : O(1) - no extra space needed
const reverseLinkedList1 = (head: linkedListNode | null) => {
  let current = head;
  let previous = null;
  while (current) {
    const currentNext = current.next;
    current.next = previous;
    previous = current;
    current = currentNext;
  }

  return previous;
};

```

#### Recursion

```ts


// Approach - by recursion
// Time : O(n) - loops through whole linkedList
// Space : O(n) - have call stack upto last linkedList node
const reverseLinkedList2 = (
  current: linkedListNode | null,
  previous: linkedListNode | null = null,
) => {
  if (current) {
    const nextNode = current.next;
    current.next = previous;
    previous = current;
    return reverseLinkedList2(nextNode, previous);
  } else {
    return previous;
  }
};


```



#### Refs

from chatGPT

Reversing a linked list is a common algorithmic problem, and there are several approaches to solve it in JavaScript. Below are a few different methods:

### 1. Iterative Approach

This approach uses a loop to reverse the pointers of the linked list.

```javascript
class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

function reverseLinkedList(head) {
    let prev = null;
    let current = head;

    while (current) {
        const nextTemp = current.next; // Store next node
        current.next = prev;            // Reverse the pointer
        prev = current;                 // Move prev forward
        current = nextTemp;             // Move current forward
    }

    return prev; // New head of the reversed list
}
```

### 2. Recursive Approach

This approach uses recursion to reverse the linked list.

```javascript
function reverseLinkedListRecursive(head) {
    if (!head || !head.next) return head; // Base case: if empty or single node

    const newHead = reverseLinkedListRecursive(head.next); // Reverse the rest of the list
    head.next.next = head; // Make the next node point to the current node
    head.next = null; // Set current node's next to null

    return newHead; // Return new head
}
```

### 3. Using a Stack

This method uses a stack to reverse the linked list by pushing nodes onto the stack and popping them off.

```javascript
function reverseLinkedListStack(head) {
    if (!head) return null;

    const stack = [];
    let current = head;

    // Push all nodes onto the stack
    while (current) {
        stack.push(current);
        current = current.next;
    }

    const newHead = stack.pop(); // New head is the last element popped
    current = newHead;

    // Pop the rest of the nodes and link them
    while (stack.length) {
        current.next = stack.pop();
        current = current.next;
    }

    current.next = null; // Last node's next should be null

    return newHead;
}
```

### 4. Using Array

You can also use an array to store nodes, then rebuild the linked list in reverse order.

```javascript
function reverseLinkedListArray(head) {
    if (!head) return null;

    const nodes = [];
    let current = head;

    // Store nodes in an array
    while (current) {
        nodes.push(current);
        current = current.next;
    }

    // Rebuild the linked list in reverse order
    for (let i = nodes.length - 1; i > 0; i--) {
        nodes[i].next = nodes[i - 1];
    }
    nodes[0].next = null; // First node's next should be null

    return nodes[nodes.length - 1]; // Return new head
}
```

### Summary

1. **Iterative**: Efficient and straightforward, using constant space.
2. **Recursive**: Clean and elegant, but uses O(n) space for the call stack.
3. **Stack**: Uses extra space but can be easier to understand conceptually.
4. **Array**: Also uses extra space and is less efficient for very large lists.

Choose the method that best fits your needs based on constraints like memory usage and code clarity!



**Problem:** Reverse a singly linked list.

```python
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev
```


---


#### Tests

```ts

class linkedListNode {
  public value: number;
  public next: linkedListNode | null;
  constructor(value: number) {
    this.value = value;
    this.next = null;
  }
}

const REVERSE_LINKED_LIST_TEST_CASES = [
  {
    name: "Empty List",
    input: [],
    expected: [],
  },
  {
    name: "Single Element",
    input: [1],
    expected: [1],
  },
  {
    name: "Two Elements",
    input: [1, 2],
    expected: [2, 1],
  },
  {
    name: "Three Elements",
    input: [1, 2, 3],
    expected: [3, 2, 1],
  },
  {
    name: "Multiple Elements",
    input: [1, 2, 3, 4, 5],
    expected: [5, 4, 3, 2, 1],
  },
  {
    name: "Negative Numbers",
    input: [-1, -2, -3],
    expected: [-3, -2, -1],
  },
];

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

const testReverseLinkedList = (reverseFunc: Function) => {
  for (const testCase of REVERSE_LINKED_LIST_TEST_CASES) {
    const linkedListArray = testCase.input;
    const linkedListHead = getArrayToLinkedList(linkedListArray);
    const reversedHead = reverseFunc(linkedListHead);
    const resultArray = getLinkedListToAry(reversedHead);

    console.assert(
      JSON.stringify(resultArray) === JSON.stringify(testCase.expected),
      `Test case '${testCase.name}' failed: expected ${JSON.stringify(testCase.expected)}, got ${JSON.stringify(resultArray)}`,
    );
  }

  console.log("All test cases completed!");
};
```


