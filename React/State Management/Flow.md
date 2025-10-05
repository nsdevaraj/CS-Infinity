
## 🧠 **State Management Flow (Under the Hood)**

---

### 1. **UI Triggers an Action**

- A user interacts with the UI (e.g. clicks a button).
    
- This triggers a **dispatch** with an **action** (a plain object describing _what happened_).
    

```js
dispatch({ type: 'INCREMENT' });
```

---

### 2. **Action Goes to the Reducer**

- The Redux **store** receives the action and forwards it to the **reducer(s)**.
    
- A **reducer** is a **pure function** that:
    
    - Takes current `state` and the `action`
        
    - Returns **new state**
        

```js
function counterReducer(state, action) {
  switch(action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 }; // returns new state (immutable)
    default:
      return state;
  }
}
```

---

### 3. **Store Updates the State**

- Redux updates the **store's internal state** with the new state returned by the reducer.
    
- Redux compares the **previous state vs new state** (shallow comparison).
    
- If there's a change, Redux **notifies all subscribed components**.
    

---

### 4. **UI Subscribes via Hooks (or HOCs)**

- In React, components use:
    
    - `useSelector()` to **read** from the store.
        
    - `useDispatch()` to **send** actions to the store.
        
- When state changes, components **re-render automatically** if the part they read from changed.
    

```js
const count = useSelector((state) => state.counter.count);
```

---

### 5. **React Re-Renders the UI**

- If the subscribed value changed:
    
    - React triggers a re-render.
        
    - The new UI reflects the updated state.
        

---

### 📊 Visual Flow:

```
[User Interaction]
        ↓
  dispatch(action)
        ↓
    reducer(state, action)
        ↓
     new state returned
        ↓
   Redux store updates
        ↓
Subscribed components re-render
        ↓
     UI reflects new state
```

---

### ⚙️ Behind the Scenes

- Redux uses a **Pub/Sub (publish-subscribe)** model.
    
- React-Redux uses **context + hooks** (`useSelector`, `useDispatch`) under the hood.
    
- Efficient updates: Only components using affected state **will re-render**.
    

---

### ✅ Key Principles:

- **Immutable updates**: No in-place state mutation.
    
- **Pure reducers**: Always return new state based on input.
    
- **Unidirectional flow**: Action → Reducer → Store → UI
    

---
