

import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()  # stores indices

        # first window
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        
        res.append(nums[q[0]])

        # rest of the windows
        for i in range(k, len(nums)):
            # remove elements out of window
            if q and q[0] <= i - k:
                q.popleft()

            # maintain decreasing deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            res.append(nums[q[0]])

        return res


        
