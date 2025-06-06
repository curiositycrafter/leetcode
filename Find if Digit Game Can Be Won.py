class Solution(object):
    def canAliceWin(self, nums):
        s1=s2=0
        for i in nums:
            if i/10>0:
                s2+=i
            else:
                s1+=i
        if s1>s2 or s1<s2:
            return True
        else:
            return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        
