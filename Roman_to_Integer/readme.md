# Roman to Integer Problem

- Level: Easy 🟢

## Problem Description:

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |


For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. 
Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.
  
Given a roman numeral, convert it to an integer.

### Example 1:
- Input: s = "III"
- Output: 3
- Explanation: III = 3.

### Example 2:
- Input: s = "LVIII"
- Output: 58
- Explanation: L = 50, V= 5, III = 3.

### Example 3:
- Input: s = "MCMXCIV"
- Output: 1994
- Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

### Constraints:

- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

## Problem Understanding

First, you should understand the logic behind this calculation and identify a pattern so you can apply it to all numbers.
In the problem description, it is important to note:
**"Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not 'IIII'. Instead, the number four is written as 'IV'. Because the one comes before the five, we subtract it, making four."**
So, if we reverse the string, it becomes easier to compare characters. **Remember that:**
Roman numerals are structured so that subtraction happens only if a smaller value comes before a larger value. That is why we reverse the string in the algorithm.
To implement this, we need a mapping solution using a **dictionary (dict)**.
Try running the algorithm on an example (for instance, number 3) with pen and paper. You will see that if you do not reverse the string, the algorithm will not give the correct result.
That’s the key reason why we reverse it.

### Time Complexity

- The function iterates over the input string s exactly once (in reverse order).
- For each character, it performs:
- A dictionary lookup (dict[char]) — O(1) average time since dictionary lookups are constant time.
- A simple comparison and addition/subtraction — O(1).
- Therefore, the total time complexity is: **𝑂(𝑛)**

where 𝑛 is the length of the input string s.

### Space Complexity

- The dictionary dict is fixed in size (always 7 key-value pairs) — O(1) space.
- Variables like total and pre use constant space — O(1).
- No additional data structures grow with input size.
- Therefore, the total space complexity is: **𝑂(1)**

​



