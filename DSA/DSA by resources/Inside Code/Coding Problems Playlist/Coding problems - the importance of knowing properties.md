

[Coding problems: the importance of knowing properties - Inside code](https://youtu.be/5CrU0ldetF4?si=Cp9Zmf0iF66L8n7Y)



### Coding Problems: The Importance of Knowing Properties - Inside Code

Welcome to this **Inside Code** where we'll explore the importance of understanding **properties** when solving coding problems.

#### What Are Properties?
**Properties** are characteristics that define an element. For example, consider a **binary search tree (BST)**:
- All nodes in the left subtree are smaller than the root.
- All nodes in the right subtree are greater than the root.
- Performing an inorder traversal on a BST yields sorted values.
- Operations like insert, delete, and search can be done in **O(h)** time complexity, where **h** is the height of the tree.

Understanding these properties helps you fully grasp a problem, find an efficient solution, and analyze its time and space complexity.

#### Example 1: Checking If a String Can Be Rearranged Into a Palindrome

A **palindrome** is a string that reads the same forward and backward, like `"racecar"`. Suppose we want to check if a string can be rearranged into a palindrome. 

**Naive approach**: Generate all permutations of the string and check if any of them is a palindrome. This would result in a The time complexity of $O(n \cdot n!)$.
, where **n** is the length of the string. Highly inefficient!

**Optimized approach**: The property of palindromes is that every character must appear an even number of times, except at most one character which can appear an odd number of times.

##### Example:
- Input: `"abbcabbbb"`
- Output: `True` (Can be rearranged into `"babbcbbab"`)

#### Code:

```python
from collections import Counter

def can_be_palindrome(s: str) -> bool:
    """
    Check if the string can be rearranged into a palindrome.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    counter = Counter(s)
    # Count how many characters have an odd number of occurrences
    odd_count = sum(1 for count in counter.values() if count % 2 == 1)
    return odd_count <= 1
```

**Time Complexity**:  
- Traversing the string and updating the count map takes **O(n)**, where **n** is the length of the string.
- Checking the counts also takes **O(n)**.

**Space Complexity**:  
- The space complexity is **O(n)** due to the storage of character counts.

#### Example 2: Reversing a Singly Linked List

We want to reverse a **singly linked list**. A naive approach might be to reverse it as if it were an array—using two pointers. But with a singly linked list, we can't traverse backwards. 

No problem! If you're looking for a **O(n²)** approach to reversing a linked list, it usually involves repeatedly traversing the list to find the previous node for each node you want to reverse. While this method is inefficient and not typically used for reversing a linked list, here’s how it might look conceptually:

### O(n²) Approach for Reversing a Linked List

In this approach, for each node in the linked list, we traverse the entire list to find its previous node, and we do this for each node. This results in a quadratic time complexity.

### Code Example:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListQuadratic(head: ListNode) -> ListNode:
    """
    Reverse a singly linked list using an O(n^2) approach.
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    # Initialize the new head of the reversed list
    new_head = None
    current = head
    
    # While there are nodes left in the original list
    while current:
        # Store the next node
        next_node = current.next
        
        # Find the previous node of current
        prev = None
        temp = head
        while temp != current:
            prev = temp
            temp = temp.next
            
        # Reverse the link
        current.next = new_head
        new_head = current
        
        # If we found a previous node, set its next to None
        if prev:
            prev.next = next_node
        
        current = next_node  # Move to the next node in the original list
    
    return new_head
```

### Explanation of the Code:
1. **Initialization**: Start with `new_head` as `None`, which will eventually become the head of the reversed list. Set `current` to point to the head of the original list.
2. **Outer Loop**: Iterate through each node in the original list.
3. **Inner Loop**: For each `current` node, traverse the list from the head to find the previous node. This is the part that causes the **O(n²)** time complexity, as you may need to iterate through the entire list for each node.
4. **Reversing the Link**: Set `current.next` to point to `new_head`, effectively reversing the link.
5. **Updating Pointers**: Move `new_head` to `current`, and update `current` to the next node.
6. **Return the New Head**: Once all nodes have been processed, return `new_head`, which now points to the head of the reversed list.

### Time Complexity:
- The time complexity is **O(n²)** because for each of the `n` nodes in the list, we may traverse up to `n` nodes to find its previous node.

### Space Complexity:
- The space complexity is **O(1)** since we are not using any additional data structures that scale with input size.

### Summary
This quadratic approach is inefficient for reversing a linked list and is not practical in real-world applications. The more common approaches (iterative or recursive) are both **O(n)** in time complexity and are significantly more efficient.

I've opened the uploaded image, which contains a Python code snippet for reversing a singly linked list using a nested loop approach. Here's a detailed explanation of how this code works, along with the time complexity analysis:

### Code Explanation

```python
for i in range(length // 2):
    right = list.head
    for j in range(length - i - 1):
        right = right.next
    left.data, right.data = right.data, left.data
    left = left.next
```

1. **Outer Loop (`for i in range(length // 2):`)**:
   - This loop runs half the length of the linked list. It effectively decides how many pairs of nodes need to be swapped to reverse the entire list.
   - If the list has `n` elements, this loop will iterate `n/2` times.

2. **Inner Loop (`for j in range(length - i - 1):`)**:
   - This inner loop is responsible for moving the `right` pointer to the correct position in the linked list for each iteration of the outer loop.
   - The `right` pointer starts at the head of the list for each iteration of the outer loop and moves forward until it reaches the last node that hasn't been swapped yet.

3. **Swapping Values (`left.data, right.data = right.data, left.data`)**:
   - Once the `right` pointer is positioned correctly, the values of the nodes at `left` and `right` are swapped.
   - The `left` pointer is then moved one step forward to the next node.

4. **Moving the `left` Pointer (`left = left.next`)**:
   - After the swap, the `left` pointer is advanced to the next node, preparing for the next iteration of the outer loop.

### Time Complexity Analysis

The time complexity of this algorithm can be analyzed as follows:

- **Outer Loop**: Runs for `n/2` iterations (where `n` is the length of the linked list).
- **Inner Loop**: For each iteration of the outer loop, it runs a number of iterations equal to `length - i - 1`, which starts at `n-1` and goes down to `1`. The number of iterations for the inner loop can be approximated as follows:
  
  - First iteration: `n - 1`
  - Second iteration: `n - 2`
  - ...
  - Last iteration: `1`

- The total number of operations can be expressed as:
  
  $$ T(n) = (n-1) + (n-2) + \ldots + 1 = \frac{(n-1) \cdot n}{2} $$

This simplifies to:

$$ T(n) = O(n^2) $$

### Space Complexity

- The space complexity of this algorithm is **O(1)**, as it only uses a fixed number of pointers (i.e., `left`, `right`, `i`, and `j`) regardless of the size of the input linked list.

### Conclusion

Using this approach, reversing a singly linked list takes **O(n²)** time due to the nested loops, which is inefficient compared to the **O(n)** time complexity achievable through a more optimal method using three pointers. The space complexity is minimal, requiring only a constant amount of extra space.


Instead, we can use three pointers: **previous**, **current**, and **next** to reverse the list in **O(n)** time.

##### Code:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    """
    Reverse a singly linked list.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    previous = None
    current = head
    while current:
        next_node = current.next  # Save the next node
        current.next = previous   # Reverse the current node's pointer
        previous = current        # Move previous to current node
        current = next_node       # Move to next node
    return previous
```

**Time Complexity**:  
- Traversing the list once takes **O(n)**, where **n** is the number of nodes.

**Space Complexity**:  
- Since we use only constant extra space (for the three pointers), the space complexity is **O(1)**.

#### Example 3: Counting Distinct Permutations of a String

Suppose we want to count how many distinct permutations of a string we can generate. The brute-force approach would be to generate all permutations, eliminate duplicates, and return the count. This results in **O(n!)** time complexity.


The image you provided illustrates a brute-force approach to count distinct permutations of a string by generating all possible permutations, removing duplicates, and returning the count. Here’s how this approach works, along with the code implementation and explanations.

### Problem Definition

**Goal:** Given a string, count how many distinct permutations can be generated from its characters.

**Brute-force Approach Steps:**
1. **Generate all permutations** of the string.
2. **Remove duplicates** since some characters may repeat.
3. **Return the length** of the unique permutations.

### Time Complexity
- The brute-force solution has a time complexity of **O(n!)**, where \(n\) is the length of the string. This is because the number of permutations of \(n\) items is \(n!\). 

### Code Implementation

Here is a Python code snippet that implements the brute-force approach:

```python
from itertools import permutations

def count_distinct_permutations(s: str) -> int:
    """
    Count the number of distinct permutations of a given string.
    
    Parameters:
    s (str): The input string for which we want to find distinct permutations.
    
    Returns:
    int: The count of distinct permutations.
    """
    # Step 1: Generate all permutations
    all_permutations = permutations(s)
    
    # Step 2: Use a set to eliminate duplicates
    unique_permutations = set(all_permutations)
    
    # Step 3: Return the length of the set
    return len(unique_permutations)

# Example usage:
input_str = "aabc"
result = count_distinct_permutations(input_str)
print(f"The number of distinct permutations of '{input_str}' is: {result}")
```

### Explanation of the Code

1. **Imports**: 
   - The `itertools` module is imported to use the `permutations` function, which generates all possible permutations of the input string.

2. **Function Definition**:
   - The function `count_distinct_permutations` takes a string `s` as an argument.

3. **Generating Permutations**:
   - The `permutations(s)` function generates all permutations of the string `s`. This results in a sequence of tuples, where each tuple represents a permutation.

4. **Removing Duplicates**:
   - By converting the list of permutations to a `set`, duplicates are automatically removed since sets do not allow duplicate values.

5. **Returning the Count**:
   - The function returns the length of the set, which represents the count of distinct permutations.

### Example Usage
- When the input string is `"aabc"`, the function generates the permutations:
  - `['aabc', 'aacb', 'abac', 'abca', 'acab', 'acba', 'baac', 'baca', 'bcaa', 'cbaa', 'caab', 'cab']`
- The distinct permutations are calculated, resulting in a count of `12`.

### Conclusion
While the brute-force method is straightforward and works for small strings, it becomes inefficient for longer strings due to the factorial growth of permutations. For large inputs, a more optimized approach should be considered, leveraging properties of permutations and combinatorics to reduce the time complexity. If you need information about the optimized approach, let me know!


However, there's a property of permutations that allows us to calculate the number of distinct permutations using **factorials**:
- If the string has **n** characters and some characters repeat, the number of distinct permutations is:

$$
\frac{n!}{k_1! \cdot k_2! \cdot \dots \cdot k_m!}
$$


Where **k_1, k_2, \dots, k_m** are the counts of each distinct character.

##### Example:
- Input: `"aaabb"`
- Output: `10` (Permutations like `"aabab"`, `"baaab"`, etc.)

#### Code:

```python
from collections import Counter
import math

def possible_permutations(s: str) -> int:
    """
    Count distinct permutations of a string.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    counter = Counter(s)
    numerator = math.factorial(len(s))
    denominator = math.prod(math.factorial(count) for count in counter.values())
    return numerator // denominator
```

**Time Complexity**:  
- Building the character count map takes **O(n)**.
- Calculating the factorials and their product is also **O(n)**.

**Space Complexity**:  
- The space complexity is **O(n)** due to the character count storage.

---

### Conclusion: Why Knowing Properties Matters

In each of these examples, knowing the **properties** of the data structures and the problem allows us to avoid brute-force solutions and come up with more efficient approaches. Whether it's recognizing that only one character can have an odd count in a palindrome, or knowing that we can't move backwards in a singly linked list, understanding these properties leads to better problem-solving and more efficient algorithms.

If you want to dive deeper into mastering coding problems, check out our **50 popular coding interview problems** course, where you can learn about topics like the longest common subsequence, 0-1 knapsack, and much more!



