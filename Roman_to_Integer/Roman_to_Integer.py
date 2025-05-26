class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        pre = 0
        for char in reversed(s):
            if dict[char]>=pre:
                total = total+dict[char]
               
            else:
                total = total-dict[char]    
            pre = dict[char]
        return total
