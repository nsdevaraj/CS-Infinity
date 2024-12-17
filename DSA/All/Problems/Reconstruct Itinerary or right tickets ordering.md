


The **332. Reconstruct Itinerary**(A route or proposed route of a journey) problem requires reconstructing an itinerary from a list of tickets where each ticket is represented as `(from, to)`. The goal is to find an itinerary that starts at `"JFK"` and uses all the tickets exactly once, respecting lexical order when multiple valid itineraries exist.

---

reffered {
https://www.youtube.com/watch?v=ZyB_gQ8vqGA

https://youtu.be/WYqsg5dziaQ?si=4pwKKspTR8QeEJX6


}

---

Leetcode : https://leetcode.com/problems/reconstruct-itinerary



### Problem Statement

Given a list of airline tickets represented as pairs of departure and arrival airports `[from, to]`, reconstruct the itinerary in order. The itinerary must:

1. Start at `"JFK"`.
2. Use all the tickets exactly once.
3. Follow **lexicographical order** if there are multiple valid itineraries.

#### Example 1:

- **Input**: `tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]`
- **Output**: `["JFK", "MUC", "LHR", "SFO", "SJC"]`

#### Example 2:

- **Input**: `tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]`
- **Output**: `["JFK","ATL","JFK","SFO","ATL","SFO"]`

---

### Solution Explanation

The problem can be solved using **Hierholzer's Algorithm**, which is designed for finding Eulerian paths in a graph. Here's how we adapt it:

1. **Graph Representation**:
    
    - Use a `HashMap<String, BinaryHeap<Reverse<String>>>` to store all destinations for each departure in sorted order (lexicographically smallest order when popped).
2. **Depth-First Search (DFS)**:
    
    - Start from `"JFK"` and visit destinations recursively.
    - Push the current airport to the result stack **after** visiting all neighbors (post-order traversal).
3. **Reverse the Result**:
    
    - Since we append to the result stack after visiting all neighbors, reversing it will give the correct itinerary.

---

### Implementation in Rust

```rust
use std::collections::{BinaryHeap, HashMap};
use std::cmp::Reverse;

pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
    let mut graph: HashMap<String, BinaryHeap<Reverse<String>>> = HashMap::new();

    // Build the graph
    for ticket in tickets {
        graph
            .entry(ticket[0].clone())
            .or_insert_with(BinaryHeap::new)
            .push(Reverse(ticket[1].clone()));
    }

    let mut result = Vec::new();
    let mut stack = vec!["JFK".to_string()];

    // DFS using iterative stack
    while let Some(airport) = stack.last() {
        if let Some(destinations) = graph.get_mut(airport) {
            if let Some(next) = destinations.pop() {
                stack.push(next.0); // Push next destination
            } else {
                result.push(stack.pop().unwrap()); // No more destinations, add to result
            }
        } else {
            result.push(stack.pop().unwrap()); // Dead end, add to result
        }
    }

    result.reverse(); // Reverse for the correct order
    result
}

```


```rust
// tried not working - have ownership issues.. 
 fn ans_func(mut tickets: Vec<Vec<String>>) -> Vec<String> {
        // Sort tickets lexicographically to maintain lexical ordering
        tickets.sort();

        let tickets_len = tickets.len();

        // Create adjacency map
        let mut adj_map: HashMap<String, Vec<String>> = HashMap::new();
        for ticket in &tickets {
            adj_map
                .entry(ticket[0].clone())
                .or_insert(Vec::new())
                .push(ticket[1].clone());
        }

        let mut itinerary = vec!["JFK".to_string()];

        // DFS function to explore paths safely without repeated mutable borrows
        fn dfs(
            current: &str,
            adj_map: &mut HashMap<String, Vec<String>>,
            itinerary: &mut Vec<String>,
            tickets_len: usize,
        ) -> bool {
            // Base condition: if all tickets are used
            if itinerary.len() == tickets_len + 1 {
                return true;
            }

            // Extract the destination list to avoid multiple mutable borrows
            if let Some(dest_list) = adj_map.get_mut(current) {
                // Sort destinations for lexical order traversal
                let mut local_dest_list = dest_list.clone();
                local_dest_list.sort();

                for i in 0..local_dest_list.len() {
                    let next = local_dest_list[i].clone();

                    // Remove this destination temporarily
                    dest_list.retain(|x| x != &next);
                    itinerary.push(next.clone());

                    // Recurse
                    if dfs(&next, adj_map, itinerary, tickets_len) {
                        return true; // Found a valid path
                    }

                    // Backtrack
                    itinerary.pop();
                    dest_list.push(next.clone());
                }
            }

            false
        }

        // Perform DFS starting at "JFK"
        if dfs("JFK", &mut adj_map, &mut itinerary, tickets_len) {
            itinerary
        } else {
            Vec::new()
        }
    }
```



