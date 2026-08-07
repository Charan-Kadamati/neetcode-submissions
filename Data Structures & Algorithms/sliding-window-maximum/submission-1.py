from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        res = []

        for i in range(len(nums)):

            # remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            
            # remove out of window
            if dq[0] <= i - k:
                dq.popleft()

            # add result
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res