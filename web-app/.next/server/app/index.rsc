3:"$Sreact.fragment"
4:I[3379,["177","static/chunks/app/layout-1843c2dad8a8caeb.js"],"default"]
5:I[5244,[],""]
6:I[3866,[],""]
8:I[6213,[],"OutletBoundary"]
a:I[6213,[],"MetadataBoundary"]
c:I[6213,[],"ViewportBoundary"]
e:I[4835,[],""]
1:HL["/_next/static/media/a34f9d1faa5f3315-s.p.woff2","font",{"crossOrigin":"","type":"font/woff2"}]
2:HL["/_next/static/css/87b0a9fc77e88b3d.css","style"]
0:{"P":null,"b":"VQtM1mwsxRepQFu19jaIP","p":"","c":["",""],"i":false,"f":[[["",{"children":["__PAGE__",{}]},"$undefined","$undefined",true],["",["$","$3","c",{"children":[[["$","link","0",{"rel":"stylesheet","href":"/_next/static/css/87b0a9fc77e88b3d.css","precedence":"next","crossOrigin":"$undefined","nonce":"$undefined"}]],["$","html",null,{"lang":"en","className":"h-full","children":["$","body",null,{"className":"__className_d65c78 h-full bg-gray-50 dark:bg-gray-900","children":["$","div",null,{"className":"min-h-full","children":[["$","nav",null,{"className":"bg-white dark:bg-gray-800 shadow-sm","children":["$","div",null,{"className":"mx-auto max-w-7xl px-4 sm:px-6 lg:px-8","children":["$","div",null,{"className":"flex h-16 justify-between","children":[["$","div",null,{"className":"flex","children":["$","div",null,{"className":"flex flex-shrink-0 items-center","children":["$","h1",null,{"className":"text-xl font-bold text-gray-900 dark:text-white","children":"CS Infinity"}]}]}],["$","div",null,{"className":"flex items-center","children":["$","$L4",null,{}]}]]}]}]}],["$","$L5",null,{"parallelRouterKey":"children","segmentPath":["children"],"error":"$undefined","errorStyles":"$undefined","errorScripts":"$undefined","template":["$","$L6",null,{}],"templateStyles":"$undefined","templateScripts":"$undefined","notFound":[["$","title",null,{"children":"404: This page could not be found."}],["$","div",null,{"style":{"fontFamily":"system-ui,\"Segoe UI\",Roboto,Helvetica,Arial,sans-serif,\"Apple Color Emoji\",\"Segoe UI Emoji\"","height":"100vh","textAlign":"center","display":"flex","flexDirection":"column","alignItems":"center","justifyContent":"center"},"children":["$","div",null,{"children":[["$","style",null,{"dangerouslySetInnerHTML":{"__html":"body{color:#000;background:#fff;margin:0}.next-error-h1{border-right:1px solid rgba(0,0,0,.3)}@media (prefers-color-scheme:dark){body{color:#fff;background:#000}.next-error-h1{border-right:1px solid rgba(255,255,255,.3)}}"}}],["$","h1",null,{"className":"next-error-h1","style":{"display":"inline-block","margin":"0 20px 0 0","padding":"0 23px 0 0","fontSize":24,"fontWeight":500,"verticalAlign":"top","lineHeight":"49px"},"children":"404"}],["$","div",null,{"style":{"display":"inline-block"},"children":["$","h2",null,{"style":{"fontSize":14,"fontWeight":400,"lineHeight":"49px","margin":0},"children":"This page could not be found."}]}]]}]}]],"notFoundStyles":[]}]]}]}]}]]}],{"children":["__PAGE__",["$","$3","c",{"children":["$L7",null,["$","$L8",null,{"children":"$L9"}]]}],{},null]},null],["$","$3","h",{"children":[null,["$","$3","h7VXuuVu0u14v84p-dAKH",{"children":[["$","$La",null,{"children":"$Lb"}],["$","$Lc",null,{"children":"$Ld"}],["$","meta",null,{"name":"next-size-adjust"}]]}]]}]]],"m":"$undefined","G":["$e","$undefined"],"s":false,"S":true}
f:I[4839,["839","static/chunks/839-f703ec834851f667.js","974","static/chunks/app/page-b31d2b1bb577579f.js"],""]
10:Tade,<p>![[BigOGraph.png]]</p>
<p>Big O :</p>
<p>https://www.bigocheatsheet.com/</p>
<p>https://bigocheatsheet.io/</p>
<h3>Understanding Big O Notation</h3>
<p>Big O notation is a mathematical representation that describes the efficiency of an algorithm in terms of time complexity (how fast it runs) and space complexity (how much memory it uses). It provides a way to evaluate how the performance of an algorithm changes as the size of the input, denoted by ( n ), increases.</p>
<h4>Key Points of Big O Notation</h4>
<ol>
<li><strong>Definition</strong>: Big O expresses the upper bound of an algorithm’s running time or space requirement, allowing us to compare efficiencies.</li>
<li><strong>Variables</strong>: The variable ( n ) represents the number of inputs. For example, if you have an array of 5 elements, ( n = 5 ).</li>
<li><strong>Growth Rates</strong>: Algorithms with lower growth rates (e.g., ( O(1) ), ( O(\log n) )) are generally more efficient than those with higher growth rates (e.g., ( O(n) ), ( O(n^2) )).</li>
</ol>
<h4>Common Big O Functions (Best to Worst)</h4>
<ul>
<li>( O(1) ): Constant time</li>
<li>( O(\log n) ): Logarithmic time</li>
<li>( O(n) ): Linear time</li>
<li>( O(n \log n) ): Linearithmic time</li>
<li>( O(n^2) ): Quadratic time</li>
<li>( O(2^n) ): Exponential time</li>
<li>( O(n!) ): Factorial time</li>
</ul>
<h3>Example: Comparing Algorithms</h3>
<p>Let’s illustrate why Big O notation is important with an example involving two algorithms:</p>
<ul>
<li><strong>Algorithm A</strong>: ( O(\log n) )</li>
<li><strong>Algorithm B</strong>: ( O(n) )</li>
</ul>
<h4>Scenario 1: Analyzing 10 Elements</h4>
<p>For ( n = 10 ):</p>
<ul>
<li>( O(\log(10)) ) ≈ 3.3 milliseconds</li>
<li>( O(10) ) = 10 milliseconds</li>
</ul>
<p>With 10 elements, the difference in speed is noticeable but might not matter significantly in practice.</p>
<h4>Scenario 2: Analyzing 10 Million Elements</h4>
<p>Now consider ( n = 10,000,000 ):</p>
<ul>
<li>( O(\log(10,000,000)) ) ≈ 23.3 milliseconds</li>
<li>( O(10,000,000) ) = 10,000,000 milliseconds (or about 2 hours and 47 minutes)</li>
</ul>
<p>In this scenario, the performance gap becomes critical. A delay of 2 hours for a search engine would be unacceptable.</p>
<h3>Conclusion</h3>
<p>Understanding Big O notation helps you evaluate algorithms' performance and make informed decisions when selecting the right algorithm for your project. As seen, even a small difference in complexity can lead to vastly different performance outcomes with larger datasets.</p>
<p>If you're interested in diving deeper, consider exploring resources that detail the complexities of various data structures and algorithms. This foundational knowledge is invaluable for software engineering and algorithm design!</p>
11:Tdbe,<h2>Greedy Algorithms: An Overview</h2>
<p>Greedy algorithms are designed to make the most favorable choice at each step in order to find a solution. This approach can be efficient for specific problems but may not always yield the optimal solution. Let’s explore when to use greedy algorithms, along with an example of their strengths and weaknesses.</p>
<h4>Key Characteristics of Greedy Algorithms</h4>
<ol>
<li><strong>Local Optimality</strong>: At each decision point, the algorithm makes the best local choice without considering the broader consequences.</li>
<li><strong>Efficiency</strong>: Greedy algorithms typically have lower time complexity since they don’t evaluate every possible outcome.</li>
<li><strong>Not Always Optimal</strong>: While they can be efficient, greedy algorithms do not guarantee an optimal solution for all problems.</li>
</ol>
<h3>When Not to Use Greedy Algorithms</h3>
<p>Greedy algorithms are ineffective in scenarios where making a locally optimal choice does not lead to a globally optimal solution. For example, consider a pathfinding problem where each decision incurs a cost:</p>
<ul>
<li><strong>Example</strong>: Imagine you have a set of paths with different costs:
<ul>
<li>Path A: $7</li>
<li>Path B: $8</li>
<li>Path C: $9</li>
<li>Path D: $10</li>
</ul>
</li>
</ul>
<p>If you use a greedy algorithm, it might choose Path A ($7) first, then Path C ($9), resulting in a total cost of $16. However, the optimal path might only cost $3 by taking a different route entirely.</p>
<h3>When to Use Greedy Algorithms</h3>
<p>Greedy algorithms are suitable for problems where:</p>
<ul>
<li>An approximate solution is acceptable.</li>
<li>The problem exhibits optimal substructure, meaning the optimal solution to a problem can be constructed from optimal solutions of its subproblems.</li>
</ul>
<h4>Famous Example: The Traveling Salesman Problem (TSP)</h4>
<p>The TSP asks for the shortest possible route that visits each city exactly once and returns to the starting point. Given the factorial growth of potential routes, the total number of paths becomes infeasible to calculate for larger datasets:</p>
<ul>
<li>For 5 cities: ( (n-1)!/2 = 12 ) routes.</li>
<li>For 10 cities: ( 181,440 ) routes.</li>
<li>For 50 cities: ( 304140932017133780436126081660647688443776415689605120000000000 ) routes.</li>
</ul>
<p>Given such exponential growth, finding an optimal solution using brute force is impractical. Here’s where a greedy approach can be beneficial:</p>
<ol>
<li><strong>Starting Point</strong>: Choose an arbitrary starting city.</li>
<li><strong>Next City</strong>: Always select the nearest unvisited city.</li>
<li><strong>Completion</strong>: Repeat until all cities are visited, then return to the starting city.</li>
</ol>
<p>While this approach doesn’t guarantee the optimal route, it provides a practical solution that is significantly faster than evaluating all possible paths.</p>
<h3>Summary</h3>
<p>Greedy algorithms excel in scenarios where:</p>
<ul>
<li>An exact optimal solution is infeasible due to the problem’s complexity.</li>
<li>A reasonable approximation is acceptable.</li>
</ul>
<p>They are best applied to problems that allow for a step-by-step decision-making process leading to a satisfactory solution. Understanding when and how to implement these algorithms can enhance problem-solving efficiency in various computational tasks. If you have more questions or want further clarification on specific examples, feel free to ask!</p>
12:T24e8,<h2>Binary Search</h2>
<p>Binary search is an efficient algorithm for finding the position of a specific element in a <strong>sorted</strong> list. Let’s illustrate this with a guessing game example:</p>
<p>Imagine your friend chooses a number between <strong>1 and 100</strong>, and your task is to guess it.</p>
<h4>Linear Search</h4>
<p>One approach is <strong>linear search</strong>, where you start at <strong>1</strong> and guess each number in sequence. If the correct number is <strong>100</strong>, you’d need <strong>100 guesses</strong>—which is inefficient, especially with larger ranges (like <strong>1 to 10,000</strong>). This method has a time complexity of <strong>O(n)</strong>, meaning the number of guesses grows linearly with the size of the list.</p>
<h4>Binary Search</h4>
<p>Now, let’s consider <strong>binary search</strong>. Instead of starting at <strong>1</strong>, you begin by guessing the <strong>middle</strong> of the range, which is <strong>50</strong>. Your friend then tells you if the number is higher or lower. Based on that feedback, you can eliminate half of the remaining possibilities with each guess.</p>
<p>For instance:</p>
<ol>
<li>Guess <strong>50</strong>: If the number is higher, you now consider <strong>51 to 100</strong>.</li>
<li>Guess the new middle (let's say <strong>75</strong>): Continue narrowing down the range based on feedback.</li>
</ol>
<p>This method effectively halves the number of options with each guess, leading to a time complexity of <strong>O(log n)</strong>.</p>
<pre><code class="language-pseudo">FUNCTION binarySearch(array, target):
    low = 0
    high = length(array) - 1

    WHILE low &#x3C;= high:
        mid = (low + high) // 2  // Integer division

        IF array[mid] == target:
            RETURN mid  // Target found
        ELSE IF array[mid] &#x3C; target:
            low = mid + 1  // Search in the right half
        ELSE:
            high = mid - 1  // Search in the left half

    RETURN -1  // Target not found

</code></pre>
<h4>Worst-Case Comparison</h4>
<p>To see how efficient this is, let’s look at the worst-case scenario:</p>
<ul>
<li>For linear search in the range <strong>1 to 10,000</strong>, you might need <strong>10,000 guesses</strong>.</li>
<li>For binary search, using <strong>O(log n)</strong>:
<ul>
<li>Calculate ( \log_2(10,000) ), which is approximately <strong>13.3</strong>. Thus, you’d need <strong>14 guesses</strong> in the worst case.</li>
</ul>
</li>
</ul>
<h4>Conclusion</h4>
<p>Binary search is a powerful tool, particularly when dealing with sorted lists. Its efficiency makes it significantly faster than linear search for large datasets. Just remember: binary search only works on sorted data. If you find yourself needing to search through a sorted list, binary search is an excellent approach to consider.</p>
<h2>Depth-First Search (DFS)</h2>
<p>Depth-First Search (DFS) is a traversal algorithm used to explore nodes and edges in a graph or tree structure. The key idea behind DFS is to start at the <strong>root node</strong> and explore as far down one branch as possible before backtracking. This approach effectively utilizes a technique called <strong>backtracking</strong>.</p>
<h4>How DFS Works</h4>
<ol>
<li>
<p><strong>Initialization</strong>: Before starting DFS, create a <strong>visited array</strong> to keep track of nodes you’ve already explored.</p>
</li>
<li>
<p><strong>Traversal</strong>:</p>
<ul>
<li>Begin at the <strong>root node</strong> and add it to the visited array.</li>
<li>Move to the first child node and add it to the visited array.</li>
<li>Continue down this branch, visiting nodes and adding them to the visited array until you reach a node with no unvisited children.</li>
</ul>
</li>
<li>
<p><strong>Backtracking</strong>:</p>
<ul>
<li>Once you hit a dead end, backtrack to the previous node and check for any unvisited children.</li>
<li>If there are unvisited nodes, proceed down that branch and repeat the process.</li>
<li>If not, backtrack further up until all nodes have been visited.</li>
</ul>
</li>
</ol>
<p>This process continues until the entire graph has been explored.</p>
<h4>Visual Example</h4>
<p>Imagine navigating a maze: you start at the entrance and explore each path to its end. If you encounter a wall, you backtrack to the last junction and try another path. This method of exploration allows you to efficiently search through complex structures.</p>
<p>Recursive DFS Pseudocode</p>
<pre><code class="language-pseudo">FUNCTION DFS(node, visited):
    IF node IS NULL:
        RETURN

    // Mark the node as visited
    visited.add(node)

    // Process the current node (e.g., print it)
    PRINT(node)

    // Recur for each unvisited adjacent node
    FOR each neighbor in node.adjacent:
        IF neighbor NOT IN visited:
            DFS(neighbor, visited)

</code></pre>
<p>Iterative DFS Pseudocode</p>
<pre><code class="language-pseudo">FUNCTION iterativeDFS(root):
    visited = empty set
    stack = empty stack

    stack.push(root)

    WHILE stack is not empty:
        node = stack.pop()

        IF node NOT IN visited:
            visited.add(node)

            // Process the current node (e.g., print it)
            PRINT(node)

            // Add all unvisited neighbors to the stack
            FOR each neighbor in node.adjacent:
                IF neighbor NOT IN visited:
                    stack.push(neighbor)

</code></pre>
<h4>Time Complexity</h4>
<p>The time complexity of DFS is expressed as <strong>O(V + E)</strong>, where:</p>
<ul>
<li><strong>V</strong> is the total number of <strong>vertices</strong> (or nodes).</li>
<li><strong>E</strong> is the total number of <strong>edges</strong> (or branches).</li>
</ul>
<p>This complexity arises because, in the worst case, you may need to visit every node and edge.</p>
<h4>Real-World Applications</h4>
<p>DFS is particularly useful in scenarios like:</p>
<ul>
<li><strong>Maze solving</strong>: Finding a path through a maze by exploring all possible routes.</li>
<li><strong>Puzzle solving</strong>: Games like Sudoku, where exploring different configurations is necessary.</li>
<li><strong>Graph algorithms</strong>: Such as topological sorting and finding connected components.</li>
</ul>
<p>Now that we’ve covered DFS, let’s move on to its counterpart: <strong>Breadth-First Search (BFS)</strong>.</p>
<h2>Breadth-First Search (BFS)</h2>
<p>Breadth-First Search (BFS) is an algorithm used to explore nodes and edges in a graph or tree structure. Unlike Depth-First Search (DFS), BFS explores all the nodes at the current level before moving on to the next level. This level-by-level approach makes it intuitive and easy to understand.</p>
<h4>How BFS Works</h4>
<ol>
<li>
<p><strong>Initialization</strong>:</p>
<ul>
<li>Create a <strong>visited array</strong> to track which nodes have been explored.</li>
<li>Create a <strong>queue</strong> to hold the nodes that need to be explored.</li>
</ul>
</li>
<li>
<p><strong>Traversal</strong>:</p>
<ul>
<li>Start at the <strong>root node</strong>, mark it as visited, and add it to the queue.</li>
<li>While the queue is not empty:
<ul>
<li>Dequeue the front node.</li>
<li>Process that node (e.g., print it or store it).</li>
<li>Enqueue all its unvisited neighbors, marking them as visited as you go.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><strong>Level-by-Level Exploration</strong>:</p>
<ul>
<li>Continue this process until all reachable nodes have been visited, ensuring that you explore each level fully before proceeding to the next.</li>
</ul>
</li>
</ol>
<h4>Visual Example</h4>
<p>Think of BFS like exploring a building floor by floor. You check every room on the first floor before moving to the second floor. This systematic approach ensures that you see all possible connections at each level.</p>
<h4>Real-World Applications</h4>
<p>BFS is commonly used in scenarios such as:</p>
<ul>
<li><strong>Chess algorithms</strong>: To evaluate possible moves by exploring all possible next moves and their subsequent options.</li>
<li><strong>Social networking</strong>: Finding the shortest path between users.</li>
<li><strong>Web crawling</strong>: To explore web pages level by level.</li>
</ul>
<h4>Time Complexity</h4>
<p>The time complexity of BFS is also <strong>O(V + E)</strong>, where:</p>
<ul>
<li><strong>V</strong> is the total number of vertices (nodes).</li>
<li><strong>E</strong> is the total number of edges (connections).</li>
</ul>
<h3>Pseudocode for Breadth-First Search</h3>
<pre><code class="language-plaintext">FUNCTION BFS(root):
    visited = empty set
    queue = empty queue

    // Start with the root node
    visited.add(root)
    queue.enqueue(root)

    WHILE queue is not empty:
        node = queue.dequeue()

        // Process the current node (e.g., print it)
        PRINT(node)

        // Enqueue all unvisited neighbors
        FOR each neighbor in node.adjacent:
            IF neighbor NOT IN visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
</code></pre>
<h3>Summary</h3>
<ul>
<li><strong>BFS</strong> efficiently explores nodes level by level, ensuring that all neighbors are examined before moving deeper.</li>
<li>The algorithm is particularly useful for problems requiring the shortest path or level-based exploration.</li>
</ul>
<p>If you have any further questions or need more examples, feel free to ask!</p>
13:T3266,<h2>Insertion Sort Explained</h2>
<p><strong>Insertion Sort</strong> is a straightforward and intuitive sorting algorithm. It builds a sorted array (or list) one element at a time by repeatedly taking an unsorted element and inserting it into its correct position within the sorted portion of the array.</p>
<h4>How Insertion Sort Works</h4>
<ol>
<li>
<p><strong>Start with the first element</strong>: Consider the first element as a sorted portion.</p>
</li>
<li>
<p><strong>Compare and Insert</strong>:</p>
<ul>
<li>Take the next element in the unsorted portion.</li>
<li>Compare it with elements in the sorted portion, moving from right to left.</li>
<li>If the current element is smaller than the compared element, shift the compared element to the right.</li>
<li>Insert the current element in its correct position once you find the right spot.</li>
</ul>
</li>
<li>
<p><strong>Repeat</strong>: Continue this process for all elements in the list until the entire array is sorted.</p>
</li>
</ol>
<h4>Example</h4>
<p>Let’s say we have the following list: <code>[5, 2, 9, 1, 5, 6]</code>.</p>
<ul>
<li>Start with the first element (5). It’s already sorted.</li>
<li>Compare 2 with 5; since 2 &#x3C; 5, swap them. The list is now <code>[2, 5, 9, 1, 5, 6]</code>.</li>
<li>Compare 9 with 5; since 9 > 5, leave it.</li>
<li>Compare 1 with 9; since 1 &#x3C; 9, shift 9 to the right. Now compare with 5; shift 5 to the right. Insert 1. The list is now <code>[1, 2, 5, 9, 5, 6]</code>.</li>
<li>Continue this process until the list is fully sorted.</li>
</ul>
<h4>Time Complexity</h4>
<ul>
<li><strong>Best Case</strong>: <strong>O(n)</strong>, which occurs when the list is already sorted. The algorithm makes a single pass through the list.</li>
<li><strong>Worst Case</strong>: <strong>O(n²)</strong>, which occurs when the list is in reverse order. Each element has to be compared with every other element.</li>
<li><strong>Average Case</strong>: <strong>O(n²)</strong>, typical for randomly ordered lists.</li>
</ul>
<h4>When to Use Insertion Sort</h4>
<ul>
<li><strong>Mostly Sorted Lists</strong>: Insertion sort performs well when the list is nearly sorted, as it can achieve linear time complexity.</li>
<li><strong>Small Lists</strong>: Due to its simplicity and low overhead, it’s efficient for small datasets.</li>
<li><strong>Stability</strong>: Insertion sort is a stable sort, meaning that it preserves the relative order of equal elements.</li>
</ul>
<h3>Pseudocode for Insertion Sort</h3>
<pre><code class="language-plaintext">FUNCTION insertionSort(array):
    FOR i FROM 1 TO length(array) - 1:
        key = array[i]
        j = i - 1

        // Move elements of array[0..i-1] that are greater than key
        WHILE j >= 0 AND array[j] > key:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key  // Insert key into its correct position
</code></pre>
<h3>Summary</h3>
<p>Insertion Sort is an effective algorithm for small or nearly sorted datasets. While it may not be suitable for large lists due to its O(n²) worst-case runtime, it is easy to implement and understand, making it a good choice for certain scenarios. If you have more questions or need further examples, feel free to ask!</p>
<h3>Insertion Sort vs. Merge Sort</h3>
<h4>Insertion Sort Overview</h4>
<p><strong>Insertion Sort</strong> is a simple sorting algorithm that builds a sorted array one element at a time. Here’s a quick recap of its performance:</p>
<ul>
<li><strong>Best Case</strong>: <strong>O(n)</strong> when the array is already sorted, as it only requires a single pass through the elements.</li>
<li><strong>Worst Case</strong>: <strong>O(n²)</strong> when the array is in reverse order, necessitating comparisons with every other element.</li>
<li><strong>Use Cases</strong>: Best for small or nearly sorted lists due to its simplicity and efficiency in those scenarios.</li>
</ul>
<h2>Merge Sort Overview</h2>
<p><strong>Merge Sort</strong> is a more advanced sorting algorithm that uses the <strong>divide-and-conquer</strong> strategy. It efficiently handles larger and more complex datasets. Here’s how it works:</p>
<ol>
<li>
<p><strong>Divide</strong>: Split the array into two halves. This process continues recursively until each subarray contains a single element.</p>
</li>
<li>
<p><strong>Conquer</strong>: Merge the sorted subarrays back together. During this process, compare the elements from each half and sort them as you combine them.</p>
</li>
<li>
<p><strong>Combine</strong>: The merging process continues until the entire array is reconstructed in sorted order.</p>
</li>
</ol>
<h4>Visualization of Merge Sort</h4>
<p>Imagine you have an array <code>[38, 27, 43, 3, 9, 82, 10]</code>:</p>
<ol>
<li>
<p><strong>Splitting</strong>:</p>
<ul>
<li>First, split into <code>[38, 27, 43]</code> and <code>[3, 9, 82, 10]</code>.</li>
<li>Split further until you reach single elements: <code>[38]</code>, <code>[27]</code>, <code>[43]</code>, <code>[3]</code>, <code>[9]</code>, <code>[82]</code>, <code>[10]</code>.</li>
</ul>
</li>
<li>
<p><strong>Merging</strong>:</p>
<ul>
<li>Merge pairs: <code>[27, 38]</code>, <code>[3, 9, 10, 82]</code>, <code>[43]</code>.</li>
<li>Continue merging while sorting: <code>[27, 38, 43]</code> and <code>[3, 9, 10, 82]</code>.</li>
<li>Finally, combine to get the fully sorted array: <code>[3, 9, 10, 27, 38, 43, 82]</code>.</li>
</ul>
</li>
</ol>
<h4>Time Complexity</h4>
<ul>
<li><strong>Merge Sort</strong>: Both best and worst-case time complexity is <strong>O(n log n)</strong>. This efficiency makes it suitable for large datasets.</li>
<li><strong>Insertion Sort vs. Merge Sort</strong>:
<ul>
<li>For small or mostly sorted lists, Insertion Sort is more efficient (O(n)).</li>
<li>For larger, unsorted lists, Merge Sort is preferable due to its O(n log n) runtime, which remains consistent regardless of initial order.</li>
</ul>
</li>
</ul>
<h3>Summary</h3>
<ul>
<li><strong>Insertion Sort</strong>: Effective for small or nearly sorted lists with a best-case of O(n) but poor performance on larger datasets (O(n²)).</li>
<li><strong>Merge Sort</strong>: Ideal for larger or more unordered lists, consistently performing at O(n log n), leveraging the power of recursion and divide-and-conquer.</li>
</ul>
<p>Understanding these algorithms allows you to choose the right one based on the size and initial order of the dataset you're working with. If you have any further questions or need additional examples, feel free to ask!</p>
<p>Here’s the pseudocode for <strong>Merge Sort</strong>:</p>
<h3>Merge Sort Pseudocode</h3>
<pre><code class="language-plaintext">FUNCTION mergeSort(array):
    IF length(array) &#x3C;= 1:
        RETURN array  // Base case: an array of zero or one element is already sorted

    // Divide the array into two halves
    mid = length(array) // 2
    left = mergeSort(array[0:mid])    // Recursively sort the left half
    right = mergeSort(array[mid:end])  // Recursively sort the right half

    // Merge the sorted halves
    RETURN merge(left, right)

FUNCTION merge(left, right):
    result = empty array
    i = 0  // Pointer for left array
    j = 0  // Pointer for right array

    // Merge elements from both arrays in sorted order
    WHILE i &#x3C; length(left) AND j &#x3C; length(right):
        IF left[i] &#x3C;= right[j]:
            result.append(left[i])
            i = i + 1
        ELSE:
            result.append(right[j])
            j = j + 1

    // Append any remaining elements from left array
    WHILE i &#x3C; length(left):
        result.append(left[i])
        i = i + 1

    // Append any remaining elements from right array
    WHILE j &#x3C; length(right):
        result.append(right[j])
        j = j + 1

    RETURN result  // Return the merged and sorted array
</code></pre>
<h3>Explanation</h3>
<ol>
<li><strong>Base Case</strong>: If the array has one or no elements, it’s already sorted.</li>
<li><strong>Divide</strong>: The array is split into two halves.</li>
<li><strong>Conquer</strong>: Each half is sorted recursively using <code>mergeSort</code>.</li>
<li><strong>Merge</strong>: The sorted halves are combined into a single sorted array using the <code>merge</code> function.</li>
</ol>
<p>This pseudocode clearly outlines how Merge Sort operates, utilizing recursion and the merging process to achieve efficient sorting. If you have more questions or need further details, just let me know!</p>
<h2>Quick Sort Overview</h2>
<p><strong>Quick Sort</strong> is a powerful and efficient sorting algorithm that follows the <strong>divide-and-conquer</strong> strategy. It's known for its speed in practical scenarios, making it one of the most commonly used sorting algorithms, despite its potential for poor performance in specific cases.</p>
<h4>How Quick Sort Works</h4>
<ol>
<li>
<p><strong>Choose a Pivot</strong>:</p>
<ul>
<li>Select a pivot element from the array. The ideal choice is a value close to the median, as this helps to balance the partitions.</li>
</ul>
</li>
<li>
<p><strong>Partitioning</strong>:</p>
<ul>
<li>Rearrange the array so that elements less than the pivot come before it and elements greater than the pivot come after it. This process is called partitioning.</li>
<li>The pivot is then placed in its correct position in the sorted array.</li>
</ul>
</li>
<li>
<p><strong>Recursion</strong>:</p>
<ul>
<li>Recursively apply the above steps to the sub-arrays formed by partitioning (the left sub-array and the right sub-array).</li>
</ul>
</li>
<li>
<p><strong>Base Case</strong>:</p>
<ul>
<li>The recursion ends when the sub-arrays have one or no elements, as they are already sorted.</li>
</ul>
</li>
</ol>
<h4>Visualization Example</h4>
<ol>
<li>Start with the array: <code>[10, 7, 8, 9, 1, 5]</code>.</li>
<li>Select a pivot (e.g., <code>8</code>). Move it to the end of the list: <code>[10, 7, 9, 1, 5, 8]</code>.</li>
<li>Set pointers at the leftmost and rightmost ends:
<ul>
<li>Compare elements and swap as needed to ensure all elements left of the pivot are less than it, and all elements right are greater.</li>
</ul>
</li>
<li>Once the pointers cross, place the pivot in its correct position. The array might look like: <code>[7, 5, 1, 8, 10, 9]</code>.</li>
<li>Recursively apply the same steps to the sub-arrays <code>[7, 5, 1]</code> and <code>[10, 9]</code>.</li>
</ol>
<h4>Time Complexity</h4>
<ul>
<li><strong>Best Case</strong>: <strong>O(n log n)</strong> when the pivot divides the array into two equal halves.</li>
<li><strong>Average Case</strong>: <strong>O(n log n)</strong>; this is where Quick Sort shines.</li>
<li><strong>Worst Case</strong>: <strong>O(n²)</strong> occurs when the smallest or largest element is consistently chosen as the pivot (e.g., already sorted arrays).</li>
</ul>
<h4>Space Complexity</h4>
<ul>
<li><strong>Quick Sort</strong>: <strong>O(log n)</strong> due to the recursive stack space.</li>
<li><strong>Merge Sort</strong>: <strong>O(n)</strong> due to the need for temporary arrays during the merge process.</li>
</ul>
<h3>Why Use Quick Sort?</h3>
<ul>
<li><strong>Speed</strong>: On average, Quick Sort tends to be faster than both Insertion Sort and Merge Sort due to its efficient in-place partitioning.</li>
<li><strong>Memory Efficiency</strong>: Uses less memory than Merge Sort.</li>
<li><strong>Performance Tuning</strong>: With careful implementation (like choosing good pivots), it can avoid worst-case scenarios.</li>
</ul>
<h3>Pseudocode for Quick Sort</h3>
<pre><code class="language-plaintext">FUNCTION quickSort(array, low, high):
    IF low &#x3C; high:
        // Partition the array and get the pivot index
        pivotIndex = partition(array, low, high)

        // Recursively sort elements before and after the partition
        quickSort(array, low, pivotIndex - 1)
        quickSort(array, pivotIndex + 1, high)

FUNCTION partition(array, low, high):
    pivot = array[high]  // Choose the last element as the pivot
    i = low - 1          // Pointer for the smaller element

    FOR j FROM low TO high - 1:
        IF array[j] &#x3C;= pivot:
            i = i + 1
            swap(array[i], array[j])  // Swap if element is smaller than the pivot

    swap(array[i + 1], array[high])  // Swap the pivot into the correct position
    RETURN i + 1  // Return the partition index
</code></pre>
<h3>Summary</h3>
<ul>
<li><strong>Quick Sort</strong> is an efficient, recursive, divide-and-conquer algorithm that, when implemented correctly, is typically faster than other sorting algorithms on average.</li>
<li>Understanding its mechanics and proper implementation is crucial, as even minor mistakes can lead to inefficiencies.</li>
<li>Its low space complexity makes it a favorable choice for large datasets.</li>
</ul>
<p>If you have more questions or need additional explanations, feel free to ask!</p>
14:Tfa6,<p>Object-Relational Mappers (ORMs) are tools that help developers interact with databases using object-oriented programming languages. Here’s a list of some of the most popular ORMs in various programming languages:</p>
<h3>Python</h3>
<ol>
<li>
<p><strong>SQLAlchemy</strong></p>
<ul>
<li>A powerful and flexible ORM that provides a full suite of well-known enterprise-level persistence patterns. It supports both high-level ORM capabilities and low-level database interaction.</li>
</ul>
</li>
<li>
<p><strong>Django ORM</strong></p>
<ul>
<li>Built into the Django web framework, it allows developers to interact with databases using Python objects and provides a powerful query language.</li>
</ul>
</li>
<li>
<p><strong>Peewee</strong></p>
<ul>
<li>A small and expressive ORM that is easy to use and well-suited for small projects or applications that don’t need the full complexity of SQLAlchemy.</li>
</ul>
</li>
</ol>
<h3>JavaScript</h3>
<ol>
<li>
<p><strong>Sequelize</strong></p>
<ul>
<li>A promise-based ORM for Node.js that supports multiple SQL dialects like PostgreSQL, MySQL, and SQLite. It features migrations, model validation, and associations.</li>
</ul>
</li>
<li>
<p><strong>TypeORM</strong></p>
<ul>
<li>An ORM for TypeScript and JavaScript (ES7, ES6, ES5) that supports Active Record and Data Mapper patterns. It works with various databases and is great for TypeScript projects.</li>
</ul>
</li>
<li>
<p><strong>Mongoose</strong></p>
<ul>
<li>An ODM (Object Data Modeling) library for MongoDB and Node.js, providing a schema-based solution to model application data.</li>
</ul>
</li>
</ol>
<h3>Ruby</h3>
<ol>
<li>
<p><strong>Active Record</strong></p>
<ul>
<li>The default ORM for Ruby on Rails, it provides a straightforward way to interact with databases and supports features like migrations, validations, and associations.</li>
</ul>
</li>
<li>
<p><strong>Sequel</strong></p>
<ul>
<li>A simple, flexible ORM for Ruby that supports multiple databases and offers a powerful query DSL.</li>
</ul>
</li>
</ol>
<h3>PHP</h3>
<ol>
<li>
<p><strong>Eloquent</strong></p>
<ul>
<li>The ORM included with the Laravel framework. It provides an elegant and expressive syntax for working with databases and includes support for relationships, eager loading, and more.</li>
</ul>
</li>
<li>
<p><strong>Doctrine</strong></p>
<ul>
<li>A powerful ORM for PHP that supports complex data models and is used widely in Symfony applications.</li>
</ul>
</li>
</ol>
<h3>C#</h3>
<ol>
<li>
<p><strong>Entity Framework</strong></p>
<ul>
<li>A popular ORM for .NET applications that supports both Code First and Database First approaches. It provides a rich set of features for querying and updating databases.</li>
</ul>
</li>
<li>
<p><strong>Dapper</strong></p>
<ul>
<li>A lightweight ORM for .NET that focuses on performance. It’s not as feature-rich as Entity Framework but is very fast and suitable for simple scenarios.</li>
</ul>
</li>
</ol>
<h3>Go</h3>
<ol>
<li>
<p><strong>GORM</strong></p>
<ul>
<li>An ORM for Go that provides an easy way to interact with databases and supports associations, hooks, and migrations.</li>
</ul>
</li>
<li>
<p><strong>Ent</strong></p>
<ul>
<li>An ORM for Go that focuses on code generation and type safety, making it easy to work with complex data models.</li>
</ul>
</li>
</ol>
<h3>Conclusion</h3>
<p>When choosing an ORM, consider the following:</p>
<ul>
<li><strong>Project Requirements</strong>: Some ORMs are better suited for complex applications, while others are lightweight for simpler projects.</li>
<li><strong>Database Support</strong>: Ensure the ORM supports the database system you plan to use.</li>
<li><strong>Community and Documentation</strong>: A strong community and good documentation can make a big difference in development speed and troubleshooting.</li>
</ul>
<p>Ultimately, the best ORM for your project will depend on your specific needs, the programming language you're using, and the overall architecture of your application.</p>
15:Te55,<p>Terminal linux commands:
To create a folder</p>
<pre><code class="language-bash">mkdir folder_name  
</code></pre>
<p>If you want to create a folder in a specific directory, navigate to that directory using the <code>cd</code> command first:</p>
<pre><code class="language-bash">cd /path/to/your/directory  
mkdir MyFolder  
</code></pre>
<p>You can also create nested folders by using the <code>-p</code> option:</p>
<pre><code class="language-bash">mkdir -p parent_folder/child_folder  
</code></pre>
<p>This will create both the parent and child folders if they do not already exist.</p>
<h3>1. Using <code>touch</code></h3>
<p>The <code>touch</code> command is the simplest way to create an empty file:</p>
<pre><code class="language-bash">touch filename.txt  
</code></pre>
<p>This creates an empty file named <code>filename.txt</code>.</p>
<h3>2. Using <code>echo</code></h3>
<p>You can create a file and add some text to it with the <code>echo</code> command:</p>
<pre><code class="language-bash">echo "Hello, World!" > filename.txt  
</code></pre>
<p>This creates a file named <code>filename.txt</code> containing the text "Hello, World!".</p>
<h3>3. Using <code>cat</code></h3>
<p>You can also create a file using the <code>cat</code> command:</p>
<pre><code class="language-bash">cat > filename.txt  
</code></pre>
<p>After running this command, you can type your text. Press <code>Ctrl + D</code> to save and exit.</p>
<h3>4. Using <code>nano</code> or another text editor</h3>
<p>You can create and edit a file using a text editor like <code>nano</code>:</p>
<pre><code class="language-bash">nano filename.txt  
</code></pre>
<p>This opens the <code>nano</code> editor. After typing your content, press <code>Ctrl + X</code>, then <code>Y</code>, and <code>Enter</code> to save.</p>
<h3>5. Using <code>printf</code></h3>
<p>For more complex file creation with formatting, you can use <code>printf</code>:</p>
<pre><code class="language-bash">printf "Line 1\nLine 2\n" > filename.txt  
</code></pre>
<h3>1. Delete a File</h3>
<p>To delete a single file, use the <code>rm</code> command:</p>
<pre><code class="language-bash">rm filename.txt  
</code></pre>
<h3>2. Delete a Folder</h3>
<p>To delete an empty folder, use the <code>rmdir</code> command:</p>
<pre><code class="language-bash">rmdir folder_name  
</code></pre>
<h3>3. Delete a Folder with Files Inside</h3>
<p>To delete a folder and all its contents (including files and subfolders), use the <code>rm</code> command with the <code>-r</code> (recursive) option:</p>
<pre><code class="language-bash">rm -r folder_name  
</code></pre>
<h3>4. Force Delete (Optional)</h3>
<p>If you want to delete without being prompted for confirmation, you can add the <code>-f</code> (force) option:</p>
<pre><code class="language-bash">rm -rf folder_name  
</code></pre>
<h3>Important Note</h3>
<p>Be very careful when using the <code>rm -rf</code> command, as it will permanently delete files and folders without any warning. Always double-check the folder or file name before executing the command.</p>
<p>You can run both commands in a single command line using <code>&#x26;&#x26;</code> or <code>&#x26;</code>, depending on your needs.</p>
<h3>Using <code>&#x26;&#x26;</code></h3>
<p>This will run the second command only if the first command succeeds:</p>
<pre><code class="language-bash">tsc runner.ts &#x26;&#x26; bun runner.js
</code></pre>
<h3>Using <code>&#x26;</code></h3>
<p>This will run both commands concurrently, without waiting for the first to finish:</p>
<pre><code class="language-bash">tsc runner.ts &#x26; bun runner.js
</code></pre>
<p>Choose the method that best suits your use case!</p>
7:["$","div",null,{"className":"flex h-full","children":[["$","div",null,{"className":"hidden lg:fixed lg:inset-y-0 lg:flex lg:w-64 lg:flex-col","children":["$","div",null,{"className":"flex grow flex-col gap-y-5 overflow-y-auto border-r border-gray-200 bg-white px-6 pb-4","children":[["$","div",null,{"className":"flex h-16 shrink-0 items-center","children":["$","span",null,{"className":"text-lg font-semibold","children":"Categories"}]}],["$","nav",null,{"className":"flex flex-1 flex-col","children":["$","ul",null,{"role":"list","className":"flex flex-1 flex-col gap-y-7","children":[["$","li","Famous algo",{"children":[["$","div",null,{"className":"text-xs font-semibold leading-6 text-gray-400","children":"Famous algo"}],["$","ul",null,{"role":"list","className":"-mx-2 mt-2 space-y-1","children":[["$","li","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/0 Outline.md",{"children":["$","$Lf",null,{"href":"#/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/0 Outline.md","className":"text-gray-700 hover:text-indigo-600 hover:bg-gray-50 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold","children":"0 Outline"}]}],["$","li","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Big O.md",{"children":["$","$Lf",null,{"href":"#/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Big O.md","className":"text-gray-700 hover:text-indigo-600 hover:bg-gray-50 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold","children":"Big O"}]}],["$","li","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Greedy.md",{"children":["$","$Lf",null,{"href":"#/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Greedy.md","className":"text-gray-700 hover:text-indigo-600 hover:bg-gray-50 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold","children":"Greedy"}]}],["$","li","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Search.md",{"children":["$","$Lf",null,{"href":"#/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Search.md","className":"text-gray-700 hover:text-indigo-600 hover:bg-gray-50 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold","children":"Search"}]}],["$","li","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Sort.md",{"children":["$","$Lf",null,{"href":"#/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Sort.md","className":"text-gray-700 hover:text-indigo-600 hover:bg-gray-50 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold","children":"Sort"}]}]]}]]}],["$","li","sorting",{"children":[["$","div",null,{"className":"text-xs font-semibold leading-6 text-gray-400","children":"sorting"}],["$","ul",null,{"role":"list","className":"-mx-2 mt-2 space-y-1","children":[["$","li","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/sorting/Sort.md",{"children":["$","$Lf",null,{"href":"#/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/sorting/Sort.md","className":"text-gray-700 hover:text-indigo-600 hover:bg-gray-50 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold","children":"Sort"}]}]]}]]}],["$","li","ORMs",{"children":[["$","div",null,{"className":"text-xs font-semibold leading-6 text-gray-400","children":"ORMs"}],["$","ul",null,{"role":"list","className":"-mx-2 mt-2 space-y-1","children":[["$","li","/Users/jeevas/Documents/Jeeva/CS Infinity/CS/Backend/DB/ORMs/Stacks.md",{"children":["$","$Lf",null,{"href":"#/Users/jeevas/Documents/Jeeva/CS Infinity/CS/Backend/DB/ORMs/Stacks.md","className":"text-gray-700 hover:text-indigo-600 hover:bg-gray-50 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold","children":"Stacks"}]}]]}]]}],["$","li","CS",{"children":[["$","div",null,{"className":"text-xs font-semibold leading-6 text-gray-400","children":"CS"}],["$","ul",null,{"role":"list","className":"-mx-2 mt-2 space-y-1","children":[["$","li","/Users/jeevas/Documents/Jeeva/CS Infinity/CS/CMD commands.md",{"children":["$","$Lf",null,{"href":"#/Users/jeevas/Documents/Jeeva/CS Infinity/CS/CMD commands.md","className":"text-gray-700 hover:text-indigo-600 hover:bg-gray-50 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold","children":"CMD commands"}]}],["$","li","/Users/jeevas/Documents/Jeeva/CS Infinity/CS/CS doubt.md",{"children":["$","$Lf",null,{"href":"#/Users/jeevas/Documents/Jeeva/CS Infinity/CS/CS doubt.md","className":"text-gray-700 hover:text-indigo-600 hover:bg-gray-50 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold","children":"CS doubt"}]}],["$","li","/Users/jeevas/Documents/Jeeva/CS Infinity/CS/Files running.md",{"children":["$","$Lf",null,{"href":"#/Users/jeevas/Documents/Jeeva/CS Infinity/CS/Files running.md","className":"text-gray-700 hover:text-indigo-600 hover:bg-gray-50 group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold","children":"Files running"}]}]]}]]}]]}]}]]}]}],["$","main",null,{"className":"py-10 lg:pl-72","children":["$","div",null,{"className":"px-4 sm:px-6 lg:px-8","children":[["$","div","Famous algo",{"className":"mb-12","children":[["$","h2",null,{"className":"text-2xl font-bold mb-6 text-gray-900 dark:text-white","children":"Famous algo"}],["$","div",null,{"className":"grid grid-cols-1 md:grid-cols-2 gap-6","children":[["$","article","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/0 Outline.md",{"id":"/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/0 Outline.md","className":"bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6","children":[["$","h3",null,{"className":"text-xl font-semibold mb-4 text-gray-900 dark:text-white","children":"0 Outline"}],["$","div",null,{"className":"prose dark:prose-invert prose-sm max-w-none","dangerouslySetInnerHTML":{"__html":"<p>Noted</p>\n<p><a href=\"https://youtu.be/kp3fCihUXEg?si=lJoiiwBRlFpFtJu3\">top 7 algo</a>\n<a href=\"https://www.youtube.com/watch?v=4TUgqm2gJkE\">bigO</a></p>\n<p>[[Search]]\n[[Famous algo/Sort]]\n[[Greedy]]</p>\n<p>[[Big O]]</p>\n"}}]]}],["$","article","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Big O.md",{"id":"/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Big O.md","className":"bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6","children":[["$","h3",null,{"className":"text-xl font-semibold mb-4 text-gray-900 dark:text-white","children":"Big O"}],["$","div",null,{"className":"prose dark:prose-invert prose-sm max-w-none","dangerouslySetInnerHTML":{"__html":"$10"}}]]}],["$","article","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Greedy.md",{"id":"/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Greedy.md","className":"bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6","children":[["$","h3",null,{"className":"text-xl font-semibold mb-4 text-gray-900 dark:text-white","children":"Greedy"}],["$","div",null,{"className":"prose dark:prose-invert prose-sm max-w-none","dangerouslySetInnerHTML":{"__html":"$11"}}]]}],["$","article","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Search.md",{"id":"/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Search.md","className":"bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6","children":[["$","h3",null,{"className":"text-xl font-semibold mb-4 text-gray-900 dark:text-white","children":"Search"}],["$","div",null,{"className":"prose dark:prose-invert prose-sm max-w-none","dangerouslySetInnerHTML":{"__html":"$12"}}]]}],["$","article","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Sort.md",{"id":"/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/Famous algo/Sort.md","className":"bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6","children":[["$","h3",null,{"className":"text-xl font-semibold mb-4 text-gray-900 dark:text-white","children":"Sort"}],["$","div",null,{"className":"prose dark:prose-invert prose-sm max-w-none","dangerouslySetInnerHTML":{"__html":"$13"}}]]}]]}]]}],["$","div","sorting",{"className":"mb-12","children":[["$","h2",null,{"className":"text-2xl font-bold mb-6 text-gray-900 dark:text-white","children":"sorting"}],["$","div",null,{"className":"grid grid-cols-1 md:grid-cols-2 gap-6","children":[["$","article","/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/sorting/Sort.md",{"id":"/Users/jeevas/Documents/Jeeva/CS Infinity/Algorithms/sorting/Sort.md","className":"bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6","children":[["$","h3",null,{"className":"text-xl font-semibold mb-4 text-gray-900 dark:text-white","children":"Sort"}],["$","div",null,{"className":"prose dark:prose-invert prose-sm max-w-none","dangerouslySetInnerHTML":{"__html":"<p>sorting olympics</p>\n<p>https://www.youtube.com/watch?v=N4JVT3eVBP8</p>\n"}}]]}]]}]]}],["$","div","ORMs",{"className":"mb-12","children":[["$","h2",null,{"className":"text-2xl font-bold mb-6 text-gray-900 dark:text-white","children":"ORMs"}],["$","div",null,{"className":"grid grid-cols-1 md:grid-cols-2 gap-6","children":[["$","article","/Users/jeevas/Documents/Jeeva/CS Infinity/CS/Backend/DB/ORMs/Stacks.md",{"id":"/Users/jeevas/Documents/Jeeva/CS Infinity/CS/Backend/DB/ORMs/Stacks.md","className":"bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6","children":[["$","h3",null,{"className":"text-xl font-semibold mb-4 text-gray-900 dark:text-white","children":"Stacks"}],["$","div",null,{"className":"prose dark:prose-invert prose-sm max-w-none","dangerouslySetInnerHTML":{"__html":"$14"}}]]}]]}]]}],["$","div","CS",{"className":"mb-12","children":[["$","h2",null,{"className":"text-2xl font-bold mb-6 text-gray-900 dark:text-white","children":"CS"}],["$","div",null,{"className":"grid grid-cols-1 md:grid-cols-2 gap-6","children":[["$","article","/Users/jeevas/Documents/Jeeva/CS Infinity/CS/CMD commands.md",{"id":"/Users/jeevas/Documents/Jeeva/CS Infinity/CS/CMD commands.md","className":"bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6","children":[["$","h3",null,{"className":"text-xl font-semibold mb-4 text-gray-900 dark:text-white","children":"CMD commands"}],["$","div",null,{"className":"prose dark:prose-invert prose-sm max-w-none","dangerouslySetInnerHTML":{"__html":"$15"}}]]}],["$","article","/Users/jeevas/Documents/Jeeva/CS Infinity/CS/CS doubt.md",{"id":"/Users/jeevas/Documents/Jeeva/CS Infinity/CS/CS doubt.md","className":"bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6","children":[["$","h3",null,{"className":"text-xl font-semibold mb-4 text-gray-900 dark:text-white","children":"CS doubt"}],["$","div",null,{"className":"prose dark:prose-invert prose-sm max-w-none","dangerouslySetInnerHTML":{"__html":"<p>in hashmap , when collosion happen , it is stored as linked list..</p>\n<p>but how this more values to single key makes its usable ?</p>\n"}}]]}],["$","article","/Users/jeevas/Documents/Jeeva/CS Infinity/CS/Files running.md",{"id":"/Users/jeevas/Documents/Jeeva/CS Infinity/CS/Files running.md","className":"bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6","children":[["$","h3",null,{"className":"text-xl font-semibold mb-4 text-gray-900 dark:text-white","children":"Files running"}],["$","div",null,{"className":"prose dark:prose-invert prose-sm max-w-none","dangerouslySetInnerHTML":{"__html":"<p>python file running</p>\n<p>python3 filename.py</p>\n<p>ts file running</p>\n<p>tsc runner.ts &#x26; node runner.js</p>\n<p>rs file running</p>\n<p>rustc runner.rs &#x26;&#x26; ./runner</p>\n"}}]]}]]}]]}]]}]}]]}]
d:[["$","meta","0",{"name":"viewport","content":"width=device-width, initial-scale=1"}]]
b:[["$","meta","0",{"charSet":"utf-8"}],["$","title","1",{"children":"CS Infinity Notes"}],["$","meta","2",{"name":"description","content":"A collection of Computer Science and Programming notes"}],["$","link","3",{"rel":"icon","href":"/favicon.ico","type":"image/x-icon","sizes":"16x16"}]]
9:null
