class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #another approach is an array and using binary search to find where to insert
        #also nlogn 
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]