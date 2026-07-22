class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        storage = set(nums)

        for num in nums:
            streak = 0
            current = num
            
            while current in storage:
                streak = streak + 1
                current = current + 1

                res = max(res, streak)

        return res