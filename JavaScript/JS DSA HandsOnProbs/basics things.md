
Here’s a list of popular JavaScript coding interview questions with concise answers:

---

### **1. Reverse a String**

**Question:** Write a function to reverse a string.  
**Answer:**

```javascript
function reverseString(str) {
  return str.split('').reverse().join('');
}
```

---

### **2. Check for Palindrome**

**Question:** Write a function to check if a string is a palindrome (reads the same forward and backward).  
**Answer:**

```javascript
function isPalindrome(str) {
  const cleanedStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  return cleanedStr === cleanedStr.split('').reverse().join('');
}
```

---

### **3. FizzBuzz**

**Question:** Write a function that prints numbers 1 to 100, but for multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both print "FizzBuzz".  
**Answer:**

```javascript
function fizzBuzz() {
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log('FizzBuzz');
    } else if (i % 3 === 0) {
      console.log('Fizz');
    } else if (i % 5 === 0) {
      console.log('Buzz');
    } else {
      console.log(i);
    }
  }
}
```

---

### **4. Find the Largest Number in an Array**

**Question:** Write a function that returns the largest number in an array.  
**Answer:**

```javascript
function findLargestNumber(arr) {
  return Math.max(...arr);
}
```

---

### **5. Remove Duplicates from an Array**

**Question:** Write a function to remove duplicate values from an array.  
**Answer:**

```javascript
function removeDuplicates(arr) {
  return [...new Set(arr)];
}
```

---

### **6. Flatten an Array**

**Question:** Write a function to flatten a nested array.  
**Answer:**

```javascript
function flattenArray(arr) {
  return arr.flat(Infinity);
}
```

---

### **7. Merge Two Sorted Arrays**

**Question:** Write a function that merges two sorted arrays into one sorted array.  
**Answer:**

```javascript
function mergeSortedArrays(arr1, arr2) {
  return [...arr1, ...arr2].sort((a, b) => a - b);
}
```

---

### **8. Sum of All Numbers in an Array**

**Question:** Write a function that returns the sum of all numbers in an array.  
**Answer:**

```javascript
function sumArray(arr) {
  return arr.reduce((sum, num) => sum + num, 0);
}
```

---

### **9. Find the Factorial of a Number**

**Question:** Write a function to find the factorial of a number.  
**Answer:**

```javascript
function factorial(n) {
  if (n === 0) return 1;
  return n * factorial(n - 1);
}
```

---

### **10. Debounce Function**

**Question:** Implement a debounce function (limits how often a function is called).  
**Answer:**

```javascript
function debounce(func, delay) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), delay);
  };
}
```

---

### **11. Deep Clone an Object**

**Question:** Write a function to deep clone an object (without references).  
**Answer:**

```javascript
function deepClone(obj) {
  return JSON.parse(JSON.stringify(obj));
}
```

---

### **12. Find Missing Number in an Array**

**Question:** Write a function that finds the missing number in a sequence (1 to n).  
**Answer:**

```javascript
function findMissingNumber(arr, n) {
  const expectedSum = (n * (n + 1)) / 2;
  const actualSum = arr.reduce((sum, num) => sum + num, 0);
  return expectedSum - actualSum;
}
```

---

### **13. Count Occurrences of an Element in an Array**

**Question:** Write a function that counts the occurrences of a specific element in an array.  
**Answer:**

```javascript
function countOccurrences(arr, element) {
  return arr.filter(item => item === element).length;
}
```

---

### **14. Convert an Object to Query String**

**Question:** Write a function to convert an object into a query string for a URL.  
**Answer:**

```javascript
function toQueryString(obj) {
  return Object.keys(obj)
    .map(key => `${encodeURIComponent(key)}=${encodeURIComponent(obj[key])}`)
    .join('&');
}
```

---

### **15. Throttle Function**

**Question:** Implement a throttle function (limits the frequency of function calls).  
**Answer:**

```javascript
function throttle(func, limit) {
  let lastFunc;
  let lastRan;
  return function(...args) {
    if (!lastRan) {
      func(...args);
      lastRan = Date.now();
    } else {
      clearTimeout(lastFunc);
      lastFunc = setTimeout(() => {
        if (Date.now() - lastRan >= limit) {
          func(...args);
          lastRan = Date.now();
        }
      }, limit - (Date.now() - lastRan));
    }
  };
}
```

---

These answers cover common JavaScript problems and their efficient solutions for coding interviews. Let me know if you need more questions or clarifications!