```python
from collections import defaultdict

def ans_func(tickets):
    # Sort tickets lexicographically to maintain lexical order
    tickets.sort()

    # Create adjacency map
    adj_map = defaultdict(list)
    for src, dst in tickets:
        adj_map[src].append(dst)

    # Sort destinations for lexical order traversal
    for src in adj_map:
        adj_map[src].sort()

    itinerary = ["JFK"]

    def dfs(current):
        # Base condition: if all tickets are used
        if len(itinerary) == len(tickets) + 1:
            return True

        if current in adj_map:
            # Use a copy of the destinations to backtrack safely
            dest_list = list(adj_map[current])
            for i, next_dest in enumerate(dest_list):
                # Remove the destination temporarily
                adj_map[current].pop(i)
                itinerary.append(next_dest)

                # Recurse
                if dfs(next_dest):
                    return True

                # Backtrack
                itinerary.pop()
                adj_map[current].insert(i, next_dest)

        return False

    # Perform DFS starting at "JFK"
    if dfs("JFK"):
        return itinerary
    else:
        return []

```





```python

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create adjacency map for destinations
        adj_map: dict[str, list[str]] = {}
        
        # Sort tickets lexicographically
        tickets.sort()
        
        # Populate adjacency map
        for src, dest in tickets:
            if src not in adj_map:
                adj_map[src] = []
            adj_map[src].append(dest)
        
        start_city = "JFK"
        itinerary: List[str] = [start_city]

        # Perform depth-first search with backtracking
        def dfs(city: str) -> bool:
            # Base case: if itinerary uses all tickets
            if len(itinerary) == len(tickets) + 1:
                return True

            # If there are destinations left from the current city
            if city in adj_map and adj_map[city]:
                # Iterate over destinations
                # for i, next_city in enumerate(adj_map[city]):

                # used adj_cities for safer side.. since modifying adj_map inside loop
                adj_cities = adj_map[city]
                for i, next_city in enumerate(adj_cities):
                    # Simulate using this ticket
                    adj_map[city].pop(i)
                    itinerary.append(next_city)

                    # Recursively explore this path
                    if dfs(next_city):
                        return True

                    # Backtrack
                    itinerary.pop()
                    adj_map[city].insert(i, next_city)

            return False

        # Run the DFS from the starting city
        if dfs(start_city):
            return itinerary
        else:
            return []
```

The `Time Limit Exceeded` (TLE) issue in your depth-first search (DFS) approach is likely caused by redundant work due to repeated backtracking across a lot of paths.


Code

Python3

```python
from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create adjacency map with a list
        adj_map = defaultdict(list)
        
        # Populate the adjacency map with sorted destinations for lexicographical order
        for src, dest in sorted(tickets):
            adj_map[src].append(dest)

        itinerary = []
        
        def dfs(city: str):
            # While there are destinations left from the current node, traverse them
            while adj_map[city]:
                dfs(adj_map[city].pop(0))  # Remove the first available destination
            itinerary.append(city)

        # Start DFS from JFK
        dfs("JFK")
        
        # Return the reversed itinerary
        return itinerary[::-1]
```


---

### Explanation of the Code:

1. **Graph Construction**:
    
    - Use `BinaryHeap<Reverse<String>>` to maintain lexicographical order of destinations for each departure.
2. **Iterative DFS**:
    
    - Use a stack for traversal to avoid recursion depth issues. Push destinations to the stack while traversing.
    - When no further destination exists, backtrack and add the current airport to the result.
3. **Result Reversal**:
    
    - Since nodes are appended in post-order, reverse the result at the end to reconstruct the itinerary.

---

### Complexity Analysis:

1. **Time Complexity**:
    
    - **Graph Construction**: O(Elog⁡E)O(E \log E), where EE is the number of tickets (for sorting).
    - **DFS Traversal**: O(E)O(E), visiting each edge once.
    - Overall: O(Elog⁡E)O(E \log E).
2. **Space Complexity**:
    
    - Graph storage: O(V+E)O(V + E), where VV is the number of airports and EE is the number of tickets.
    - Call stack: O(V)O(V) in worst-case traversal.

---

### Test Cases:

