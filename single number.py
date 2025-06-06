class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i)==1:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
#not the optimsied soln
