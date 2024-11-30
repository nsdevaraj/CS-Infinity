

[Leet Code #234](https://leetcode.com/problems/palindrome-linked-list/description/)


Given a singly linked list, determine if it is a palindrome. A linked list is considered a palindrome if it reads the same forward and backward.

```markdown
## Problem Statement: Palindrome Linked List


### Definition of a Singly Linked List Node:
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Example 1

**Input:**
```python
head = [1, 2, 2, 1]
```

**Output:**
```python
True
```

**Explanation:** The linked list reads `1 -> 2 -> 2 -> 1`, which is the same forwards and backwards.

---

### Example 2

**Input:**
```python
head = [1, 2]
```

**Output:**
```python
False
```

**Explanation:** The linked list reads `1 -> 2`, which is not the same forwards and backwards.

---

### Example 3

**Input:**
```python
head = [1, 2, 3, 2, 1]
```

**Output:**
```python
True
```

**Explanation:** The linked list reads `1 -> 2 -> 3 -> 2 -> 1`, which is the same forwards and backwards.





## Approaches to Solve Palindrome Linked List

### Approach 1: Reverse the Second Half

1. Find the midpoint of the linked list using the slow and fast pointer technique.
2. Reverse the second half of the linked list.
3. Compare the first half and the reversed second half node by node.
4. Restore the original linked list (optional).

**Time Complexity:** O(n)  
**Space Complexity:** O(1) (in-place reversal)

---

### Approach 2: Use a Stack

1. Traverse the linked list and push each node's value onto a stack.
2. Traverse the linked list again, popping values from the stack and comparing them with the current node's value.

**Time Complexity:** O(n)  
**Space Complexity:** O(n) (for the stack)

---

### Approach 3: Convert to Array/List

1. Traverse the linked list and store the values in an array or list.
2. Check if the array/list is a palindrome by comparing elements from the start and end.

**Time Complexity:** O(n)  
**Space Complexity:** O(n) (for the array/list)

---

### Approach 4: Recursive Approach

1. Use recursion to reach the end of the linked list.
2. During the unwinding of the recursion, compare the current node's value with the value from the previous calls.

**Time Complexity:** O(n)  
**Space Complexity:** O(n) (due to recursion stack)

---

### Summary of Approaches

- **Reverse the Second Half:** Efficient and in-place but modifies the linked list.
- **Use a Stack:** Simple and easy to implement but uses extra space.
- **Convert to Array/List:** Straightforward but not space-efficient.
- **Recursive Approach:** Clean but can hit stack limits with long lists.



```typescript
// Definition for singly-linked list node
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val: number = 0, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

// Approach 1: Reverse the Second Half
function isPalindromeReverse(head: ListNode | null): boolean {
    if (!head) return true;

    // Find the middle of the linked list
    let slow: ListNode | null = head;
    let fast: ListNode | null = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Reverse the second half of the list
    let prev: ListNode | null = null;
    while (slow) {
        const next: ListNode | null = slow.next;
        slow.next = prev;
        prev = slow;
        slow = next;
    }

    // Compare the first and second halves
    let left: ListNode | null = head;
    let right: ListNode | null = prev; // Start from the head of the reversed second half
    while (right) {
        if (left!.val !== right.val) return false;
        left = left!.next;
        right = right.next;
    }
    return true;
}

// Approach 2: Use a Stack
function isPalindromeStack(head: ListNode | null): boolean {
    const stack: number[] = [];
    let current: ListNode | null = head;

    // Push all node values onto the stack
    while (current) {
        stack.push(current.val);
        current = current.next;
    }

    // Compare values from the stack with the linked list
    current = head;
    while (current) {
        if (current.val !== stack.pop()) return false;
        current = current.next;
    }
    return true;
}

// Approach 3: Convert to Array/List
function isPalindromeArray(head: ListNode | null): boolean {
    const values: number[] = [];
    let current: ListNode | null = head;

    // Store all values in an array
    while (current) {
        values.push(current.val);
        current = current.next;
    }

    // Check if the array is a palindrome
    let left: number = 0;
    let right: number = values.length - 1;
    while (left < right) {
        if (values[left] !== values[right]) return false;
        left++;
        right--;
    }
    return true;
}

// Approach 4: Recursive Approach
function isPalindromeRecursive(head: ListNode | null): boolean {
    let left: ListNode | null = head;

    const check: (node: ListNode | null) => boolean = (right: ListNode | null) => {
        // Base case: if we reach the end of the list
        if (!right) return true;

        // Recursively check the rest of the list
        const result: boolean = check(right.next);
        // Compare values during the unwinding of the recursion
        if (!result) return false; // Early return if mismatch found
        const isEqual: boolean = left!.val === right.val;
        left = left!.next; // Move left pointer forward
        return isEqual;
    };

    return check(head);
}
```

### Comments:
- Each approach is designed to determine if a linked list is a palindrome using different methods, each with its own trade-offs regarding time and space complexity.
- The **reverse method** modifies the linked list, but it runs in O(n) time and O(1) space.
- The **stack method** is simple and runs in O(n) time but uses O(n) space.
- The **array method** also runs in O(n) time and uses O(n) space.
- The **recursive approach** is elegant but may run into stack overflow issues for very long linked lists, with O(n) time and O(n) space due to the recursion stack.



### Tests

```typescript
// Definition for singly-linked list node
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val: number = 0, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

// Test cases for the Palindrome Linked List function
interface PalindromeTestCase {
  name: string;
  input: ListNode | null; // Head of the linked list
  expected: boolean; // Expected result (true or false)
}

const palindromeTestCases: PalindromeTestCase[] = [
  // // Case 1: Empty list
  // {
  //   name: "Empty List",
  //   input: null,
  //   expected: true,
  // },
  // // Case 2: Single element
  // {
  //   name: "Single Element",
  //   input: new ListNode(1),
  //   expected: true,
  // },
  // // Case 3: Palindrome with two identical elements
  // {
  //   name: "Two Identical Elements",
  //   input: new ListNode(1, new ListNode(1)),
  //   expected: true,
  // },
  // // Case 4: Palindrome with odd number of elements
  // {
  //   name: "Odd Length Palindrome",
  //   input: new ListNode(1, new ListNode(2, new ListNode(1))),
  //   expected: true,
  // },
  // Case 5: Palindrome with even number of elements
  {
    name: "Even Length Palindrome",
    input: new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1)))),
    expected: true,
  },
  // // Case 6: Not a palindrome
  // {
  //   name: "Not a Palindrome",
  //   input: new ListNode(1, new ListNode(2, new ListNode(3))),
  //   expected: false,
  // },
  // // Case 7: Long palindrome
  // {
  //   name: "Long Palindrome",
  //   input: new ListNode(
  //     1,
  //     new ListNode(2, new ListNode(3, new ListNode(2, new ListNode(1)))),
  //   ),
  //   expected: true,
  // },
  // // Case 8: Long non-palindrome
  // {
  //   name: "Long Non-Palindrome",
  //   input: new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4)))),
  //   expected: false,
  // },
];

