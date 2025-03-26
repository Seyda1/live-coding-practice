# Search Insert Position
- Level : Easy

## Problem Description:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1:
- **Input:** nums = [1,3,5,6], target = 5
- **Output:** 2
  
### Example 2:
- **Input:** nums = [1,3,5,6], target = 2
- **Output:** 1

### Example 3:
- **Input:** nums = [1,3,5,6], target = 7
- **Output:** 4

### Constraints:
- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums contains distinct values sorted in ascending order.
- -104 <= target <= 104

## Problem Understanding:

This is a really easy problem. We will simply check if the target is in the array by searching for it. If it is found, we return its index.
If the number is not in the array, we will check where the target is smaller than an element in the array and return that element’s index. This is because if the target were in the array, that would be its position.
✨ However, this is not the best approach. There is a better way using binary search. It’s okay if we don’t find the best approach at first; we can always think about improving time complexity.

### Solution 1 Time Complexity (Linear Search):

- The function iterates through the nums list using a for loop.
- In the worst case, if target is larger than all elements in nums, the loop runs through the entire list of size n, making the complexity **O(n)**.
- In the best case, if target is found early (e.g., at the first index), the function returns immediately, making the best-case complexity **O(1)**.

### Solution 1 Space Complexity:

**- The algorithm only uses a constant amount of extra space:**
- A few variables (i, target, and nums) are used during the search, but these don't depend on the size of the input.
- It does not create any additional data structures that scale with the input size.
Thus, the space complexity of the linear search approach is **O(1)**.
---
### Solution 2 Time Complexity (Binary Search):

**Binary search repeatedly divides the array in half.**

- At each step, it eliminates half of the remaining elements.
- This results in a logarithmic reduction in the number of elements to search.
- 
**Number of iterations:**

- In each iteration, we halve the search space.
- If the array has n elements, the number of times we can halve it before reaching a single element is approximately **log₂(n)**.
- This gives a time complexity of **O(log n)**.

**Example:**
Let's say nums has 16 elements:
- 1st step → 16 elements → check middle → 8 elements left
- 2nd step → 8 elements → check middle → 4 elements left
- 3rd step → 4 elements → check middle → 2 elements left
- 4th step → 2 elements → check middle → 1 element left

Since log₂(16) = 4, the search takes at most 4 iterations.
For n elements, the worst-case time complexity is O(log n). 

### Solution 2 Space Complexity:

- Like the linear search approach, the binary search algorithm only uses a constant amount of extra space:
- It uses a few variables (left, right, mid), but these do not depend on the size of the input.
- No additional data structures (such as lists or dictionaries) are created that scale with input size.
Thus, the space complexity of the binary search approach is also O(1).
