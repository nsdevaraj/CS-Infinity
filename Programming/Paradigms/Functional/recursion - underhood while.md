
In most programming languages, **compilers do not automatically transform recursion into while loops**—**unless** it's a **tail recursion** and the compiler or interpreter supports **tail call optimization (TCO)**.

### Here's a crisp breakdown:

- **Normal recursion**:  
    Usually compiled as a series of **function calls** with stack frames → **not converted** to while loops by default.
    
- **Tail recursion**:  
    If the last operation in a function is the recursive call, some languages (like Scheme, and optionally Scala or optimized C compilers) can **optimize** it into a loop to avoid growing the call stack.
    
- **Why not always?**  
    Automatic conversion to loops is complex and not always feasible, especially for **non-tail recursive** functions with nested calls and branching logic.
    

### TL;DR:

✅ Tail recursion → _may_ be converted to a loop (TCO)  
❌ General recursion → stays as function calls, not while loops

Let me know if you want a code example comparing the two!

