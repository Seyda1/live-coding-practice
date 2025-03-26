class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            elif target < nums[i]:
                return i
            
        return len(nums)
