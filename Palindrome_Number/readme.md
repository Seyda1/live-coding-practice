# Palindrome Number Problem

##  Problem Description:

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

**Example 1:**
- Input: x = 121
- Output: true
- Explanation: 121 reads as 121 from left to right and from right to left.

**Example 2:**
- Input: x = -121
- Output: false
- Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**
- Input: x = 10
- Output: false
- Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

**Constraints:**
- -231 <= x <= 231 - 1

## Problem Understanding:
 To check if a given input is a palindrome, we simply reverse the input and compare it to the original. If the reversed input is equal to the original, then the input is a palindrome.

 I encountered this kind of problem during a live coding session. After solving it using a straightforward approach, I was asked to rewrite the solution using fewer lines and with better time and space complexity. 
 This made it clear that interviewers not only expect you to solve the problem but also to proactively suggest optimizations when possible — even if the initial solution is correct.

 ### Time Complexity:
 
- n is the number of digits in the integer x.
- Converting the integer to a string: O(n)
- Reversing the string: O(n)
- Comparing the two strings: O(n)
- So overall: O(n)

 ### Space Complexity:
 
- A string of length n is created from the integer → O(n)
- A reversed copy of the string is also created → another O(n)
- So total auxiliary space: O(n)
