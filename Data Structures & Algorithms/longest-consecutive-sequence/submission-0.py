class Solution(object):
    def longestConsecutive(self, nums):
        hashset = set(nums)
        maxcount = 0

        for i in hashset:          
            if i - 1 in hashset:
                continue
            count = 1
            nxt = i + 1
            while nxt in hashset:
                count += 1
                nxt += 1

            maxcount = max(maxcount, count)

        return maxcount