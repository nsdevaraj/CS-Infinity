

[FizzBuzz @GFG](https://www.geeksforgeeks.org/fizz-buzz-implementation/)




### 6. **Fizz Buzz**
- **Problem**: Write a program that prints the numbers from 1 to n. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
- **Example**:
  - Input: `n = 15`
  - Output: `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]`



```python

def fizz_buzz_1(num: int) -> list[str]:
    result_list: list[str] = []
    for i in range(1, num + 1):
        div_3, div_5 = i % 3 == 0, i % 5 == 0
        if div_3 and div_5:
            result_list.append("FizzBuzz")
        elif div_5:
            result_list.append("Buzz")
        elif div_3:
            result_list.append("Fizz")
        else:
            result_list.append(str(i))
    return result_list

```



```python

def fizz_buzz_2(num: int) -> list[str]:
    result_list: list[str] = [
        str(i) for i in range(1, num + 1)
    ]
    div_3_ptr, div_5_ptr, div_15_ptr = 3, 5, 15

    while (
        div_3_ptr <= num
        or div_5_ptr <= num
        or div_15_ptr <= num
    ):
        if div_3_ptr <= num:
            if result_list[div_3_ptr - 1] != "FizzBuzz":
                result_list[div_3_ptr - 1] = "Fizz"
            div_3_ptr += 3
        if div_5_ptr <= num:
            if result_list[div_5_ptr - 1] != "FizzBuzz":
                result_list[div_5_ptr - 1] = "Buzz"
            div_5_ptr += 5
        if div_15_ptr <= num:
            result_list[div_15_ptr - 1] = "FizzBuzz"
            div_15_ptr += 15
    return result_list


```





  ### 1. Basic Loop
  This is the most straightforward approach using a simple loop:

  ```python
  def fizz_buzz_basic(num: int) -> list[str]:
      result = []
      for i in range(1, num + 1):
          if i % 15 == 0:
              result.append("FizzBuzz")
          elif i % 3 == 0:
              result.append("Fizz")
          elif i % 5 == 0:
              result.append("Buzz")
          else:
              result.append(str(i))
      return result
  ```

  ### 2. List Comprehension and Ternary
  A more concise approach using list comprehension:

  ```python
  def fizz_buzz_comprehension(num: int) -> list[str]:
      return [
          "FizzBuzz" if i % 15 == 0 else
          "Fizz" if i % 3 == 0 else
          "Buzz" if i % 5 == 0 else
          str(i)
          for i in range(1, num + 1)
      ]
  ```


```python
i=1

while i <= 100:

print("FizzBuzz" if i%15 == 0 else "Buzz" if i%5 == 0 else "Fizz" if i%3 == 0 else str(i))

i+=1
```



#### lesser codes

```python

for i in range(1,101):print("FizzBuzz"*(i%15==0)or"Buzz"*(i%5==0)or"Fizz"*(i%3==0)or i)

```
  
```python
for i in range(1,101):print("Fizz"*(i%3==0)+"Buzz"*(i%5==0)or i)

```

```python
for i in range(1,101):print('Fizz'*(i%3<1)+'Buzz'*(i%5<1)or i)
```




  ### 3. Functional Programming with `map`
  Using `map` to apply a function to each number:

  ```python
 def fizzBuzz(n):
    result = []  

    # Hash map to store all FizzBuzz mappings.
    mp = {3: "Fizz", 5: "Buzz"}
    divisors = [3, 5] 

    for i in range(1, n + 1):
        res = ""  

        for d in divisors: 
          
            # If i is divisible by d,
            # then add the corresponding string mapping to current res
            if i % d == 0:
                res += mp[d]

        # Not divisible by 3 or 5, add the number
        if not res:
            res += str(i)

        # Append the current answer str to the result list
        result.append(res)

    return result  

if __name__ == "__main__":
    n = 10
    result = fizzBuzz(n)

    for str_ in result:
        print(str_, end=" ") 

  ```

  ### 4. Generator Function
  Using a generator to yield results one at a time:

  ```python
  def fizz_buzz_generator(num: int):
      for i in range(1, num + 1):
          if i % 15 == 0:
              yield "FizzBuzz"
          elif i % 3 == 0:
              yield "Fizz"
          elif i % 5 == 0:
              yield "Buzz"
          else:
              yield str(i)

  # To use the generator:
  # for value in fizz_buzz_generator(15):
  #     print(value)
  ```

  ### 5. Using a Dictionary for Lookup
  This approach uses a dictionary for cleaner mapping:

  ```python
  def fizz_buzz_dict(num: int) -> list[str]:
      output = []
      for i in range(1, num + 1):
          result = ""
          if i % 3 == 0:
              result += "Fizz"
          if i % 5 == 0:
              result += "Buzz"
          output.append(result or str(i))
      return output
  ```



#### without using modulo

```python

i = 1
div3_counter = 0
div5_counter = 0
while(i<101):
  div3_counter += 1
  div5_counter += 1
  
  ans = ''
  if(div3_counter == 3):
    ans += 'Fizz'
    div3_counter = 0
  if(div5_counter == 5):
    ans += 'Buzz'
    div5_counter = 0
  
  if(not ans):
    ans += str(i)
  
  print(ans)
  i+=1

```


#### Tests

```python


def test_fizz_buzz(func):
    print(f"Testing function: {func.__name__}")
    fizz_buzz_test_cases = [
        # Case 1: Basic case
        {
            "name": "Basic Case",
            "input": 15,
            "expected": [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        },
        # Case 2: Lower bound (n = 1)
        {
            "name": "Lower Bound",
            "input": 1,
            "expected": ["1"],
        },
        # Case 3: No multiples of 3 or 5 (n = 2)
        {
            "name": "No Multiples",
            "input": 2,
            "expected": ["1", "2"],
        },
        # Case 4: Only multiples of 3 (n = 3)
        {
            "name": "Only Multiples of 3",
            "input": 3,
            "expected": ["1", "2", "Fizz"],
        },
        # Case 5: Only multiples of 5 (n = 5)
        {
            "name": "Only Multiples of 5",
            "input": 5,
            "expected": ["1", "2", "Fizz", "4", "Buzz"],
        },
        # Case 6: All multiples of 3 and 5 (n = 15)
        {
            "name": "All Multiples of 3 and 5",
            "input": 30,
            "expected": [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
                "16",
                "17",
                "Fizz",
                "19",
                "Buzz",
                "Fizz",
                "22",
                "23",
                "Fizz",
                "Buzz",
                "26",
                "Fizz",
                "28",
                "29",
                "FizzBuzz",
            ],
        },
        # Case 7: n = 0 (edge case)
        {
            "name": "Edge Case Zero",
            "input": 0,
            "expected": [],
        },
        # Case 8: Larger n
        {
            "name": "Larger n",
            "input": 20,
            "expected": [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
                "16",
                "17",
                "Fizz",
                "19",
                "Buzz",
            ],
        },
        # Case 9: Negative value (n = -5)
        {
            "name": "Negative Value",
            "input": -5,
            "expected": [],
        },
        # Case 10: Large positive input (n = 100)
        {
            "name": "Large Positive Input",
            "input": 100,
            "expected": [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
                "16",
                "17",
                "Fizz",
                "19",
                "Buzz",
                "Fizz",
                "22",
                "23",
                "Fizz",
                "Buzz",
                "26",
                "Fizz",
                "28",
                "29",
                "FizzBuzz",
                "31",
                "32",
                "Fizz",
                "34",
                "Buzz",
                "Fizz",
                "37",
                "38",
                "Fizz",
                "Buzz",
                "41",
                "Fizz",
                "43",
                "44",
                "FizzBuzz",
                "46",
                "47",
                "Fizz",
                "49",
                "Buzz",
                "Fizz",
                "52",
                "53",
                "Fizz",
                "Buzz",
                "56",
                "Fizz",
                "58",
                "59",
                "FizzBuzz",
                "61",
                "62",
                "Fizz",
                "64",
                "Buzz",
                "Fizz",
                "67",
                "68",
                "Fizz",
                "Buzz",
                "71",
                "Fizz",
                "73",
                "74",
                "FizzBuzz",
                "76",
                "77",
                "Fizz",
                "79",
                "Buzz",
                "Fizz",
                "82",
                "83",
                "Fizz",
                "Buzz",
                "86",
                "Fizz",
                "88",
                "89",
                "FizzBuzz",
                "91",
                "92",
                "Fizz",
                "94",
                "Buzz",
                "Fizz",
                "97",
                "98",
                "Fizz",
                "Buzz",
            ],
        },
    ]

    for i, test_case in enumerate(fizz_buzz_test_cases, 1):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)
        assert (
            result == expected_result
        ), f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All applicable test cases passed!")



test_fizz_buzz(fizz_buzz_3)


```


