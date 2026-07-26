class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1 = 0
        pointer2 = 0

        k = 0

        last_seen = -10000
        
        while pointer2 < len(nums):
            if nums[pointer2] != last_seen:
                nums[pointer1] = nums[pointer2]
                pointer1 += 1
                k += 1
            
            last_seen = nums[pointer2]
            pointer2 += 1

        return k
            
            

            
