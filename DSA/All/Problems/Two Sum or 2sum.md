

[LeetCode #1](https://leetcode.com/problems/two-sum/)



Problem: Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Input: nums = [ 2, 7, 11, 15 ] , target = 9
Output: [ 0, 1 ]


You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.


```python

'''
Approach :
 - iterate through the list of numbers
 - take each number and check the next numbers sum with the current number to the target

Time Complexity :  O(n^2) where n(n-1)/2 sum of arithmetic progression, so O(n^2) i.e two nested loops
Space Complexity : O(1) as we are not using any extra space
'''
def findTwoSum1(nums, target):
  for i in range(len(nums) - 1):
    for j in range(i+1,len(nums)):
      value1 = nums[i]
      value2 = nums[j]
      if(value1+value2 == target):
        return {'indices': [i, j], 'values': [value1, value2]}
  else:
    return {'indices': [-1, -1], 'values': [-1, -1]}

```




```python

'''
Approach:
 - iterate over list and put each element in a dictionary with its index as value
 - for next elements, check different of target and element is already in dictionary

Time complexity: O(n) since we are iterating over list only once
Space complexity: O(n) since we are storing all elements in dictionary
'''
def findTwoSum3 (nums, target):
  value_to_index = {}
  for i,value2 in enumerate(nums):
    value1= target - value2
    if(value1 in value_to_index):
      return {'indices': [value_to_index[value1], i], 'values': [value1, value2]}
    value_to_index[value2] = i
  else:
    return {'indices': [-1, -1], 'values': [-1, -1]}

```




```python
'''
Approach :
- sort the list and filter out values above target [ stop until first item going above target]
- iterate through the list and find the pair that sums to target

Time complexity: O(n^2) since we have two nested loops
Space complexity: O(n) since we are creating a new list to store the filtered values
'''
def findTwoSum1(nums, target):
  sorted_nums = sorted(nums)
  filtered_nums = []

  for num in sorted_nums:
      if(num > target):
          break
      filtered_nums.append(num)

  for i in range(len(filtered_nums)):
    for j in range(i+1, len(filtered_nums)):
      value1 = filtered_nums[i]
      value2 = filtered_nums[j]
      if( value1 + value2 == target):
        # finding indices of original array
        index1 = nums.index(value1)
        # to handle duplication cases
        #  for strings,  rfind() method to get the last occurrence
        index2 = (len(nums) - nums[::-1].index(value2) - 1) if(value1 == value2)  else nums.index(value2)
        return {'indices': [index1, index2], 'values': [value1, value2]}
  else:
    return {'indices': [-1, -1], 'values': [-1, -1]}

```



 If array is sorted, we can use two pointers approach :


```python

'''
Approach: ( sorted array )
* have 2 pointers, one at start and one at end
* alter pointers and find sum of 2 numbers
* sum < target, move the start pointer, sum > target, move the end pointer

Time complexity:  O(n) for pointe
Space complexity: O(n) for sorted array
'''

def findTwoSum4(nums, target):
  # not doing inplace sort inorder to return original indices
  sorted_nums = sorted(nums)
  nums_length = len(nums)
  [prt1, prt2] = [0,nums_length-1]
  while(prt1<prt2):
    [value1, value2] = [sorted_nums[prt1] ,  sorted_nums[prt2]]
    sum_number = value1 + value2
    if sum_number == target:
      value1_index = nums.index(value1)
      # when duplicate items, don't say same item index
      value2_index = nums_length - nums[::-1].index(value2) - 1 if value1 == value2 else nums.index(value2)
      return {'indices': [value1_index, value2_index], 'values': [value1,value2]}
    elif sum_number > target:
      prt2 -= 1
    elif sum_number < target:
      prt1 += 1
  return {'indices': [-1, -1], 'values': [-1, -1]}

```




```python
'''
Two-Pointer Approach( sorted array )
have sorted indices from array!
Time: sorting + travesal => O(N logN) + O(N) =  O(N logN)
Space: sorted indices = O(N)
'''
def findTwoSumSorted(nums, target):
    sorted_indices = sorted(range(len(nums)), key=lambda i: nums[i])
    sorted_nums = [nums[i] for i in sorted_indices]

    left, right = 0, len(sorted_nums) - 1
    while left < right:
        current_sum = sorted_nums[left] + sorted_nums[right]
        if current_sum == target:
            # no need to handle duplicates
            return {
                'indices': [sorted_indices[left], sorted_indices[right]],
                    'values': [sorted_nums[left], sorted_nums[right]]
            }
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return {'indices': [-1, -1], 'values': [-1, -1]}

```



### Test


```python


def test_two_sum(func):
    two_sum_test_cases = [
        {
            'input': {'nums': [2, 7, 11, 15], 'target': 9},
            'expected': {'indices': [[0, 1]], 'values': [[2, 7]]}
        },
        {
            'input': {'nums': [1, 2, 3, 4, 5], 'target': 7},
            'expected': {'indices': [[1, 4], [2, 3]], 'values': [[2, 5], [3, 4]]}
        },
        {
            'input': {'nums': [3, 2, 4], 'target': 6},
            'expected': {'indices': [[1, 2]], 'values': [[2, 4]]}
        },
        # {
        #     'input': {'nums': [3, 3], 'target': 6},
        #     'expected': {'indices': [[0, 1]], 'values': [[3, 3]]}
        #     # [3,3] at [0, 0] , [0,0] index is wrong, if repetative elements comes in !
        # },
        # {
        #     'input': {'nums': [0, 1, 2, 0], 'target': 0},
        #     'expected': {'indices': [[0, 3]], 'values': [[0, 0]]}
        # },
        {
            'input': {'nums': [2, 5, 8, 11], 'target': 13},
            'expected': {'indices': [[0, 3], [1, 2]], 'values': [[2, 11], [5, 8]]}
        },
    ]

    for i, test_case in enumerate(two_sum_test_cases, 1):
        input_data = test_case['input']
        expected_output = test_case['expected']

        result = func(input_data['nums'], input_data['target'])

        # Check if the result matches expected indices and values
        assert result['indices'] in expected_output['indices'], f"Test case {i} failed: expected indices {expected_output['indices']}, got {result['indices']}"
        assert result['values'] in expected_output['values'], f"Test case {i} failed: expected values {expected_output['values']}, got {result['values']}"

    print(f"Test cases passed!")

```



Similar:

[[Three Sum or 3Sum]]

to check {

https://www.youtube.com/watch?v=cQ1Oz4ckceM


}
