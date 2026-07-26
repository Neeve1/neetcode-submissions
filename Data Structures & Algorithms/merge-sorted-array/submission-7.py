class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer1 = m - 1          # Last valid element in nums1
        pointer2 = n - 1          # Last element in nums2
        position = m + n - 1      # Last position in nums1

        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[position] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[position] = nums2[pointer2]
                pointer2 -= 1

            position -= 1

        while pointer2 >= 0:
            nums1[position] = nums2[pointer2]
            pointer2 -= 1
            position -= 1