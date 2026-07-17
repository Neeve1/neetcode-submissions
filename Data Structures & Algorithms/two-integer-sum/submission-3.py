class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            match = target - nums[i]

            if match in seen:
                return [seen[match], i]

            else:
                seen[nums[i]] = i
        