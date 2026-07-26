class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = 0
        pointer2 = 0
        position = 0

        partnums1 = nums1[0:m]

        while pointer1 < m and pointer2 < len(nums2):

            if partnums1[pointer1] <= nums2[pointer2]:
                nums1[position] = partnums1[pointer1]
                pointer1 += 1
            
            else:
                nums1[position] = nums2[pointer2]
                pointer2 += 1
            
            position += 1

        while pointer1 < m:
            nums1[position] = partnums1[pointer1]
            pointer1 += 1
            position += 1
        
        while pointer2 < len(nums2):
            nums1[position] = nums2[pointer2]
            pointer2 += 1
            position += 1
        