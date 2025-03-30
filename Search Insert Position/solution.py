from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        flag = 0
        if target in nums:
            return nums.index(target)
        else:
            for i in nums:
                if i >= target:
                    return nums.index(i)
                    flag = 1 
                    break
            if flag == 0:
                return len(nums)

if __name__ == "__main__":

    nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    target = int(input("Enter the target number: "))
    solution = Solution()
    result = solution.searchInsert(nums, target)
    
    print(f"The target should be inserted at index: {result}")
