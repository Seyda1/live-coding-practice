# Two Sum Problem
- Level : Easy 🟢

## Problem Description:

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have **exactly one solution**, and you may not use the same element twice.
You can return the answer in any order.

### Example 1:
- **Input:** nums = [2,7,11,15], target = 9
- **Output:** [0,1]
- **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].
  
### Example 2:
- **Input:** nums = [3,2,4], target = 6
- **Output:** [1,2]

### Example 3:
- **Input:** nums = [3,3], target = 6
- **Output:** [0,1]

### Constraints:
- 2 <= nums.length <= 104
- 10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- -10<sup>9</sup> <= target <= 10<sup>9</sup>
- Only one valid answer exists.

## Problem Understanding:

I tend to approach problems as if I have no prior programming knowledge, treating them like mathematical problems. 
While I’m not certain it’s the most optimal approach, it helps me maintain simplicity in my thinking, as programming-based solutions often feel more complex. 
For this problem, I subtract each element in the array from the target and then check if the resulting value exists in the array. 
This method avoids the need to search the array twice for two elements that sum to the target, providing a more efficient solution.

## Time and Space Complexity

### Time Complexity
- **O(n)**: The algorithm iterates through the `nums` list once, performing a constant-time dictionary lookup and insert operation for each element. Therefore, the time complexity is **O(n)**, where **n** is the number of elements in the `nums` list.

### Space Complexity
- **O(n)**: The space complexity is determined by the dictionary `seen`, which stores the indices of the elements encountered during the iteration. In the worst case, the dictionary will store every element, so the space complexity is **O(n)**, where **n** is the number of elements in the `nums` list.


