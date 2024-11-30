

### Built-in Data Structures in JavaScript

1. **Arrays**
   - Arrays hold a dynamic collection of indexed items and are created using square brackets.
   ```javascript
   const fruits = ['apple', 'banana', 'orange'];
   console.log(fruits[1]); // Output: banana
   ```

2. **Array Methods**
   - JavaScript provides numerous methods for manipulating arrays, such as `push`, `pop`, `shift`, `unshift`, `map`, `filter`, and `reduce`.
   ```javascript
   fruits.push('grape'); // Adds 'grape' to the end
   console.log(fruits); // Output: ['apple', 'banana', 'orange', 'grape']

   const lengths = fruits.map(fruit => fruit.length);
   console.log(lengths); // Output: [5, 6, 6, 5]
   ```

3. **Sets**
   - A `Set` is a collection of unique values, and can store any data type.
   ```javascript
   const uniqueNumbers = new Set([1, 2, 3, 1, 2, 3]);
   console.log(uniqueNumbers); // Output: Set { 1, 2, 3 }
   ```

4. **Set Methods**
   - Common methods for sets include `add`, `delete`, and `has`.
   ```javascript
   uniqueNumbers.add(4);
   console.log(uniqueNumbers.has(2)); // Output: true
   uniqueNumbers.delete(3);
   console.log(uniqueNumbers); // Output: Set { 1, 2, 4 }
   ```

5. **Maps**
   - A `Map` holds key-value pairs where keys can be of any type.
   ```javascript
   const scores = new Map();
   scores.set('Alice', 90);
   scores.set('Bob', 85);
   console.log(scores.get('Alice')); // Output: 90
   ```

6. **Map Methods**
   - Maps provide methods like `set`, `get`, `delete`, and `has`.
   ```javascript
   console.log(scores.has('Bob')); // Output: true
   scores.delete('Alice');
   console.log(scores); // Output: Map { 'Bob' => 85 }
   ```

7. **WeakSets**
   - A `WeakSet` is similar to a `Set`, but it only holds weak references to its objects, allowing them to be garbage collected if there are no other references.
   ```javascript
   let obj1 = {};
   let obj2 = {};
   const weakSet = new WeakSet([obj1, obj2]);

   console.log(weakSet.has(obj1)); // Output: true
   obj1 = null; // Now obj1 can be garbage collected
   ```

8. **WeakMaps**
   - A `WeakMap` holds key-value pairs, where keys are objects and can be garbage collected if there are no other references.
   ```javascript
   const weakMap = new WeakMap();
   const obj3 = {};
   weakMap.set(obj3, 'some value');

   console.log(weakMap.get(obj3)); // Output: some value
   obj3 = null; // Now obj3 can be garbage collected
   ```

9. **Common Use Cases**
   - **Arrays**: Used for ordered lists and easy iteration.
   - **Sets**: Useful for ensuring unique values, such as user IDs or tags.
   - **Maps**: Efficient for lookups based on keys, such as caching values or maintaining relationships between data.

10. **Interview Implications**
    - **Array Methods**: Be prepared to discuss the functional programming aspects of array methods.
    - **Sets and Maps**: Understand their differences and when to use one over the other.
    - **Weak Structures**: Explain the advantages of using weak references for memory management.

Let me know if you want to proceed to the next section!


