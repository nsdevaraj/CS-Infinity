

[# 5-stars reviews problem - Inside code](https://youtu.be/rXcNzfYHwcI?si=cI82GG4UqpDkNRSS)


### Problem Definition:
"We have a number of reviews on our course, some of them are 5-stars reviews, and we are searching for the minimum number of additional 5-stars reviews that we need to reach a certain percentage target. For example, if we have 16 reviews and 10 of them are 5-stars reviews, the actual percentage is 62.5%. If we want to reach, for example, 72%, we'd need to add at least 6 more 5-stars reviews, because after doing so, the percentage becomes 72.72%, which is acceptable."

### Solution Approaches:

1. **Brute Force Approach**
   - **Approach Explanation**:
     "Incrementally add 5-stars reviews until the target percentage is reached. Count the number of iterations required."
   - **Implementation**:
     ```python
     def min_reviews(nb_reviews, five_stars, target):
         count = 0
         while ((five_stars * 100) / nb_reviews) < target:
             count += 1
             nb_reviews += 1
             five_stars += 1
         return count
     ```
   - **Time Complexity**: \( O(n) \) in the worst case.
   - **Space Complexity**: \( O(1) \).

2. **Mathematical Approach**
   - **Approach Explanation**:
     "Derive an equation to calculate the minimum additional reviews (`x`) required mathematically. 
     
     Use the formula \( x \geq \lceil \frac{cb - 100a}{100 - c} \rceil \), where \( a \) is `five_stars`, \( b \) is `nb_reviews`, and \( c \) is `target`.
```python
import math

# Given variables
a = five_stars  # number of 5-stars reviews
b = nb_reviews  # total number of reviews
c = target      # target percentage of 5-stars reviews

# Calculate the minimum number of additional 5-stars reviews needed
x = math.ceil((c * b - 100 * a) / (100 - c))

```
     
   - **Implementation**:
     ```python
     import math
     
     def min_reviews(nb_reviews, five_stars, target):
         return math.ceil((target * nb_reviews - 100 * five_stars) / (100 - target))
     ```
   - **Time Complexity**: \( O(1) \).
   - **Space Complexity**: \( O(1) \).

### Problem Example:
"Suppose we have 16 reviews, 10 of which are 5-stars, and we want to reach a target of 72%:
- Initial percentage: \( \frac{10}{16} \times 100 = 62.5\% \).
- Additional 5-stars reviews needed using the first approach: 6 reviews.
- Using the second approach (mathematical): \( x = \lceil \frac{72 \times 16 - 100 \times 10}{100 - 72} \rceil = 6 \)."
```python
import math

# Given values for the example
five_stars = 10  # number of 5-stars reviews
nb_reviews = 16  # total number of reviews
target = 72      # target percentage of 5-stars reviews

# Calculate the minimum number of additional 5-stars reviews needed
x = math.ceil((target * nb_reviews - 100 * five_stars) / (100 - target))

print(f"x = {x}")

```
### Conclusion:
"These solutions provide different methods to solve the problem of determining the minimum number of additional 5-stars reviews needed to achieve a specified target percentage. The mathematical approach is more efficient and avoids the need for iterative checks, making it preferable for large input sizes or targets close to 100%."