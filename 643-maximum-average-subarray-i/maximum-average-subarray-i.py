class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = 0
        l = r = 0
        while r<k:
            sum_+=nums[r]
            r+=1
        max_sum = sum_
        while r<len(nums):
            sum_ -= nums[l]
            l += 1
            sum_ += nums[r]
            max_sum = max(max_sum,sum_)
            r+=1
        return max_sum/k