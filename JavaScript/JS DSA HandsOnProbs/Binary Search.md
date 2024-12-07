
### **47. Write a function to perform binary search on a sorted array.**

#### **Answer:**

```javascript
function binarySearch(arr, target) {
  let left = 0, right = arr.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return -1;
}
// Usage:
console.log(binarySearch([1, 2, 3, 4, 5], 3)); // 2
```

