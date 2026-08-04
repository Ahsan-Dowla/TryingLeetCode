class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums = sorted(nums)        
        j = len(nums) - 1
        dif = nums[j] - nums[0]
        if dif:
            for i in range(1,dif):
                if nums[0]+i not in nums and nums[0]+i<nums[j]:
                    res.append(nums[0]+i)        
        return res