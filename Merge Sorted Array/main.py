from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            pass
        if m == 0:
            nums1[m:] = nums2[m:]
        else:
            nums1[m:] = nums2
            nums1.sort()

if __name__ == "__main__":
    nums1 = list(map(int, input("Enter nums1 (comma-separated): ").split(',')))
    m = int(input("Enter the number of elements in nums1 to be merged (m): "))

    nums2 = list(map(int, input("Enter nums2 (comma-separated): ").split(',')))
    n = int(input("Enter the number of elements in nums2 (n): "))

    nums1 += [0] * (len(nums2) - len(nums1) + m + n - len(nums1))

    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    print("Merged nums1:", nums1)
