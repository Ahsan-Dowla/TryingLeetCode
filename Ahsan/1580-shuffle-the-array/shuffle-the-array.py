class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        r = n
        res = []
        while l<n and r<2*n:
            res.extend([nums[l],nums[r]])
            l += 1
            r += 1
        return res