

[Restore IP addresses problem  - Inside code](https://youtu.be/vjrSYpeFXeQ?si=kO0gxyExI9TiJ9pD)

[LeetCode #93](https://leetcode.com/problems/restore-ip-addresses/description/)


### Problem Statement: Restore IP Addresses (LeetCode #93)

Given a string containing only digits, return all possible valid IP addresses that can be obtained by inserting three dots into the string. A valid IP address consists of four integers (each between 0 and 255, inclusive) separated by periods. Leading zeros are not allowed for each integer unless the integer is "0".

#### Example
**Input:** 
`s = "25525511135"`

**Output:** 
`["255.255.11.135", "255.255.111.35"]`

### Approach 1: Backtracking (Recursive)

#### Explanation:
We break down the problem into forming four parts of an IP address. Starting from the beginning, we try forming each part using 1, 2, or 3 digits. We recursively proceed to form the remaining parts and check if the IP address is valid.

**Key Points:**
- Each part must be between 0 and 255.
- No part should have leading zeros unless it's the number 0 itself.
- The recursion ends once four valid parts are formed, and the string is exhausted.

#### Code:

```python
from typing import List

# Helper function to perform backtracking
def rec(s: str, i: int, address: List[str], addresses: List[str]) -> None:
    # If we have 4 parts and we've used up the entire string, it's a valid IP
    if len(address) == 4:
        if i == len(s):
            addresses.append('.'.join(address))
        return
    
    # Try to form a part using 1, 2, or 3 digits
    for j in range(i + 1, i + 4):
        next_part = s[i:j]
        # Check validity: within range, no leading zeros
        if j <= len(s) and 0 <= int(next_part) <= 255 and (next_part == '0' or not next_part.startswith('0')):
            address.append(next_part)
            rec(s, j, address, addresses)  # Recursively process the next part
            address.pop()  # Backtrack to try another option

# Main function to restore addresses
def restore_addresses(s: str) -> List[str]:
    addresses = []
    rec(s, 0, [], addresses)
    return addresses

# Example usage:
s = "25525511135"
print(restore_addresses(s))  # Output: ["255.255.11.135", "255.255.111.35"]
```

#### Time Complexity:
- Each level of recursion explores up to 3 possibilities (taking 1, 2, or 3 digits). Given that an IP address has 4 parts and each part has up to 3 digits, the recursion depth is bounded. This results in $O(1)$ complexity since the problem size is bounded by a constant number (4 parts of up to 3 digits).

#### Space Complexity:
- The recursive stack can go as deep as 4 (for the 4 parts), so the space complexity is also $O(1)$.

---

### Approach 2: Iterative (Brute Force)

#### Explanation:
Instead of using recursion, we can try every possible combination of three dots placed between the digits. For each combination, we check if the four parts formed by the dots constitute a valid IP address.

**Key Points:**
- Try placing dots at all combinations of three positions.
- For each combination, check the validity of the four parts.

#### Code:

```python
from typing import List

def restore_addresses_iterative(s: str) -> List[str]:
    addresses = []
    
    # Try placing the three dots at every combination of positions
    for i in range(1, min(len(s), 4)):  # First part
        for j in range(i + 1, i + 4):   # Second part
            for k in range(j + 1, j + 4):  # Third part
                if k < len(s):
                    part1, part2, part3, part4 = s[:i], s[i:j], s[j:k], s[k:]
                    # Validate each part
                    if all(is_valid_part(p) for p in [part1, part2, part3, part4]):
                        addresses.append(f"{part1}.{part2}.{part3}.{part4}")
    
    return addresses

# Helper function to check if a part of the address is valid
def is_valid_part(part: str) -> bool:
    return 0 <= int(part) <= 255 and (part == '0' or not part.startswith('0'))

# Example usage:
s = "25525511135"
print(restore_addresses_iterative(s))  # Output: ["255.255.11.135", "255.255.111.35"]
```

#### Time Complexity:
- The brute force approach generates all possible combinations of placing three dots, so the complexity is $O(1)$ as the number of combinations is fixed.

#### Space Complexity:
- Space complexity is $O(1)$ for storing the list of results.

---

### Summary of Approaches

| Approach       | Method         | Time Complexity | Space Complexity |
|----------------|----------------|-----------------|------------------|
| Backtracking   | Recursive      | $O(1)$          | $O(1)$           |
| Iterative      | Brute Force    | $O(1)$          | $O(1)$           |

---

This problem primarily focuses on using backtracking to explore all valid ways to split the string into four parts and checks if each split can form a valid IP address.





