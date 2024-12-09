

## Validate IP Address (LeetCode #468)

[**LeetCode Link**](https://leetcode.com/problems/validate-ip-address)

---

### Problem Statement

Write a function to validate an IP address. The input can either be a valid **IPv4** or **IPv6** address, or it can be neither.

### Rules for Validation:

#### IPv4:

1. Consists of four decimal numbers separated by dots (`.`).
2. Each part must be between `0` and `255`, inclusive.
3. Leading zeros are not allowed (e.g., "01" is invalid).
4. Each segment must be a numeric string.

#### IPv6:

1. Consists of eight groups of four hexadecimal digits separated by colons (`:`).
2. Each group can have 1 to 4 hexadecimal characters (digits or letters `a-f` / `A-F`).
3. Leading zeros are allowed, (but groups cannot be empty)

---

### Example

**Input 1:**

```plaintext
IP = "172.16.254.1"
```

**Output 1:**

```plaintext
"IPv4"
```

**Input 2:**

```plaintext
IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
```

**Output 2:**

```plaintext
"IPv6"
```

**Input 3:**

```plaintext
IP = "256.256.256.256"
```

**Output 3:**

```plaintext
"Neither"
```

---

### Approaches

|**Approach**|**Time Complexity**|**Space Complexity**|**Description**|
|---|---|---|---|
|**Regex Matching**|O(1)O(1)|O(1)O(1)|Validates the format using regular expressions for IPv4 and IPv6.|
|**String Parsing**|O(n)O(n)|O(1)O(1)|Splits the string manually and validates each part.|

---

### Solution Using Regex Matching

A simple and efficient solution uses regular expressions to validate the formats of IPv4 and IPv6 addresses.

```python
import re

def validIPAddress(IP):
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
    ipv6_pattern = r'^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})$'

    if re.match(ipv4_pattern, IP):
        return "IPv4"
    elif re.match(ipv6_pattern, IP):
        return "IPv6"
    else:
        return "Neither"
```

---

### Solution Using String Parsing

This approach manually checks the format of the IP address by splitting the string and validating each part.


```js

def validIPAddress(addressText:str)-> Literal['IPv4' ,'IPv6' ,'Neither']:

    def isValidIPv4Address()-> bool:
        sections = addressText.split('.')

        if(len(sections) != 4):
            return False

        for section in sections:
            isStarted = False
            sectionInt = 0
            try:
                sectionInt = int(section)
                if(not(-1 < sectionInt < 256)):
                    return False
            except ValueError:
                return False

            for s in section:
                if(not isStarted and s == '0'):
                    if(len(section)==1):
                        continue
                    return False
                else:
                    isStarted = True
        return True

    def isValidIPv6Address()-> bool:
        sections = addressText.split(':')

        if(len(sections) != 8):
            return False

        for section in sections:
            if(not(0 < len(section) < 5)):
                return False

            for s in section:
                if (not(s.isdigit() or s in "abcdefABCDEF")):
                    return False

        return True



    if '.' in addressText:
        return 'IPv4' if isValidIPv4Address() else 'Neither'
    elif ':' in addressText:
        return 'IPv6' if isValidIPv6Address() else 'Neither'


    return 'Neither'


```

#### Code:

```python
def validIPAddress(IP):
    def is_valid_ipv4(ip):
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255 or (len(part) > 1 and part[0] == "0"):
                return False
        return True

    def is_valid_ipv6(ip):
        parts = ip.split(":")
        if len(parts) != 8:
            return False
        for part in parts:
            if not (1 <= len(part) <= 4) or not all(c in "0123456789abcdefABCDEF" for c in part):
                return False
        return True

    if "." in IP and is_valid_ipv4(IP):
        return "IPv4"
    elif ":" in IP and is_valid_ipv6(IP):
        return "IPv6"
    else:
        return "Neither"
```

---

### Test Cases

```python
def test_validIPAddress(func):
	
    test_cases = [
        {"input": "172.16.254.1", "expected": "IPv4"},
        {"input": "2001:0db8:85a3:0:0:8A2E:0370:7334", "expected": "IPv6"},
        {"input": "256.256.256.256", "expected": "Neither"},
        {"input": "192.0.0.01", "expected": "Neither"},
        {"input": "2001:0db8:85a3::8A2E:0370:7334", "expected": "Neither"},
        {"input": "2001:db8:85a3:0:0:8A2E:370:7334", "expected": "IPv6"},
        {"input": "192.0.0.1", "expected": "IPv4"},
        {"input": "01.01.01.01", "expected": "Neither"}
    ]

    for i, case in enumerate(test_cases, 1):
        result = func(case["input"])
        assert result == case["expected"], \
            f"Test case {i} failed: input={case['input']}, expected={case['expected']}, got={result}"
    print("All test cases passed!")

# Example usage
test_validIPAddress(validIPAddress)
```

---

### Comparison of Approaches

|**Approach**|**Advantages**|**Disadvantages**|
|---|---|---|
|**Regex Matching**|Concise and easy to understand.|Requires knowledge of regex syntax.|
|**String Parsing**|More flexible for custom validations.|Longer and more manual implementation.|

---

### Summary

Both approaches work well, but **Regex Matching** is usually shorter and easier to implement, making it a preferred choice for interviews or competitive programming. However, **String Parsing** provides more control and is easier to debug.





---


```python
import re

def validIPAddress(addressText: str) -> str:
    # Check if it's a valid IPv4 address
    def is_valid_ipv4(address: str) -> bool:
        segments = address.split('.')
        if len(segments) != 4:
            return False
        for segment in segments:
            if not segment.isdigit():
                return False
            num = int(segment)
            # Check for leading zeros and number bounds
            if num < 0 or num > 255 or (segment != str(num)):  
                return False
        return True

    # Check if it's a valid IPv6 address
    def is_valid_ipv6(address: str) -> bool:
        segments = address.split(':')
        if len(segments) != 8:
            return False
        hex_chars = "0123456789abcdefABCDEF"
        for segment in segments:
            if len(segment) == 0 or len(segment) > 4:
                return False
            if not all(c in hex_chars for c in segment):
                return False
        return True

    # Check for IPv4
    if '.' in addressText:
        if is_valid_ipv4(addressText):
            return 'IPv4'
    
    # Check for IPv6
    elif ':' in addressText:
        if is_valid_ipv6(addressText):
            return 'IPv6'
    
    # If neither IPv4 nor IPv6, return 'Neither'
    return 'Neither'

```

### 5. **Find All Valid IP Addresses**

**Problem:** Given a string containing only digits, restore it by returning all possible valid IP address combinations.

```python
def restore_ip_addresses(s):
    def is_valid(segment):
        return 0 <= int(segment) <= 255 and (segment[0] != '0' or len(segment) == 1)

    result = []
    for i in range(1, len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                part1, part2, part3, part4 = s[:i], s[i:j], s[j:k], s[k:]
                if is_valid(part1) and is_valid(part2) and is_valid(part3) and is_valid(part4):
                    result.append(f"{part1}.{part2}.{part3}.{part4}")
    return result
```



Memory: 16.4mb

python

```python
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_hex(s):
            return re.fullmatch(r"^[0-9a-fA-F]+$", s or "") is not None

        def isIPv4_num(s):
            # validates if string s is valid IPv4_num 
            if s == "":
                return False 

            for char in s:
                if not char.isdigit(): 
                    return False 

            # validate if there are no leading zeros 
            if s[0] == "0" and len(s) > 1:
                return False 

            number = int(s) 

            if number < 0 or number > 255:
                return False 

            return True 

        def isIPv8_num(s): 
            if len(s) < 1 or len(s) > 4:
                return False 

            return is_hex(s) 

        
        # TODO: check if both a '.' and ':' are contained in string and return "Neither"
        has_dot = '.' in queryIP 
        has_colon = ':' in queryIP 

        # either doesn't contain either or contains both 
        if has_dot == has_colon:
            return "Neither"

        # TODO: Case 1, only a '.' is contained in the string 
        if has_dot:
            # then validate if it is an IPv4
            X = queryIP.split(".")
            if len(X) != 4:
                return "Neither"

            # validate each digit 
            for x in X: 
                if not isIPv4_num(x): 
                    return "Neither"

            return "IPv4"


        # TODO: Case 2, onl a ':' is contained in the string 
        if has_colon: 
            X = queryIP.split(":")

            if len(X) != 8:
                return "Neither"

            for x in X:
                if not isIPv8_num(x): 
                    return "Neither" 

            return "IPv6" 

        return "Neither"
```


Runtime: 0ms

python

```python
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        sections = queryIP.split(".")
        if len(sections) == 4:
            for section in sections:
                if not section.isnumeric():
                    return "Neither"
                if int(section) > 255:
                    return "Neither"
                if section != "0" and section[0] == "0":
                    return "Neither"

            return "IPv4"
        else:
            sections = queryIP.split(":")
            if len(sections) != 8:
                return "Neither"
            for section in sections:
                if len(section) < 1 or len(section) > 4:
                    return "Neither"
                for c in section:
                    is_af = ord(c) >= ord("a") and ord(c) <= ord("f")
                    is_AF = ord(c) >= ord("A") and ord(c) <= ord("F")
                    if not (c.isdigit() or is_af or is_AF):
                        return "Neither"
            return "IPv6"
```



---


to check {


https://leetcode.com/problems/validate-ip-address/editorial/


}






extra {

### More Examples of Valid and Invalid IP Addresses

#### **Examples of Valid IPv4 Addresses:**

1. `192.168.1.1` - All parts are within `0-255`.
2. `0.0.0.0` - Special case for default routes in networking.
3. `255.255.255.255` - Broadcast address.
4. `1.2.3.4` - Minimal valid address.

#### **Examples of Invalid IPv4 Addresses:**

1. `256.256.256.256` - Each segment must be between `0-255`.
2. `192.168.01.1` - Leading zeros are not allowed in IPv4.
3. `192.168.1` - Missing one part (IPv4 requires exactly 4 parts).
4. `192.168.1.a` - Contains a non-numeric character.

#### **Examples of Valid IPv6 Addresses:**

1. `2001:0db8:85a3:0000:0000:8a2e:0370:7334` - Fully specified IPv6 address.
2. `2001:db8:85a3::8a2e:370:7334` - Shortened notation (`::` replaces one or more groups of `0000`).
3. `::1` - Loopback address.
4. `fe80::` - Link-local address.

#### **Examples of Invalid IPv6 Addresses:**

1. `2001:0db8:85a3:0000:0000:8a2e:0370:73345` - One part exceeds 4 hexadecimal digits.
2. `2001:db8::85a3::8a2e:7334` - Contains multiple `::`, which is not allowed.
3. `2001:0db8:85a3:z:0000:8a2e:0370:7334` - Contains invalid characters (like `z`).
4. `02001:0db8:85a3:0000:0000:8a2e:0370:7334` - Leading zeros are not allowed in IPv6 groups.

---

### Why `02001:0db8:85a3:0000:0000:8a2e:0370:7334` is Invalid?

1. **Rule for IPv6 Format:** Each group (separated by colons `:`) in an IPv6 address must be 1 to 4 hexadecimal digits, and leading zeros are allowed but are optional. Groups should not contain unnecessary leading zeros that increase the number of digits to more than 4.
    
2. **Violation:** The first group `02001` contains **5 digits**, which is invalid for an IPv6 address. While leading zeros are permissible (e.g., `0001` is valid), they should not result in the group exceeding the 4-digit limit.
    
    - Correct representation: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.

---

### General Notes:

- **IPv4:** Segments should not have leading zeros.
- **IPv6:** Groups must be 1 to 4 hexadecimal digits. Leading zeros are fine but should not inflate group size beyond 4 digits.


}