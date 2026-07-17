class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        list = []

        for num in nums:

            if num in freq:
                freq[num] = freq[num] + 1
            
            else:
                freq[num] = 1

        for i in range(0, k):
            largest = max(freq, key=freq.get)

            list.append(largest)

            del freq[largest]
        
        return list