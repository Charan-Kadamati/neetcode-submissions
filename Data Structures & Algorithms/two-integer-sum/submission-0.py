class Solution(object):
    def twoSum(self, nums, target):

        hashMap = {}

        for i in range(len(nums)):
            search = target - nums[i]

            if search in hashMap:
                return [hashMap[search], i]

            hashMap[nums[i]] = i