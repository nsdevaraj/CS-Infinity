

[Kth largest element - YT(InsideCode) ](https://www.youtube.com/watch?v=o3DUXPRyvT8&list=PL3edoBgC7ScW_CBHbMc0FtdXfzgpBOGIb&index=29&t=812s)

[LeetCode #215](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)


## Kth smalled element in unsorted array 
## Problem statement

### Problem Statement: Find the Kth Smallest Element in an Unsorted Array

Given an unsorted array of integers and an integer `k`, your task is to find the `k`th smallest element in the array. The `k`th smallest element is defined as the element that would be in the `k`th position if the array were sorted.

### Input

- An unsorted array of integers `arr` (1 ≤ |arr| ≤ 10^5).
- An integer `k` (1 ≤ k ≤ |arr|).

### Output

- Return the `k`th smallest element in the array.

### Examples

#### Example 1

**Input:**
```plaintext
arr = [3, 2, 1, 5, 6, 4]
k = 2
```

**Output:**
```plaintext
2
```

**Explanation:** The second smallest element in the sorted version of the array `[1, 2, 3, 4, 5, 6]` is `2`.

---

#### Example 2

**Input:**
```plaintext
arr = [7, 10, 4, 3, 20, 15]
k = 3
```

**Output:**
```plaintext
7
```

**Explanation:** The third smallest element in the sorted version of the array `[3, 4, 7, 10, 15, 20]` is `7`.

---

#### Example 3

**Input:**
```plaintext
arr = [1, 5, 2, 4, 3]
k = 1
```

**Output:**
```plaintext
1
```

**Explanation:** The first smallest element in the sorted version of the array is `1`.

---

#### Example 4

**Input:**
```plaintext
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
k = 5
```

**Output:**
```plaintext
5
```

**Explanation:** The fifth smallest element in the sorted version of the array `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` is `5`.

---

#### Example 5

**Input:**
```plaintext
arr = [8, 7, 6, 5, 4, 4, 3, 2, 1]
k = 4
```

**Output:**
```plaintext
4
```

**Explanation:** The fourth smallest element in the sorted version of the array is `4`, which appears twice.

---

### Constraints

- The array can contain duplicate elements.
- The value of `k` is guaranteed to be within the bounds of the array length.

### Note

The solution should be efficient, ideally with a time complexity of O(n) on average, as this is typically achievable using algorithms like Quickselect.


## Soln

### use  sort

```ts
// Approach: inbuilt sorting
// Time - O(nlogn) - Sort func
// Spacke - O(1)- inplace sorting, no extra space
const kthSmallestElement1 = (ary: number[], k: number): number | null => {
  const aryLen = ary.length;
  if (k > aryLen) return null;
  ary.sort((a, b) => a - b);
  return ary[k - 1];
};

```


```ts

// Approach: finding minimum upto k
// Time - O(kn) - Sort upto k , at worst case n-1 times => kn - (k(k-1)/2) ~ kn
// Spacke - O(1)- inplace shifting, no extra space
const kthSmallestElement2 = (ary: number[], k: number): number | null => {
  const aryLen = ary.length;
  if (k > aryLen) return null;

  for (let i = 0; i < k; i++) {
    let minIndex = i;
    for (let j = i + 1; j < aryLen; j++) {
      if (ary[j] < ary[minIndex]) minIndex = j;
    }
    if (i !== minIndex) {
      [ary[i], ary[minIndex]] = [ary[minIndex], ary[i]];
    }
  }

  return ary[k - 1];
};

```



The choice between \(O(n \log n)\) and \(O(kn)\) depends on the values of \(k\) and \(n\) in the context of your problem:

1. **When \(k\) is small (e.g., \(k < \log n\)):**
   - \(O(kn)\) becomes \(O(n)\), which is better than \(O(n \log n)\).

2. **When \(k\) is comparable to \(n\) (e.g., \(k \approx n\)):**
   - \(O(kn)\) becomes \(O(n^2)\), which is worse than \(O(n \log n)\).

3. **When \(k\) is a constant (e.g., \(k = 10\)):**
   - \(O(kn)\) becomes \(O(n)\), which is better than \(O(n \log n)\).

### Conclusion:
- If \(k\) is small relative to \(n\), the \(O(kn)\) approach may be preferable.
- If \(k\) is close to \(n\) or if \(n\) is large, \(O(n \log n)\) is usually more efficient.

In general, for larger datasets, the sorting-based approach (\(O(n \log n)\)) is more efficient unless you are specifically looking for a very small \(k\).





## Refs

to check {
by chatGPT

Certainly! Here are several different approaches to find the k-th smallest element in an unsorted array:

### 1. **Sorting Approach**
- **Description:** Sort the array and return the k-th element.
- **Time Complexity:** \(O(n \log n)\)
- **Space Complexity:** \(O(1)\) (if sorting in-place).
  
```javascript
const kthSmallestElement1 = (ary, k) => {
  ary.sort((a, b) => a - b);
  return ary[k - 1];
};
```

### 2. **Selection Algorithm (Quickselect)**
- **Description:** This is a modified version of the QuickSort algorithm. It partitions the array around a pivot and only recurses into the part of the array that contains the k-th smallest element.
- **Average Time Complexity:** \(O(n)\)
- **Worst Case Time Complexity:** \(O(n^2)\) (but can be mitigated with random pivoting).
- **Space Complexity:** \(O(1)\) (in-place).
  
```javascript
const partition = (ary, low, high, pivotIndex) => {
  const pivotValue = ary[pivotIndex];
  [ary[pivotIndex], ary[high]] = [ary[high], ary[pivotIndex]]; // Move pivot to end
  let storeIndex = low;

  for (let i = low; i < high; i++) {
    if (ary[i] < pivotValue) {
      [ary[storeIndex], ary[i]] = [ary[i], ary[storeIndex]];
      storeIndex++;
    }
  }
  [ary[storeIndex], ary[high]] = [ary[high], ary[storeIndex]];
  return storeIndex;
};

const quickSelect = (ary, low, high, k) => {
  if (low === high) return ary[low];
  const pivotIndex = Math.floor(Math.random() * (high - low + 1)) + low;
  const newPivotIndex = partition(ary, low, high, pivotIndex);
  
  if (k === newPivotIndex) {
    return ary[k];
  } else if (k < newPivotIndex) {
    return quickSelect(ary, low, newPivotIndex - 1, k);
  } else {
    return quickSelect(ary, newPivotIndex + 1, high, k);
  }
};

const kthSmallestElement2 = (ary, k) => {
  return quickSelect(ary, 0, ary.length - 1, k - 1);
};
```

### 3. **Min-Heap Approach**
- **Description:** Build a min-heap from the array and then extract the minimum k times. The k-th extraction will give the k-th smallest element.
- **Time Complexity:** \(O(n + k \log n)\)
- **Space Complexity:** \(O(n)\) for the heap.
  
```javascript
class MinHeap {
  constructor() {
    this.heap = [];
  }

  insert(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  bubbleUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      const element = this.heap[index];
      const parentIndex = Math.floor((index - 1) / 2);
      const parent = this.heap[parentIndex];
      if (parent <= element) break;
      this.heap[index] = parent;
      this.heap[parentIndex] = element;
      index = parentIndex;
    }
  }

  remove() {
    const min = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = end;
      this.sinkDown();
    }
    return min;
  }

  sinkDown() {
    let index = 0;
    const length = this.heap.length;
    const element = this.heap[0];

    while (true) {
      let leftChildIndex = 2 * index + 1;
      let rightChildIndex = 2 * index + 2;
      let leftChild, rightChild;
      let swap = null;

      if (leftChildIndex < length) {
        leftChild = this.heap[leftChildIndex];
        if (leftChild < element) swap = leftChildIndex;
      }
      if (rightChildIndex < length) {
        rightChild = this.heap[rightChildIndex];
        if (
          (swap === null && rightChild < element) ||
          (swap !== null && rightChild < leftChild)
        ) {
          swap = rightChildIndex;
        }
      }
      if (swap === null) break;
      this.heap[index] = this.heap[swap];
      this.heap[swap] = element;
      index = swap;
    }
  }
}

const kthSmallestElement3 = (ary, k) => {
  const minHeap = new MinHeap();
  for (const num of ary) {
    minHeap.insert(num);
  }
  let kthSmallest;
  for (let i = 0; i < k; i++) {
    kthSmallest = minHeap.remove();
  }
  return kthSmallest;
};
```

### 4. **Counting Sort (for a known range)**
- **Description:** If the range of numbers is known (e.g., integers between 1 and 100), you can use counting sort to find the k-th smallest element.
- **Time Complexity:** \(O(n + r)\), where \(r\) is the range of the numbers.
- **Space Complexity:** \(O(r)\) for the count array.

```javascript
const kthSmallestElement4 = (ary, k, range) => {
  const count = new Array(range + 1).fill(0);

  for (const num of ary) {
    count[num]++;
  }

  let total = 0;
  for (let i = 0; i < count.length; i++) {
    total += count[i];
    if (total >= k) {
      return i;
    }
  }

  return null; // k is out of bounds
};
```

### Summary of Approaches
- **Sorting Approach:** Simple but not optimal for large \(n\).
- **Quickselect:** Average \(O(n)\) performance, best for general cases.
- **Min-Heap:** Good when you need to find multiple k-th smallest elements, but more space-intensive.
- **Counting Sort:** Efficient for small ranges of integers, but not suitable for arbitrary values.

Choose the approach that best fits your specific use case based on the size of the input and the properties of the elements in the array!


}





## Test 

```ts
const KTH_SMALLEST_TEST_CASES = [
  {
    name: "General Case",
    input: { arr: [3, 2, 1, 5, 6, 4], k: 2 },
    expected: 2,
    reason: "The second smallest element is 2.",
  },
  {
    name: "All Elements Same",
    input: { arr: [5, 5, 5, 5, 5], k: 3 },
    expected: 5,
    reason: "All elements are the same; thus, the 3rd smallest is also 5.",
  },
  {
    name: "Negative and Positive Numbers",
    input: { arr: [-1, 2, 0, -5, 4], k: 3 },
    expected: 0,
    reason: "The third smallest element is 0.",
  },
  {
    name: "Sorted Array",
    input: { arr: [1, 2, 3, 4, 5], k: 4 },
    expected: 4,
    reason: "The fourth smallest element is 4.",
  },
  {
    name: "Reversed Sorted Array",
    input: { arr: [10, 9, 8, 7, 6], k: 2 },
    expected: 7,
    reason: "The second smallest element is 7.",
  },
  {
    name: "Single Element",
    input: { arr: [42], k: 1 },
    expected: 42,
    reason: "The only element is also the 1st smallest.",
  },
  {
    name: "Large Numbers",
    input: { arr: [1000, 2000, 3000, 4000, 5000], k: 5 },
    expected: 5000,
    reason: "The fifth smallest element is 5000.",
  },
  {
    name: "Mixed Elements",
    input: { arr: [7, 10, 4, 3, 20, 15], k: 4 },
    expected: 10,
    reason: "The fourth smallest element is 10.",
  },
  {
    name: "Duplicates and Unique",
    input: { arr: [1, 3, 1, 2, 4, 2], k: 3 },
    expected: 2,
    reason: "The third smallest element is 2 (1, 1, 2).",
  },
  {
    name: "Edge Case with k Equal to Length",
    input: { arr: [2, 1], k: 2 },
    expected: 2,
    reason: "The second smallest element in [1, 2] is 2.",
  },
];

const testKthSmallestFunc = (func: Function) => {
  console.log(`Testing func: ${func.name}`);
  for (const testCase of KTH_SMALLEST_TEST_CASES) {
    const { arr, k } = testCase.input;
    const funcOutput = func(arr, k);
    console.assert(
      funcOutput === testCase.expected,
      `Test case '${testCase.name}' failed: expected ${testCase.expected}, but got ${funcOutput}. Reason: ${testCase.reason}`,
    );
  }

  console.log("All test cases completed!");
};
```



[[kth largest element]]





