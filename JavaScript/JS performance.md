
[js perf @Fireship](https://www.youtube.com/watch?v=_pWA4rbzvIg)



The most important thing to measure is the performance of your application, not your modules or functions. Measure those once you’ve detected a performance issue with your app, and need to drill down as to why and fix the issue. A slow sum or sort is usually pointless to optimize if its impact on your app is negligible.


---
We've been able to squeeze out more by declaring i before and not using a lookup for the length. I know it sounds terrible, but it's ever so slightly faster. 

let i = 0; 
const len = arr.length for 
(; i < len; i++)


I can see .length as having a slight overhead and so making a difference over a big number of loops. But the declaration of i doesn't seem logical to me as that part of the for loop is only run once. Guess I have to try Deno bench now


---


Sure! Here’s the first section broken down into key points with code snippets where relevant:

### Five Rules of Programming by Rob Pike
1. **Do Not Talk About Programming**: Emphasizes focus on the task rather than discussing it.
2. **Measure, Don't Tune**: Always measure performance before optimizing. Optimize only when necessary.
   - **Quote**: "Premature optimization is the root of all evil." — Donald Knuth.
3. **Different Ways to Solve Problems**: There are multiple ways to achieve the same functionality in programming.
4. **Performance Matters**: The way you write your code can significantly affect performance.
5. **Use Simple Algorithms**: Simple solutions are less buggy and easier to implement.

### Benchmarking JavaScript Code
- **Tool**: Using **Deno** for benchmarking, which includes a built-in benchmarking tool.
- **Performance Measurement**:
  - **Goal**: Determine the fastest way to loop through an array and sum its values.

### Looping Over an Array in JavaScript
- **Methods to Sum Array Values**:
  1. **Array `forEach` Method**:
     ```javascript
     let sumForEach = (arr) => {
       let sum = 0;
       arr.forEach(num => {
         sum += num;
       });
       return sum;
     };
     ```

  2. **Array `reduce` Method**:
     ```javascript
     let sumReduce = (arr) => {
       return arr.reduce((acc, num) => acc + num, 0);
     };
     ```

  3. **Traditional `for` Loop**:
     ```javascript
     let sumForLoop = (arr) => {
       let sum = 0;
       for (let i = 0; i < arr.length; i++) {
         sum += arr[i];
       }
       return sum;
     };
     ```

  4. **`for...of` Loop**:
     ```javascript
     let sumForOf = (arr) => {
       let sum = 0;
       for (const num of arr) {
         sum += num;
       }
       return sum;
     };
     ```

### Performance Testing with Deno Bench
- **Setting Up the Benchmark**:
  - Create an array with 100,000 elements for testing.
  - Use Deno's `bench` method for each function.

```javascript
Deno.bench("Traditional for loop", () => {
  sumForLoop(largeArray);
});
Deno.bench("Array forEach", () => {
  sumForEach(largeArray);
});
Deno.bench("Array reduce", () => {
  sumReduce(largeArray);
});
Deno.bench("for...of loop", () => {
  sumForOf(largeArray);
});
```

- **Execution**: Run in the terminal with:
```bash
deno bench yourBenchmarkFile.ts
```

- **Expected Output**: Reports showing iterations per second, average execution time, etc.

### Conclusion on Loop Performance
- **Findings**:
  - Traditional `for` loop is typically the fastest due to less overhead.
  - Performance differences become pronounced with larger datasets (e.g., 1,000,000 elements).
  - For smaller datasets, the differences in performance diminish.

---
Here’s the second section with key points and relevant code snippets:

### Optimizing Array Value Searches
- **Common Method**: Using `Array.includes` to search for a value.
  - **Performance**: O(n) complexity, as it loops through the array.
  
  ```javascript
  let arrayIncludesSearch = (arr, value) => {
    return arr.includes(value);
  };
  ```

- **Optimized Method**: Using a **Set** for faster lookups.
  - **Performance**: O(1) complexity due to indexing.
  
  ```javascript
  let setSearch = (set, value) => {
    return set.has(value);
  };
  ```

- **Benchmarking Search Performance**:
  - Create a large array and a set for comparison.
  
  ```javascript
  const largeArray = Array.from({length: 100000}, (_, i) => `item${i}`);
  const largeSet = new Set(largeArray);
  
  const valuesToSearch = Array.from({length: 1000}, (_, i) => `item${Math.floor(Math.random() * 100000)}`);
  
  // Benchmarking
  Deno.bench("Array.includes", () => {
    valuesToSearch.forEach(value => arrayIncludesSearch(largeArray, value));
  });
  
  Deno.bench("Set.has", () => {
    valuesToSearch.forEach(value => setSearch(largeSet, value));
  });
  ```

### Sorting Arrays
- **Built-in Method**: JavaScript’s `Array.sort`.
  
  ```javascript
  let sortedArray = unsortedArray.sort((a, b) => a - b);
  ```

- **Custom Sorting Algorithms**:
  1. **Bubble Sort**:
     ```javascript
     const bubbleSort = (arr) => {
       let swapped;
       do {
         swapped = false;
         for (let i = 0; i < arr.length - 1; i++) {
           if (arr[i] > arr[i + 1]) {
             [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
             swapped = true;
           }
         }
       } while (swapped);
       return arr;
     };
     ```

  2. **Quick Sort**:
     ```javascript
     const quickSort = (arr) => {
       if (arr.length <= 1) return arr;
       const pivot = arr[arr.length - 1];
       const left = [];
       const right = [];
       for (let i = 0; i < arr.length - 1; i++) {
         if (arr[i] < pivot) left.push(arr[i]);
         else right.push(arr[i]);
       }
       return [...quickSort(left), pivot, ...quickSort(right)];
     };
     ```

  3. **Merge Sort**:
     ```javascript
     const mergeSort = (arr) => {
       if (arr.length <= 1) return arr;
       const mid = Math.floor(arr.length / 2);
       const left = mergeSort(arr.slice(0, mid));
       const right = mergeSort(arr.slice(mid));
       return merge(left, right);
     };

     const merge = (left, right) => {
       let result = [], i = 0, j = 0;
       while (i < left.length && j < right.length) {
         if (left[i] < right[j]) result.push(left[i++]);
         else result.push(right[j++]);
       }
       return result.concat(left.slice(i)).concat(right.slice(j));
     };
     ```

### Performance Benchmarking of Sorting Algorithms
- **Setting Up the Benchmark**:
  - Create an array of 10,000 random elements.
  
  ```javascript
  const randomArray = Array.from({length: 10000}, () => Math.floor(Math.random() * 10000));

  // Benchmarking sort methods
  Deno.bench("Array.sort", () => {
    randomArray.slice().sort((a, b) => a - b);
  });
  
  Deno.bench("Bubble Sort", () => {
    bubbleSort([...randomArray]);
  });

  Deno.bench("Quick Sort", () => {
    quickSort([...randomArray]);
  });

  Deno.bench("Merge Sort", () => {
    mergeSort([...randomArray]);
  });
  ```

### Conclusion on Sorting Performance
- **Findings**:
  - Built-in `Array.sort` is efficient for most use cases.
  - Custom implementations like quick sort can outperform built-in methods under certain conditions, especially for numerical data.
  - Bubble sort is generally the least efficient.
  - **Recommendation**: For sorting, stick with built-in methods unless specific optimizations are needed.

### General Takeaways
- **Benchmarking**: Essential to identify performance bottlenecks.
- **Built-in Methods**: Often optimized for general use and suitable for most applications.
- **Code Quality**: Prioritize getting functional code working before worrying about performance optimizations.

---

If you have any further questions or need additional details, feel free to ask!