// Function to test the isPalindrome function
function testPalindrome(func: (head: ListNode | null) => boolean) {
  console.log(`Testing function: ${func.name}`);

  palindromeTestCases.forEach((testCase, index) => {
    const { input, expected, name } = testCase;
    const result = func(input);

    // Check if the returned result matches the expected result
    if (result !== expected) {
      console.error(
        `Test case ${index + 1} (${name}) failed: expected ${expected}, got ${result}`,
      );
    } else {
      // console.log(`Test case ${index + 1} (${name}) passed.`);
    }
  });

  console.log("All test cases executed!");
}

// Example function to be tested (replace with actual implementation)
function isPalindrome(head: ListNode | null): boolean {
  if (!head) {
    return true;
  }

  let slow: ListNode | null = head;
  let fast: ListNode | null = head;

  while (slow?.next && fast?.next?.next) {
    slow = slow!.next;
    fast = fast!.next!.next;
  }

  if (!slow?.next) {
    return true;
  } else {
    slow = slow!.next;
  }

  // console.log(slow, fast);

  let firstHalf: ListNode | null = head;
  let secondHalf: ListNode | null = slow;

  while (firstHalf && secondHalf) {
    console.log(firstHalf, secondHalf);
    if (firstHalf.val !== secondHalf.val) {
      return false;
    }
    firstHalf = firstHalf.next;
    secondHalf = secondHalf.next;
  }
  return true;
}

// Run the tests
testPalindrome(isPalindrome);


```