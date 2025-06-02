# Valid Parentheses Problem
- Level: Easy

## Problem Description:

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Example 1:
Input: s = "()"
Output: true

### Example 2:
Input: s = "()[]{}"
Output: true

### Example 3:
Input: s = "(]"
Output: false

### Example 4:
Input: s = "([])"
Output: true

### Constraints:

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

## Problem Understanding:

The problem is about checking if a string made of brackets is valid. A valid string means every opening bracket has a matching closing bracket in the correct order. 
If we get a closing bracket and it matches with the last opened one, we remove it from our stack. If not, we return False. 
In the end, if the stack is empty, it means all brackets were matched properly, so we return True.

Using a dictionary (mapping) is a good approach here because we can easily check which opening bracket should match a closing one. 
We use a stack to store the opening brackets as we go. If we hit a closing bracket, we check if it matches the last one in the stack. 
If it doesn't match or the stack is empty when it shouldn't be, we return False. Otherwise, we keep going. If everything matches, the stack will be empty at the end, so we return True.

### Time Complexity
We iterate through each character in the input string exactly once.
For each character, we perform constant-time operations like checking a dictionary, pushing to or popping from a stack.
So the total time taken grows linearly with the size of the input string n.
- Result : **O(n)**

### Space Complexity

In the worst case, all characters in the string are opening brackets (e.g., "((({{{[[["), which will all be pushed onto the stack.
Therefore, in the worst case, the stack could hold up to n characters.
The dictionary used for bracket mapping has a fixed size (3 entries), so it uses constant space O(1).
- Overall, the space complexity is **O(n)** due to the stack.