```rust
    fn test_func(ans_func: fn(Vec<Vec<String>>) -> Vec<String>) {
        let cases = vec![
            // Basic case with straightforward lexicographical order
            (
                vec![
                    vec!["JFK".to_string(), "A".to_string()],
                    vec!["A".to_string(), "B".to_string()],
                    vec!["B".to_string(), "C".to_string()],
                ],
                vec![
                    "JFK".to_string(),
                    "A".to_string(),
                    "B".to_string(),
                    "C".to_string(),
                ],
            ),
            // Multiple valid paths, lexicographical tie-breaking
            (
                vec![
                    vec!["JFK".to_string(), "B".to_string()],
                    vec!["JFK".to_string(), "A".to_string()],
                    vec!["B".to_string(), "C".to_string()],
                    vec!["A".to_string(), "C".to_string()],
                ],
                vec![
                    "JFK".to_string(),
                    "A".to_string(),
                    "C".to_string(),
                    "B".to_string(),
                    "C".to_string(),
                ],
            ),
            // Circular itinerary
            (
                vec![
                    vec!["JFK".to_string(), "A".to_string()],
                    vec!["A".to_string(), "B".to_string()],
                    vec!["B".to_string(), "JFK".to_string()],
                ],
                vec![
                    "JFK".to_string(),
                    "A".to_string(),
                    "B".to_string(),
                    "JFK".to_string(),
                ],
            ),
            // Disconnected graph (invalid input, no valid path exists)
            (
                vec![
                    vec!["JFK".to_string(), "A".to_string()],
                    vec!["B".to_string(), "C".to_string()],
                ],
                vec!["JFK".to_string(), "A".to_string()],
            ),
            // Single ticket from JFK
            (
                vec![vec!["JFK".to_string(), "A".to_string()]],
                vec!["JFK".to_string(), "A".to_string()],
            ),
            // Longer itinerary with many destinations
            (
                vec![
                    vec!["JFK".to_string(), "A".to_string()],
                    vec!["A".to_string(), "B".to_string()],
                    vec!["B".to_string(), "C".to_string()],
                    vec!["C".to_string(), "D".to_string()],
                    vec!["D".to_string(), "E".to_string()],
                    vec!["E".to_string(), "F".to_string()],
                ],
                vec![
                    "JFK".to_string(),
                    "A".to_string(),
                    "B".to_string(),
                    "C".to_string(),
                    "D".to_string(),
                    "E".to_string(),
                    "F".to_string(),
                ],
            ),
            // Itinerary with repeated destinations
            (
                vec![
                    vec!["JFK".to_string(), "A".to_string()],
                    vec!["A".to_string(), "JFK".to_string()],
                    vec!["JFK".to_string(), "A".to_string()],
                ],
                vec![
                    "JFK".to_string(),
                    "A".to_string(),
                    "JFK".to_string(),
                    "A".to_string(),
                ],
            ),
            // Multiple destinations from a single airport
            (
                vec![
                    vec!["JFK".to_string(), "A".to_string()],
                    vec!["JFK".to_string(), "B".to_string()],
                    vec!["JFK".to_string(), "C".to_string()],
                    vec!["A".to_string(), "D".to_string()],
                ],
                vec![
                    "JFK".to_string(),
                    "A".to_string(),
                    "D".to_string(),
                    "JFK".to_string(),
                    "B".to_string(),
                    "JFK".to_string(),
                    "C".to_string(),
                ],
            ),
            // No tickets (empty input)
            (vec![], vec![]),
            // Single circular path
            (
                vec![
                    vec!["JFK".to_string(), "A".to_string()],
                    vec!["A".to_string(), "JFK".to_string()],
                ],
                vec!["JFK".to_string(), "A".to_string(), "JFK".to_string()],
            ),
            // Complex itinerary with overlapping paths
            (
                vec![
                    vec!["JFK".to_string(), "A".to_string()],
                    vec!["A".to_string(), "B".to_string()],
                    vec!["B".to_string(), "JFK".to_string()],
                    vec!["JFK".to_string(), "C".to_string()],
                    vec!["C".to_string(), "D".to_string()],
                ],
                vec![
                    "JFK".to_string(),
                    "A".to_string(),
                    "B".to_string(),
                    "JFK".to_string(),
                    "C".to_string(),
                    "D".to_string(),
                ],
            ),
        ];

        for (i, (input, expected)) in cases.iter().enumerate() {
            let result = ans_func(input.clone());
            assert_eq!(result, *expected, "Test case {} failed", i + 1);
        }
        println!("All test cases passed!");
    }

```

---

### Alternative Approaches:

