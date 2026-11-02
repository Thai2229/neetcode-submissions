class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []

        for num in nums:
            if num in count:
                count[num] += 1
            else: 
                count[num] = 1
        
        sorted_count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        for i, key in enumerate(sorted_count):
            ans.append(key)
            if i == k - 1:
                break
        
        return ans