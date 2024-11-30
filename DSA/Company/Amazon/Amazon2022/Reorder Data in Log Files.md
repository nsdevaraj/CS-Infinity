


### Problem Statement: Reorder Data in Log Files

You are given an array of logs, where each log is a space-delimited string of words. The first word in each log is the identifier. There are two types of logs:

- **Letter-logs:** All words (except the identifier) consist of lowercase English letters.
- **Digit-logs:** All words (except the identifier) consist of digits.

Your task is to reorder these logs according to the following rules:

1. The letter-logs must come before all digit-logs.
2. The letter-logs are sorted lexicographically by their contents. If the contents are the same, they should be sorted lexicographically by their identifiers.
3. The digit-logs should maintain their relative ordering.

### Input

- An array of logs, where:
  - \( 1 \leq \text{logs.length} \leq 100 \)
  - \( 3 \leq \text{logs[i].length} \leq 100 \)
  - All tokens in logs[i] are separated by a single space.
  - Each log is guaranteed to have an identifier and at least one word after the identifier.

### Output

- Return the final order of the logs after reordering.

### Examples

**Example 1:**

Input:
```python
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
```

Output:
```python
["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
```

**Explanation:** The letter-log contents are all different, so their ordering is "art can", "art zero", and "own kit dig". The digit-logs maintain their original order.

---

**Example 2:**

Input:
```python
logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
```

Output:
```python
["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
```

### Constraints

- All logs adhere to the specified format, and the identifiers are unique.


Sure! Here are the explanations for the example outputs provided:

### Example 1

**Input:**
```python
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
```

**Output:**
```python
["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
```

**Explanation:**
1. **Separation of Logs:**
   - **Letter-logs:** 
     - "let1 art can"
     - "let2 own kit dig"
     - "let3 art zero"
   - **Digit-logs:** 
     - "dig1 8 1 5 1"
     - "dig2 3 6"

2. **Sorting Letter-logs:**
   - The letter-logs are sorted lexicographically based on their contents. The contents are compared as follows:
     - "art can" vs "own kit dig" vs "art zero"
     - "art can" comes first.
     - "art zero" comes next (as it has the same content "art" but is different).
     - "own kit dig" comes last.

3. **Final Order:**
   - The letter-logs are ordered as: 
     - "let1 art can"
     - "let3 art zero"
     - "let2 own kit dig"
   - The digit-logs maintain their original order:
     - "dig1 8 1 5 1"
     - "dig2 3 6"

### Example 2

**Input:**
```python
logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
```

**Output:**
```python
["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
```

**Explanation:**
1. **Separation of Logs:**
   - **Letter-logs:** 
     - "g1 act car"
     - "ab1 off key dog"
     - "a8 act zoo"
   - **Digit-logs:** 
     - "a1 9 2 3 1"
     - "zo4 4 7"

2. **Sorting Letter-logs:**
   - The letter-logs are sorted based on their contents:
     - "act car" vs "off key dog" vs "act zoo"
     - "act car" comes first.
     - "act zoo" comes next (same content "act" but different identifier).
     - "off key dog" comes last.

3. **Final Order:**
   - The letter-logs are ordered as:
     - "g1 act car"
     - "a8 act zoo"
     - "ab1 off key dog"
   - The digit-logs maintain their original order:
     - "a1 9 2 3 1"
     - "zo4 4 7"

### Summary
In both examples, the letter-logs are sorted first based on their contents and identifiers, while the digit-logs are kept in their original order. This results in the final output where letter-logs appear before digit-logs, following the required sorting criteria.





## Soln

```python

def reorder_data_1(logs: List[str]) -> List[str]:

    letter_logs, digit_logs = [], []

    for log in logs:
        # we can take last letter or whole text after first word too
        second_word_first_char = log.split(" ")[1][0]
        if second_word_first_char.isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    letter_logs.sort(
        key=lambda x: (x.split(" ")[1:], x.split(" ")[0])
    )

    return letter_logs + digit_logs


```

![[reorder_data_in_log_files.py]]


{

extra approaches: from chatGPT

Here are several different approaches to solve the problem of reordering logs based on whether they are letter logs or digit logs:

### 1. **Basic Sorting with Two Passes**
   - **Approach**: Separate the logs into two lists, then sort the letter logs by their content and identifier.
   - **Implementation**:
     ```python
     def reorder_logs(logs):
         letter_logs = []
         digit_logs = []

         for log in logs:
             if log.split()[1].isdigit():
                 digit_logs.append(log)
             else:
                 letter_logs.append(log)

         letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
         return letter_logs + digit_logs
     ```

### 2. **Using `sorted` with Custom Key**
   - **Approach**: Use the built-in `sorted()` function with a custom sorting key that handles both types of logs in one go.
   - **Implementation**:
     ```python
     def reorder_logs(logs):
         return sorted(logs, key=lambda x: (x.split()[1].isdigit(), x.split()[1:], x.split()[0]))
     ```
   - **Explanation**: The sorting key checks if a log is a digit log (to sort them last), and then sorts letter logs by content and identifier.

### 3. **Using List Comprehensions**
   - **Approach**: Utilize list comprehensions to create the two lists and sort them.
   - **Implementation**:
     ```python
     def reorder_logs(logs):
         letter_logs = [log for log in logs if not log.split()[1].isdigit()]
         digit_logs = [log for log in logs if log.split()[1].isdigit()]

         letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
         return letter_logs + digit_logs
     ```

### 4. **Using a Tuple for Sorting**
   - **Approach**: Construct a tuple that represents the sorting criteria for each log.
   - **Implementation**:
     ```python
     def reorder_logs(logs):
         def log_key(log):
             parts = log.split()
             return (1 if parts[1].isdigit() else 0, parts[1:], parts[0])

         return sorted(logs, key=log_key)
     ```

### 5. **Using `filter` and `map` Functions**
   - **Approach**: Use functional programming constructs like `filter` and `map` to separate and sort the logs.
   - **Implementation**:
     ```python
     def reorder_logs(logs):
         letter_logs = list(filter(lambda log: not log.split()[1].isdigit(), logs))
         digit_logs = list(filter(lambda log: log.split()[1].isdigit(), logs))

         letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
         return letter_logs + digit_logs
     ```

### 6. **In-Place Modification (Not Recommended for Clarity)**
   - **Approach**: Modify the original list in place, which can be less readable and is generally not recommended for clarity.
   - **Implementation**:
     ```python
     def reorder_logs(logs):
         i = 0
         while i < len(logs):
             if logs[i].split()[1].isdigit():
                 logs.append(logs.pop(i))
             else:
                 i += 1

         letter_logs = logs[:len(logs) - len(digit_logs)]
         letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
         return letter_logs + logs[len(letter_logs):]
     ```

### Summary
Each of these approaches offers a different way to tackle the problem, emphasizing different aspects such as clarity, conciseness, or leveraging built-in Python functions. The choice of which to use may depend on personal preference or specific requirements of the project.


}



for more: check


Reorder Data in Log Files: https://leetcode.com/problems/reorder-data-in-log-files/






