
[LeetCode #2 - Add Two Numbers](https://leetcode.com/problems/add-two-numbers)

# Add Two Numbers

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example 1

**Input:**

```
l1 = [2,4,3], l2 = [5,6,4]
```

**Output:**

```
[7,0,8]
```

**Explanation:** 342 + 465 = 807.

### Example 2

**Input:**

```
l1 = [0], l2 = [0]
```

**Output:**

```
[0]
```

### Example 3

**Input:**

```
l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
```

**Output:**

```
[8,9,9,9,0,0,0,1]
```

**Explanation:** 9999999 + 9999 = 10009998.

---

## Normal approach


```python

def add_two_nums(listHead1:Optional[ListNode], listHead2:Optional[ListNode])->Optional[ListNode]:
    num1, num2 = 0,0
    digit_power = 0

    while(listHead1 or listHead2):
        if(listHead1):
            num1 += ((10**digit_power)*listHead1.val)
            listHead1 = listHead1.next
        if(listHead2):
            num2 += ((10**digit_power)*listHead2.val)
            listHead2 = listHead2.next
        digit_power += 1

    sum_number = num1 + num2

    head = None
    prev = None
    while(sum_number):
        last_digit = sum_number % 10
        sum_number = sum_number // 10
        if(not prev):
            head = ListNode(last_digit)
            prev = head
        else:
            prev.next = ListNode(last_digit)
            prev = prev.next

    return head


```




---


## Approach 1: Elementary School Addition (Iterative)

The key idea behind solving this problem is to simulate the process of adding two numbers digit by digit, as we did in elementary school, starting from the least significant digit (rightmost digit).

- We start at the head of both linked lists.
- We sum the corresponding digits and carry from the previous step (if any).
- If one list is longer, treat the missing digits in the shorter list as zeros.

### Algorithm:
1. Initialize a dummy node to help build the result list.
2. Maintain a pointer `current` for the result list and a variable `carry` for handling overflow.
3. Traverse both linked lists:
   - Add corresponding digits from both lists and the carry.
   - Calculate the new sum and update the carry.
   - Create a new node in the result list with the computed value.
4. After the loop, if there’s any remaining carry, append a new node with its value.
5. Return the next node of the dummy (to exclude the dummy node itself).

### Code:



```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()  # Dummy node to simplify edge cases
    current = dummy  # Pointer to the result list
    carry = 0  # Initialize carry to 0
    
    # Traverse both lists
    while l1 or l2 or carry:
        # Get the current values (if a list is exhausted, use 0)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10  # Carry for the next iteration
        current.next = ListNode(total % 10)  # Create a new node for the digit
        
        # Move the pointers forward
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next  # Return the result list starting from the next of dummy node
```



```python


def add_two_nums(l1:Optional[ListNode], l2:Optional[ListNode])->Optional[ListNode]:
    carry_val = 0
    head = None
    prev = None
    while(l1 or l2 or carry_val):
        l1_val = l1.val if(l1) else 0
        l2_val = l2.val if(l2)  else 0

        total_val = l1_val + l2_val + carry_val

        digit_val = total_val % 10
        carry_val = 1 if total_val > 9 else 0

        node = ListNode(digit_val)
        if(not head or not prev):
            head = node
            prev = head
        else:
            prev.next = node
            prev = node

        if(l1):
            l1 = l1.next
        if(l2):
            l2 = l2.next

    if(carry_val and prev):
        total_val = carry_val + prev.val

        digit_val = total_val % 10
        carry_val = 1 if total_val / 10 > 1 else 0

        prev.val += digit_val
        if(carry_val):
            node = ListNode(carry_val)
            prev.next = node


    return head


```

### Time Complexity:
- **Time:** $O(\max(m, n))$, where $m$ and $n$ are the lengths of `l1` and `l2`. We iterate over both lists once.
- **Space:** $O(\max(m, n))$, since the new list will contain at most the number of nodes of the longer list plus one node for the carry (if required).

---

## Approach 2: Recursive Approach

An alternative to the iterative approach is to solve this problem recursively. The recursion can be used to simulate the process of adding numbers from the least significant to the most significant digit.

### Algorithm:
1. Recursively traverse both lists:
   - Add corresponding digits and carry recursively.
2. Base case: When both lists are exhausted, return `None`. Also handle carry if required at the end.
3. For each recursion level, return a new `ListNode` with the sum value.

### Code:

```python
# Recursive function to add two numbers
def addTwoNumbersRecursive(l1: ListNode, l2: ListNode, carry: int = 0) -> ListNode:
    # Base case: when both lists are exhausted and carry is 0
    if not l1 and not l2 and carry == 0:
        return None
    
    # Calculate current sum and carry
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    total = val1 + val2 + carry
    carry = total // 10
    
    # Create new node with the sum value
    current_node = ListNode(total % 10)
    
    # Recursively call for the next nodes
    next_l1 = l1.next if l1 else None
    next_l2 = l2.next if l2 else None
    current_node.next = addTwoNumbersRecursive(next_l1, next_l2, carry)
    
    return current_node
```

### Time Complexity:
- **Time:** $O(\max(m, n))$, similar to the iterative approach since we still visit each node once.
- **Space:** $O(\max(m, n))$, due to the recursion stack that grows as we traverse the lists.

---

## Summary of Approaches

| Approach  | Description                                                          | Time Complexity | Space Complexity |
| --------- | -------------------------------------------------------------------- | --------------- | ---------------- |
| Iterative | Simulates elementary addition using a dummy node and a carry.        | $O(\max(m, n))$ | $O(\max(m, n))$  |
| Recursive | Recursively adds corresponding digits and carries forward the carry. | $O(\max(m, n))$ | $O(\max(m, n))$  |



### Tests

```python

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the current node
        self.next = next  # Pointer to the next node in the list

    def __repr__(self):
        return f"{self.val} -> {self.next}"  # For easy printing of the list


def test_add_two_numbers(func):
    print(f"Testing function: {func.__name__}")

    def create_linked_list(lst):
        """Helper function to convert a list to a linked list"""
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next



    def linked_list_to_list(node:Optional[ListNode]):
        """Helper function to convert a linked list to a list"""
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    add_two_numbers_test_cases = [
        # Case 1: General case with small numbers
        {
            "name": "Small numbers",
            "l1": [2, 4, 3],
            "l2": [5, 6, 4],
            "expected": [7, 0, 8],
        },
        # Case 2: Different length lists
        {
            "name": "Different length lists",
            "l1": [1, 8],
            "l2": [0],
            "expected": [1, 8],
        },
        # Case 3: Both lists with multiple carry over
        {
            "name": "Multiple carry over",
            "l1": [9, 9, 9],
            "l2": [1],
            "expected": [0, 0, 0, 1],
        },
        # Case 4: Both lists are empty
        {
            "name": "Empty lists",
            "l1": [],
            "l2": [],
            "expected": [],
        },
        # Case 5: List with carry into a new digit
        {
            "name": "Carry into new digit",
            "l1": [5, 6],
            "l2": [5, 4],
            "expected": [0, 1, 1],
        }
    ]

    for i, test_case in enumerate(add_two_numbers_test_cases, 1):
        l1 = create_linked_list(test_case["l1"])
        l2 = create_linked_list(test_case["l2"])
        expected = create_linked_list(test_case["expected"])

        result = func(l1, l2)
        result_list = linked_list_to_list(result)
        expected_list = linked_list_to_list(expected)

        assert result_list == expected_list, f"Test case {i} ({test_case['name']}) failed: expected {expected_list}, got {result_list}"

    print("All test cases passed!")


```