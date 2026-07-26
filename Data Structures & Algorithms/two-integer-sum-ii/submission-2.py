class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1

        while True:
            sum = numbers[pointer1] + numbers[pointer2]

            if sum == target:
                return [pointer1 + 1, pointer2 + 1]
            
            elif sum > target:
                pointer2 -= 1
            
            else:
                pointer1 += 1