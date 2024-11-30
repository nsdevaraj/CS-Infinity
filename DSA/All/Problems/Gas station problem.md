

[ Gas station - YT (InsideCode)](https://www.youtube.com/watch?v=o3DUXPRyvT8&list=PL3edoBgC7ScW_CBHbMc0FtdXfzgpBOGIb&index=29&t=2211s)

[? Gas Station @LeetCode#134](https://leetcode.com/problems/gas-station/)

### Problem: Gas Station

Given two arrays: 
- `gas[]` represents the amount of gas available at each station.
- `cost[]` represents the amount of gas required to travel from the current station to the next.

The gas stations form a circular route. Your task is to find the starting station index from which we can traverse the entire circle without running out of gas. If no such station exists, return `-1`.

#### Example:

```plaintext
Input:
gas =  [1, 5, 3, 3, 5, 3, 1, 4, 5, 1]
cost = [5, 2, 2, 8, 2, 4, 2, 1, 2, 5]

Output: 8

Explanation:
Starting at station 8:
+4 (gas) -1 (cost), remaining gas = 3
+5 -2, remaining gas = 6
+1 -5, remaining gas = 2
+5 -2, remaining gas = 5
+3 -2, remaining gas = 6
+3 -8, remaining gas = 1
+5 -2, remaining gas = 4
+3 -4, remaining gas = 3
+1 -2, remaining gas = 2
+3 -5, remaining gas = 0 (back to station 8)

We can traverse all stations and return to station 8 without running out of gas.
```

### Brute Force Approach: Simulate Each Starting Station

The brute force solution checks each station as a potential starting point. We simulate driving from each station and track the remaining gas at each step.

#### Code:

```python
from typing import List

# Function to check if we can complete a cycle starting from 'start'
def can_traverse(gas: List[int], cost: List[int], start: int) -> bool:
    n = len(gas)
    remaining = 0
    i = start
    started = False
    # Continue traversing the circular route
    while i != start or not started:
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:  # Can't reach the next station
            return False
        i = (i + 1) % n  # Move to the next station, wrap around with modulus
    return True

# Main function that simulates traversal from every station
def gas_station_bruteforce(gas: List[int], cost: List[int]) -> int:
    for i in range(len(gas)):  # Check every station as a possible start
        if can_traverse(gas, cost, i):
            return i  # Found a valid start
    return -1  # No valid start found
```

#### Time Complexity: 
- **$O(n^2)$** where $n$ is the number of stations. In the worst case, each starting point results in a complete cycle simulation.

#### Space Complexity: 
- **$O(1)$**, constant space, as no additional structures are required.

### Kadane's Algorithm

Understand:
 IF a station start reacher a negative amount at the index i, then all stations between start and i inclusive are invalid, we start again from i + 1


see num[start] must be greater than cost[start] in order to go to next station...
so when nums start upto gone upto i and in i it give negative values means then 
num[start] and cost[num] gave extra fuels, but with those extra values to it can't come after num[i], so no between will pass since you don't have extra fuels too.. 
i.e even with bonus fuel we can't make it, then how we can make it without even bonus.. 


We can optimize the solution by eliminating unnecessary checks. The key idea is:
1. If starting from station `i` leads to a negative remaining gas at station `j`, then no station between `i` and `j` can be a valid starting point.
2. Thus, we can skip all stations between `i` and `j` and move directly to `j+1`.



since its single iteration...

when we are having start index at mid and at end we have still remaining values, then you have to consider previ_remianing i.e remaining found before mid ( which is negative ) have to be subtracted by current remaing values and it should be greater than -1



#### Code:

```python
from typing import List

# Optimized approach to find the starting gas station
def gas_station_optimized(gas: List[int], cost: List[int]) -> int:
    remaining = 0  # Tracks current gas after visiting each station
    prev_remaining = 0  # Tracks the leftover gas when switching candidates
    candidate = 0  # Potential valid starting station

    # Traverse through all stations
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]  # Update the remaining gas
        if remaining < 0:  # If we can't reach the next station
            candidate = i + 1  # Update the candidate to the next station
            prev_remaining += remaining  # Keep track of gas deficit
            remaining = 0  # Reset remaining gas for the new candidate

    # Check if the total gas is enough for a full circle
    if candidate == len(gas) or remaining + prev_remaining < 0:
        return -1  # No valid station
    else:
        return candidate  # Return the valid station
```


```python
from typing import List

def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    n = len(gas)  # Number of gas stations

    current_gas = 0  # Current gas from the starting point
    total_deficit = 0  # Total gas deficit encountered
    start_index = 0  # Starting index for the circuit

    for i in range(n):
        current_gas += gas[i] - cost[i]  # Update current gas after visiting station i

        # If current gas is negative, we cannot start from the previous start_index
        if current_gas < 0:
            total_deficit += current_gas  # Add deficit to total
            start_index = i + 1  # Update start index to the next station
            current_gas = 0  # Reset current gas for the new start

    # If total gas available is less than total cost, return -1
    if current_gas + total_deficit < 0:
        return -1

    return start_index  # Return the starting index from where we can complete the circuit


```



```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res = 0
        total = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1

        return res
        
```


#### Explanation:
- If starting at a station results in negative gas at any point, we move to the next potential candidate.
- After traversing the stations, if the total gas from the beginning is enough to cover the deficit (`remaining + prev_remaining`), the candidate is valid.

#### Time Complexity: 
- **$O(n)$** because we only traverse the stations once, and we immediately skip invalid ranges.
  
#### Space Complexity:
- **$O(1)$**, constant space as we only use variables for tracking candidates and remaining gas.

### Summary Table:

| Approach           | Time Complexity | Space Complexity | Explanation                                                      |
| ------------------ | --------------- | ---------------- | ---------------------------------------------------------------- |
| Brute Force        | $O(n^2)$        | $O(1)$           | Simulates every station and checks if it can complete the cycle. |
| Kadane's Algorithm | $O(n)$          | $O(1)$           | Skips invalid stations and checks the candidate in one pass.     |

The optimized solution is preferable due to its linear time complexity, making it much faster for larger inputs.





