
[LeetCode #160](https://leetcode.com/problems/intersection-of-two-linked-lists/)

### **Problem: Intersecting Linked Lists**

The problem is to find the node where two singly linked lists intersect. Given the heads of two singly linked lists, return the node at which the two lists intersect, or `null` if they do not intersect.

Here are the **TypeScript implementations** of the three approaches to solve the **Intersection of Linked Lists** problem:


Note: don't compare just values, also compare the object reference!

### 1. **Brute Force Approach**

For each node in List 1, iterate through all nodes in List 2 and check if the nodes match.

```typescript
class ListNode {
  val: number;
  next: ListNode | null = null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// Brute Force Approach
function getIntersectionNodeBruteForce(
  headA: ListNode | null,
  headB: ListNode | null
): ListNode | null {
  let currentA = headA;
  
  // Traverse List A
  while (currentA) {
    let currentB = headB;
    
    // For each node in List A, traverse List B
    while (currentB) {
      if (currentA === currentB) {
        return currentA; // Intersection found
      }
      currentB = currentB.next;
    }
    
    currentA = currentA.next;
  }
  
  return null; // No intersection
}
```



- **Time Complexity**: \( O(m \times n) \)
- **Space Complexity**: \( O(1) \)

---

### 2. **Using Hashing Approach**

Store all nodes of List 1 in a hash set, then traverse List 2 to check if any node appears in the hash set.

```typescript
// Hashing Approach
function getIntersectionNodeHashing(
  headA: ListNode | null,
  headB: ListNode | null
): ListNode | null {
  const nodesInA = new Set<ListNode>();

  let currentA = headA;
  
  // Traverse List A and store each node in the set
  while (currentA) {
    nodesInA.add(currentA);
    currentA = currentA.next;
  }

  let currentB = headB;

  // Traverse List B and check if any node is in the set
  while (currentB) {
    if (nodesInA.has(currentB)) {
      return currentB; // Intersection found
    }
    currentB = currentB.next;
  }

  return null; // No intersection
}
```

- **Time Complexity**: \( O(m + n) \)
- **Space Complexity**: \( O(m) \), where \( m \) is the length of List A.

---

### 3. **Two-Pointer Technique (Optimal Approach)**

Using two pointers, traverse both lists. When either pointer reaches the end, redirect it to the head of the other list. Both pointers will meet at the intersection or reach the end (null) simultaneously if there's no intersection.

```typescript
// Two-Pointer Approach (Optimal)
function getIntersectionNodeTwoPointer(
  headA: ListNode | null,
  headB: ListNode | null
): ListNode | null {
  if (!headA || !headB) return null;

  let pointerA: ListNode | null = headA;
  let pointerB: ListNode | null = headB;

  // Traverse both lists
  while (pointerA !== pointerB) {
    // Move to the next node or switch to the head of the other list
    pointerA = pointerA ? pointerA.next : headB;
    pointerB = pointerB ? pointerB.next : headA;
  }

  // They meet either at the intersection node or both become null
  return pointerA;
}
```

- **Time Complexity**: \( O(m + n) \)
- **Space Complexity**: \( O(1) \)

---

### **Explanation of Each Approach:**

1. **Brute Force**:
   - For each node in List A, traverse through List B to check for an intersection. This results in a time complexity of \( O(m \times n) \), as both lists are fully traversed multiple times.

2. **Hashing**:
   - Store all nodes of List A in a hash set, which allows constant-time lookups while traversing List B. If any node from List B exists in the set, it's the intersection. This approach runs in \( O(m + n) \) but requires \( O(m) \) extra space for storing nodes.

3. **Two-Pointer**:
   - Using two pointers, each pointer travels the length of both lists. If there is an intersection, both pointers will eventually meet at the intersection point. This approach is optimal in terms of both time \( O(m + n) \) and space \( O(1) \), as it uses no extra memory.

---

You can now use these implementations based on the specific requirements or constraints of your problem! Let me know if you need further clarifications or enhancements.
