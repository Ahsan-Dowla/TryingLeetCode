class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = 'aeiou'
        s = s.lower()

        max_vow = vow_count = 0
        l = r = 0
        while r<k:
            vow_count += 1 if s[r] in vow else 0
            r += 1
        max_vow = vow_count
        while r<len(s):
            if s[l] in vow:
                vow_count -= 1
            vow_count += 1 if s[r] in vow else 0
            max_vow = max(max_vow,vow_count)
            r += 1
            l += 1
        return max_vow