1. **Recursive DFS**:  
    The same algorithm can be implemented recursively, but iterative DFS avoids stack overflow issues for large graphs.
    
2. **Priority Queue**:  
    Use a `PriorityQueue` to process destinations in sorted order instead of using `BinaryHeap`.
    

This solution guarantees an **O(E log E)** runtime with lexicographically sorted output.


---



```js
// slight variant of the problem ( src is not known! )

const findPaths = (stringText) => {
  
  /*
  src: 'city1',
  */
  
  
  // BLR-HYD MAA-BLR BOM-DEL HYD-BOM 
  
  const paths = stringText.split(" ");
  
  pathMaps = {}
  dests = new Set()
  
  paths.forEach((path)=> {
    const [src, dest] = path.split("-")
    pathMaps[src] = dest
    dests.add(dest)
  })
  
  sourcesPossible = Object.keys(pathMaps);
  
  let start = sourcesPossible[0]
  
  for (let startPos of sourcesPossible){
    if(!dests.has(startPos)){
      start = startPos;
      break;
    }
  }
  
  const finalPath = []
  
  while(true){
    ans = `${start}-${pathMaps[start]}`
    finalPath.push(ans);
    start = pathMaps[start]
    if(!pathMaps[start]){
      break
    }
  }
  
  
  console.log(finalPath)
  
  return finalPath.join(" ");
  
  

}


// input => BLR-HYD MAA-BLR BOM-DEL HYD-BOM 
// output => MAA-BLR BLR-HYD HYD-BOM BOM-DEL
console.log(findPaths("BLR-HYD MAA-BLR BOM-DEL HYD-BOM "))



```



---

Other codes:

Memory: 16.4mb

python

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)

        for src, dest in sorted(tickets,reverse=True):
            g[src].append(dest)
        
        st = ["JFK"]
        res = []

        while st:
            curr = st[-1]

            if not g[curr]:
                res.append(st.pop())
            else:
                st.append(g[curr].pop())
        return res[::-1]
             
```


Runtime: 0ms

python

```python
"""
一笔画：
欧拉路径（Eulerian Path）：一条经过图中每条边恰好一次的路径。
欧拉回路（Eulerian Circuit）：如果一条欧拉路径的起点和终点是同一个点，那么这条路径就是欧拉回路。

Hierholzer 算法 是求解欧拉路径和欧拉回路的常用方法，过程如下：
    从起点开始，依次“走”过尚未使用的边。
    如果到达了一个“死路”（没有未使用的边），回溯到前一个顶点。
    ***最终路径连接成完整的欧拉路径或欧拉回路**
"""

#Time: O(NlogN) sorting
#Space: O(N)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. 构建邻接表（sort过的list的值是一个优先队列）
        graph = defaultdict(list)
        for x, y in sorted(tickets):
            graph[x].append(y)
    
        #example 2: graph {'ATL': ['JFK', 'SFO'], 'JFK': ['ATL', 'SFO'], 'SFO': ['ATL']})
        
        def dfs(airport):
            
            while graph[airport]:
                next_airport = graph[airport].pop()  # 从优先队列中弹出最小的机场
                dfs(next_airport)  
                
            result.append(airport)  # 当前机场路径结束，放入结果; 这里是从最后一个放进去的
                                    # 要使路径生成符合欧拉路径的逻辑，你需要在访问完当前机场的所有出发航班后，再将当前机场加入路径。
                                    # 这意味着，路径的生成需要在DFS回溯的过程中进行，而不是在DFS的前序中。
        result = []
        dfs('JFK')
        return result[::-1]  # 由于路径是逆序生成的，所以需要反转


#Time: O(NlogN) heap
#Space: O(N)
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # 1. 构建邻接表，使用最小堆（heapq）来管理目的地的优先队列
        graph = defaultdict(list)
        for from_airport, to_airport in tickets:
            heapq.heappush(graph[from_airport], to_airport)  # 使用 heapq 保持优先级队列
        
        def dfs(airport):
            
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])  # O(log N) 从优先队列中弹出最小的机场
                dfs(next_airport)
            
            result.append(airport)  # 当前机场路径结束，放入结果; 这里是从最后一个放进去的
                                    # 要使路径生成符合欧拉路径的逻辑，你需要在访问完当前机场的所有出发航班后，再将当前机场加入路径。
                                    # 这意味着，路径的生成需要在DFS回溯的过程中进行，而不是在DFS的前序中。
                
        result = []
        dfs('JFK')
        return result[::-1]  # 由于路径是逆序生成的，所以需要反转
