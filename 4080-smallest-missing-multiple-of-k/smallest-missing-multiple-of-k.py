class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        set_ = set(nums)
        x = k
        while x in set_:
            x += k
        return x
