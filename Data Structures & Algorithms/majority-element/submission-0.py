class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}

        for num in nums:
            if num in dict1:
                dict1[num] = dict1[num] + 1
            
            else:
                dict1[num] = 1
        
        target_value = max(dict1.values())

        for key, value in dict1.items():
             if value == target_value:
                 return key