```



Here’s the provided Python code with comments and explanations translated into English:

---

### Explanation of the Algorithm

```python
"""
Eulerian Path:
An **Eulerian Path** is a path that traverses every edge in a graph exactly once.  
An **Eulerian Circuit** is an Eulerian Path where the starting point and endpoint are the same.

The **Hierholzer's Algorithm** is commonly used to find Eulerian Paths and Eulerian Circuits. The steps are as follows:
    1. Start at the starting node.
    2. Traverse unused edges until reaching a "dead end" (no unused edges).
    3. Backtrack to the previous node and continue the process.
    ***The final path will connect into a complete Eulerian Path or Eulerian Circuit.
"""
```

---

## 1st Implementation - Using `sorted` for Lexicographical Priority

Time Complexity: **O(NlogN)** for sorting  
Space Complexity: **O(N)** for storing the graph

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. Build adjacency list (sorted destinations act as a priority queue)
        graph = defaultdict(list)
        for x, y in sorted(tickets):  # Sort tickets lexicographically by source and destination
            graph[x].append(y)

        # Example graph created:
        # {'ATL': ['JFK', 'SFO'], 'JFK': ['ATL', 'SFO'], 'SFO': ['ATL']}

        def dfs(airport):
            # Explore all destinations until a "dead end" is reached
            while graph[airport]:
                next_airport = graph[airport].pop()  # Pop from the list
                dfs(next_airport)  
            
            # Add current airport to the result after exploring all outgoing flights
            result.append(airport)
        
        result = []
        dfs('JFK')  # Start DFS from 'JFK'
        return result[::-1]  # Reverse the result because airports are added in reverse order during backtracking
```

### Explanation of the Logic

1. **Graph Construction**:
    
    - The adjacency list `graph` is constructed using sorted tickets, ensuring lexicographical order (smallest destination first).
2. **DFS Traversal**:
    
    - DFS continues until all destinations are explored.
    - After visiting all destinations from the current airport, it appends itself to the result list.
    - This ensures proper backtracking and aligns with the logic of Eulerian Paths.
3. **Reverse the Path**:
    
    - Since the path is built in reverse during DFS, we reverse the final result before returning it.

---

## 2nd Implementation - Using Heap to Prioritize Destinations

Time Complexity: **O(NlogN)** due to heap operations  
Space Complexity: **O(N)** for storing the graph

```python
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # 1. Build adjacency list using a min-heap (heapq) to prioritize lexicographically smallest destinations
        graph = defaultdict(list)
        for from_airport, to_airport in tickets:
            heapq.heappush(graph[from_airport], to_airport)  # Use heapq to maintain the priority queue

        def dfs(airport):
            # Explore all destinations in lexicographically smallest order using heapq
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])  # Pop the smallest destination
                dfs(next_airport)
            
            # Add current airport to the result after exploring all outgoing flights
            result.append(airport)

        result = []
        dfs('JFK')  # Start DFS from 'JFK'
        return result[::-1]  # Reverse the result because airports are added in reverse order during backtracking
```

### Explanation of the Logic

1. **Graph with Heap**:
    
    - Instead of a simple sorted list, this uses a heap (min-heap with `heapq`) to always fetch the lexicographically smallest destination first.
2. **Heap Operations**:
    
    - `heapq.heappush(graph[from_airport], to_airport)` adds each destination into a priority queue.
    - `heapq.heappop(graph[airport])` removes the lexicographically smallest destination in `O(log N)` time.
3. **DFS Traversal**:
    
    - Similar logic to the first example but now uses heaps to efficiently ensure lexicographically ordered traversal.
4. **Final Reversal**:
    
    - The path is built in reverse during backtracking, so it's reversed before being returned.

---

### Comparison of the Two Implementations

1. **The first implementation** uses simple sorting and list manipulations to prioritize destinations.
2. **The second implementation** uses a heap (`heapq`) to maintain dynamic, efficient lexicographical priority over multiple destinations at runtime.

The heap-based approach can have better performance when tickets are numerous and destination management in lexicographical order is a priority.

---

### Example Input/Output

Input tickets:

```python
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["JFK", "NRT"], ["NRT", "JFK"]]
```

Running:

```python
solution = Solution()
result = solution.findItinerary(tickets)
print(result)
```

Expected output:

```
['JFK', 'MUC', 'LHR', 'JFK', 'NRT', 'JFK']
```

This represents a valid Eulerian path through all the given tickets in lexicographically sorted order.

Let me know if you need further clarification!
