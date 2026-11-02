
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        q = collections.deque()
        res = []

        # Build the initial window
        for i in range(r + 1):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

        # Add maximum of initial window
        res.append(nums[q[0]])

        # Slide the window
        while r < len(nums) - 1:
            l += 1
            r += 1

            if q and q[0] < l:
                q.popleft()

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)
            res.append(nums[q[0]])

        return res
