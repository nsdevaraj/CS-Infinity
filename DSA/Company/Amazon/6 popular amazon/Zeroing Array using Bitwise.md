

### Problem Description

Joker has attacked Gotham City. Our savior, Batman, has been captured, and it is up to you to save this city.

You break a deal with the Joker. He gives you a problem to solve. If you succeed, he will release Batman; otherwise, he will kill him.

Joker will give you an array `A` of `N` elements. You can make some special moves on this array.

A **special move** is defined as follows:

In one move, you choose two distinct indices `i` and `j` such that

```
A[i] & A[j] = X
```

and make

```
A[i] = A[i] ⊕ X
```

```
A[j] = A[j] ⊕ X.
```

You can perform these moves an infinite number of times on any pair of indices.

Your task is to determine if it is possible to make all the elements of the array equal to `0`.

Can you ever solve this problem, or is the Joker playing with you?

## Input Format
- The first and only argument consists of an integer array `A`.

## Output Format
- Return `True` if it is possible to make all elements zero, otherwise return `False`.

## Problem Constraints
- ``1 <= N <= 10^5``
- ``0 <= A[i] <= 10^9``

## Example

### Input
```
A = [2, 3, 2]
```

### Output
```
True
```

### Explanation
- The operations can be performed repeatedly to reduce all elements to zero.

### Input
```
A = [2, 3, 5]
```

### Output
```
False
```

### Explanation
- It is impossible to make all elements zero using the allowed operations.

## Notes
- You may assume that any two indices can be chosen multiple times.


## Soln

```python

# Time complexity - O(n^2) since taking all pairs
def zeroing_ary_bitwise_1(ary:List[int])-> bool:
    ary_len = len(ary)
    changed = True
    while changed:
        changed = False
        for i in range(ary_len-1):
            for j in range(i+1,ary_len):
                x= ary[i] & ary[j]
                if(x>0):
                    updated_i, updated_j = ary[i] ^ x, ary[j] ^ x
                    if(ary[i] != updated_i or ary[j] != updated_j):
                        ary[i], ary[j] = updated_i , updated_j
                        changed = True

    return all(x== 0 for x in ary)


# Time complexity - 32n => O(n)
# space complexity - 32 => O(1)
def zeroing_ary_bitwise_2(ary:List[int])-> bool:
    bits_count = [0] * 31
    for e in ary:
        for i in range(32):
            if((e >> i) & 1):
                bits_count[i] += 1
    for b in bits_count:
        if(b%2):
            return False
    return True


```



{
other items to check
https://www.geeksforgeeks.org/number-ordered-pairs-ai-aj-0/

https://leetcode.com/discuss/interview-question/1528662/determine-the-number-of-pairsijsuch-that-aiaj-and-ij-is-divisible-by-x

https://leetcode.com/discuss/general-discussion/881840/pairs-having-similar-elemnts

https://leetcode.com/discuss/interview-question/841897/an-interesting-xor-based-question

https://stackoverflow.com/questions/78767583/increasing-triplet-subsequence-issue-with-the-accepted-answer-by-leetcode


}

