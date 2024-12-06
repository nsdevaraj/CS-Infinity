


5. **Async/Await**
   - `async` and `await` are `syntactic sugar built on top of promises, providing a more readable way to handle asynchronous code`
   ```javascript
   async function fetchDataAsync() {
       const data = await fetchDataPromise; // Waits for the promise to resolve
       console.log(data); // Output: Data received
   }

   fetchDataAsync();
   ```


