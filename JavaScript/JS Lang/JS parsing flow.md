
![[JSFlow.png]]

The image you provided showcases how different types of `<script>` tags in HTML are **parsed**, **fetched**, and **executed** by the browser. Here’s a breakdown of what each row means:

### 1. `<script>`
- **Parsing stops** when the browser encounters a script tag. The HTML parser waits for the script to be fetched and executed before continuing.
- **Fetch** happens immediately.
- **Execution** also happens immediately after the script is fetched.
  
### 2. `<script defer>`
- **HTML parsing continues** in parallel with fetching the script. The script is executed only after the entire HTML document has been parsed.
- **Deferred execution** occurs right before the `DOMContentLoaded` event.

### 3. `<script async>`
- **HTML parsing continues** in parallel with fetching the script. However, the script is executed **as soon as it is fetched**, even before HTML parsing finishes. This might cause scripts to run out of order.

### 4. `<script type="module">`
- **HTML parsing continues** while the module is being fetched. Modules are executed once fetched, but the execution is **deferred** until after the document is parsed.
- Modules have import/export capabilities and follow strict mode by default.

### 5. `<script type="module" async>`
- **HTML parsing continues** while fetching the module asynchronously. The execution happens once the module is fetched, similar to the async attribute for normal scripts, allowing non-blocking behavior.

### Summary of Key Differences:
- **Normal `<script>`**: Blocks parsing and waits for execution.
- **`<script defer>`**: Fetches in parallel, executes after parsing.
- **`<script async>`**: Fetches in parallel, executes immediately after being fetched.
- **Modules**: Respect module scoping rules and either defer execution (`defer`) or execute asynchronously (`async`).


Here's a tabular format that summarizes the behavior of different `<script>` types in terms of **HTML parsing**, **fetching**, and **execution**:

| Script Type                | HTML Parsing Behavior          | Fetching Behavior              | Execution Behavior                                    |
|----------------------------|--------------------------------|--------------------------------|------------------------------------------------------|
| `<script>`                 | **Pauses** while script is fetched and executed | Script is **fetched immediately**      | **Immediately** executed after fetch, blocks parsing |
| `<script defer>`           | **Continues** during script fetch | Script is **fetched in parallel**     | **Executed after HTML parsing** completes (before `DOMContentLoaded`) |
| `<script async>`           | **Continues** during script fetch | Script is **fetched in parallel**     | **Executed as soon as fetched**, may execute before parsing finishes |
| `<script type="module">`    | **Continues** during fetch     | Script is **fetched in parallel**     | **Executed after HTML parsing** completes (similar to `defer`) |
| `<script type="module" async>` | **Continues** during fetch     | Script is **fetched in parallel**     | **Executed as soon as fetched**, but does not block parsing |

This table highlights the key differences in how each script type behaves when it comes to **HTML parsing**, **fetching**, and **execution**.






