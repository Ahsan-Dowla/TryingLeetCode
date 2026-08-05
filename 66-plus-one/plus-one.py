class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dig_int = int("".join(map(str, digits)))+1
        return list(map(int, str(dig_int)))