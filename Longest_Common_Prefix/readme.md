# Longest Common Prefix
- Level: Easy
## Problem Description:

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

### Example 1:
- **Input:** strs = ["flower","flow","flight"]
- **Output:** "fl"
  
### Example 2:
- **Input:** strs = ["dog","racecar","car"]
- **Output:** ""
- **Explanation:** There is no common prefix among the input strings.

### Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters if it is non-empty.

## Problem Understanding:

### Solution 1

- Longest Common Prefix: The longest common prefix among the strings in the array cannot exceed the length of the shortest string in the array. This is because the prefix can only be as long as the shortest string.

Approach:

- First, identify the shortest string in the array, because the longest common prefix can be at most as long as the shortest string.

- Then, compare each character of the shortest string with the corresponding characters of the other strings in the array.

- As soon as a mismatch is found, stop and return the common prefix up to that point.

### Time Complexity For Solution 1:

- O(n) for finding the shortest string, and

- O(m * n) for comparing characters in the shortest string against all other strings,

)

🌟 The overall time complexity would indeed be O(m * n). 
The O(n) term for finding the shortest string is negligible compared to O(m * n), because the latter grows much faster as n (the number of strings) and m (the length of the shortest string) increase.
When you combine multiple time complexities, we look at the dominant term.

### Space Complexity For Solution 1:
1.) Auxiliary Space:
- You only need extra space to store the common prefix, which will be at most as long as the shortest string, so the space used for the prefix is O(m), where m is the length of the shortest string.

2.) No additional data structures are used that grow with the input size, other than the list strs which is given as input.

**Total Space Complexity:**
)

🌟 The overall space complexity is O(m), where m is the length of the shortest string in the list.
