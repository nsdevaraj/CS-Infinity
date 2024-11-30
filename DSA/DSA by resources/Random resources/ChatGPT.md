
Here are some well-structured coding interview questions that can help assess a candidate's problem-solving skills and coding proficiency:

1. **Reverse a Linked List**
   - Implement a function to reverse a singly linked list.

2. **Two Sum Problem**
   - Given an array of integers, return the indices of the two numbers that add up to a specific target.

3. **Longest Substring Without Repeating Characters**
   - Find the length of the longest substring without repeating characters in a given string.

4. **Merge Intervals**
   - Given a collection of intervals, merge all overlapping intervals.

5. **Valid Parentheses**
   - Determine if the input string containing just the characters '(', ')', '{', '}', '[' and ']' is valid.

6. **Binary Search**
   - Implement binary search on a sorted array. 

7. **Fibonacci Sequence**
   - Write a function that computes the nth Fibonacci number using both iterative and recursive methods.

8. **Maximum Subarray**
   - Find the contiguous subarray (containing at least one number) which has the largest sum.

9. **Check for Anagrams**
   - Given two strings, determine if they are anagrams of each other.

10. **Count Occurrences of an Element**
    - Write a function to count the occurrences of a given element in a sorted array.

11. **Find the Kth Largest Element in an Array**
    - Given an unsorted array, find the kth largest element.

12. **Balanced Binary Tree**
    - Check if a binary tree is height-balanced.

13. **N-Queens Problem**
    - Solve the N-Queens problem by placing N queens on an N×N chessboard.

14. **Implement a Queue using Stacks**
    - Create a queue using two stacks.

15. **Top K Frequent Elements**
    - Given a non-empty array of integers, return the k most frequent elements.

These questions cover various data structures and algorithms, providing a well-rounded assessment of a candidate's abilities.




### Implement a Queue using Stacks


Certainly! Implementing a queue using two stacks can be done by using one stack for enqueue operations and another for dequeue operations. Here's a simple implementation in Python:

```python
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue operations
        self.stack2 = []  # Stack for dequeue operations

    def enqueue(self, item):
        # Push the item onto stack1
        self.stack1.append(item)

    def dequeue(self):
        # If stack2 is empty, transfer items from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            raise IndexError("Dequeue from empty queue")
        
        # Pop the item from stack2
        return self.stack2.pop()

    def is_empty(self):
        # The queue is empty if both stacks are empty
        return not self.stack1 and not self.stack2

    def peek(self):
        # Get the front item of the queue without removing it
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            raise IndexError("Peek from empty queue")
        
        return self.stack2[-1]

    def size(self):
        # Return the total number of items in the queue
        return len(self.stack1) + len(self.stack2)

# Example usage:
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Outputs: 1
print(queue.peek())     # Outputs: 2
print(queue.size())     # Outputs: 2
```

### Explanation:
- **enqueue**: Adds an item to the end of the queue by pushing it onto `stack1`.
- **dequeue**: Removes the item from the front of the queue. If `stack2` is empty, it transfers all items from `stack1` to `stack2`, reversing their order. This makes the oldest element accessible for dequeue.
- **is_empty**: Checks if both stacks are empty.
- **peek**: Returns the front item of the queue without removing it, using the same logic as dequeue.
- **size**: Returns the total number of items in the queue.

This implementation ensures that both enqueue and dequeue operations are handled efficiently, adhering to the FIFO principle of a queue.


### Balanced Binary Tree


To check if a binary tree is height-balanced, we can define a balanced binary tree as one where the difference in heights between the left and right subtrees of any node is at most 1.

Here's a Python implementation of a function that checks if a binary tree is balanced:

### Definition of a Binary Tree Node
First, we'll define a simple class for the tree nodes:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

### Function to Check if the Binary Tree is Balanced
Now, let's implement the function to check for balance:

```python
def is_balanced(root):
    def check_balance(node):
        if not node:
            return 0  # Height of an empty tree is 0
        
        # Check the height of the left subtree
        left_height = check_balance(node.left)
        if left_height == -1:  # Left subtree is not balanced
            return -1
        
        # Check the height of the right subtree
        right_height = check_balance(node.right)
        if right_height == -1:  # Right subtree is not balanced
            return -1
        
        # Check the balance condition
        if abs(left_height - right_height) > 1:
            return -1  # Not balanced
        
        # Return the height of the subtree
        return max(left_height, right_height) + 1

    return check_balance(root) != -1
```

### Example Usage
Here's how you can use the above code to check if a binary tree is balanced:

```python
# Creating a balanced binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Checking if the tree is balanced
print(is_balanced(root))  # Outputs: True

# Creating an unbalanced binary tree
unbalanced_root = TreeNode(1)
unbalanced_root.left = TreeNode(2)
unbalanced_root.left.left = TreeNode(3)

# Checking if the unbalanced tree is balanced
print(is_balanced(unbalanced_root))  # Outputs: False
```

### Explanation:
1. **TreeNode Class**: A simple class to represent a node in a binary tree, with attributes for the value and pointers to left and right children.
2. **check_balance Function**: This recursive function calculates the height of each subtree while checking for balance:
   - If a subtree is found to be unbalanced, it returns -1.
   - Otherwise, it returns the height of the subtree.
3. **is_balanced Function**: This is the main function that calls `check_balance` on the root and checks if the return value indicates balance.

This implementation efficiently determines if the binary tree is balanced by calculating heights in a single traversal.



