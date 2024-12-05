
### **24. Write a function to find the longest substring without repeating characters.**

#### **Answer:**

```javascript
function longestSubstring(s) {
  let set = new Set(), maxLen = 0, left = 0;

  for (let right = 0; right < s.length; right++) {
    while (set.has(s[right])) set.delete(s[left++]);
    set.add(s[right]);
    maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
}
// Example:
console.log(longestSubstring("abcabcbb")); // 3
```


