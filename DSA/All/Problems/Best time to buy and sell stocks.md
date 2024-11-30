
[LeetCode #121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)


Best Time to Buy and Sell Stock
•	Problem: You are given an array where the ith element is the price of a given stock on day i. You want to maximize your profit by choosing a day to buy and a different day to sell.
•	Example:
Input: [7, 1, 5, 3, 6, 4]
Output: 5 (Buy on day 2, sell on day 5)



The "Best Time to Buy and Sell Stock" problem can be solved using various approaches with different levels of efficiency. Here are three common approaches, ranging from brute force to optimized methods:

### 1. **Brute Force (O(n^2))**

This approach checks all possible pairs of buying and selling days to calculate the maximum profit.

- **Idea**: For each day, check all future days to calculate the profit from buying on that day and selling later.
- **Time Complexity**: O(n²) due to the nested loops.

```python
def maxProfit(prices):
    max_profit = 0
    n = len(prices)

    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5
```


```python

def best_time_to_buy_and_sell_stock1(prices):
    if len(prices) < 2:
        return 0
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit

```

### 2. **Optimized Approach using Single Pass (O(n))**

This approach uses a single loop to track the minimum price and the maximum profit.

- **Idea**: Traverse the list once while maintaining the lowest price so far and calculating the profit if sold on the current day. The maximum of all these profits is the answer.
- **Time Complexity**: O(n), where n is the number of days.

```python
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price  # Track the minimum price
        else:
            max_profit = max(max_profit, price - min_price)  # Calculate the profit

    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5
```


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to a very high value
        min_price = 10**9  
        # Initialize maximum profit to 0
        max_profit = 0

        # Iterate through each price in the list
        for price in prices:
            # Update the minimum price encountered so far
            min_price = min(min_price, price)
            # Calculate the potential profit and update max_profit if it's greater
            max_profit = max(max_profit, price - min_price)
        
        # Return the maximum profit found
        return max_profit

```

```python
def best_time_to_buy_and_sell_stock2(prices):

    if not prices:
        return 0

    max_profit = 0
    current_min_buy = prices[0]

    for i in range(1, len(prices)):
        current_min_buy = min(current_min_buy, prices[i])
        max_profit = max(max_profit, prices[i] - current_min_buy)
    return max_profit


```

### 3. **Kadane's Algorithm Variation (O(n))**

This approach is similar to Kadane's algorithm used for finding the maximum subarray sum and focuses on the changes in prices.

- **Idea**: Calculate the difference between consecutive days, then apply Kadane's algorithm to find the maximum sum of these differences (which corresponds to the maximum profit).
- **Time Complexity**: O(n), since the list is processed once.

```python
def maxProfit(prices):
    max_current = 0
    max_profit = 0

    for i in range(1, len(prices)):
        max_current = max(0, max_current + prices[i] - prices[i - 1])
        max_profit = max(max_profit, max_current)

    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5
```




### Summary:
- **Brute Force**: Simple but inefficient (O(n²)).
- **Single Pass**: Efficient, keeping track of the minimum price and maximum profit (O(n)).
- **Kadane’s Algorithm Variation**: Leverages maximum sum subarray logic, also O(n).

The optimized single-pass approach is generally preferred due to its simplicity and efficiency.


### Tests

```python


best_time_to_buy_and_sell_stock_test_cases = [
    # Case 1: General case with mixed prices
    {
        "name": "General Case",
        "input": [7, 1, 5, 3, 6, 4],
        "expected": 5,
    },  # Buy on day 2 (price = 1), sell on day 5 (price = 6)

    # Case 2: Prices only go down
    {
        "name": "Only Decreasing Prices",
        "input": [7, 6, 4, 3, 1],
        "expected": 0,
    },  # No transactions, profit = 0

    # Case 3: Prices only go up
    {
        "name": "Only Increasing Prices",
        "input": [1, 2, 3, 4, 5],
        "expected": 4,
    },  # Buy on day 1 (price = 1), sell on day 5 (price = 5)

    # Case 4: Single price point
    {
        "name": "Single Price Point",
        "input": [5],
        "expected": 0,
    },  # Cannot buy and sell

    # Case 5: Two price points, increasing
    {
        "name": "Two Prices Increasing",
        "input": [2, 4],
        "expected": 2,
    },  # Buy at 2, sell at 4

    # Case 6: Two price points, decreasing
    {
        "name": "Two Prices Decreasing",
        "input": [4, 2],
        "expected": 0,
    },  # No profit possible

    # Case 7: Mixed prices with a local minimum
    {
        "name": "Mixed with Local Minimum",
        "input": [3, 2, 6, 5, 0, 3],
        "expected": 4,
    },  # Buy at 2, sell at 6

    # Case 8: Prices with a large gap
    {
        "name": "Prices with Large Gap",
        "input": [1, 100, 2, 3, 98],
        "expected": 99,
    },  # Buy at 1, sell at 100

    # Case 9: All same prices
    {
        "name": "All Same Prices",
        "input": [3, 3, 3],
        "expected": 0,
    },  # No profit possible

    # Case 10: Performance case with large input
    {
        "name": "Large Input",
        "input": list(range(1, 10001)),  # Prices from 1 to 10000
        "expected": 9999,
    },  # Buy at 1, sell at 10000

    # Case 11: Empty input
    {
        "name": "Empty Input",
        "input": [],
        "expected": 0,
    }
]

def test_best_time_to_buy_and_sell_stock(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(
        best_time_to_buy_and_sell_stock_test_cases, 1
    ):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)
        assert (
            result == expected_output
        ), f"Test case {i} ({case_name}) failed: expected {expected_output}, got {result}"

    print("All test cases passed!")


```