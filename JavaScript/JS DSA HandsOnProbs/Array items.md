


### **44. How would you implement a function to shuffle an array?**

#### **Answer:**

```javascript
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}
// Usage:
console.log(shuffleArray([1, 2, 3, 4, 5]));
```




### **16. Write a function to merge two sorted arrays.**

#### **Answer:**

```javascript
function mergeArrays(arr1, arr2) {
  const result = [];
  let i = 0, j = 0;

  while (i < arr1.length && j < arr2.length) {
    result.push(arr1[i] < arr2[j] ? arr1[i++] : arr2[j++]);
  }
  return result.concat(arr1.slice(i)).concat(arr2.slice(j));
}
```


