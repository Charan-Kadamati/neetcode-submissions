class Solution(object):
    def hasDuplicate(self, nums):
        myset = set()
        for x in nums:
            if x in myset:
                return True
            myset.add(x)
        return False
        