class Solution:
    def twoSum(self, nums, target):
        c = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        c.append(i)
                        c.append(j)
                        return c

if __name__ == "__main__":
    print("Enter numbers separated by spaces:")
    nums = [int(x) for x in input().split()]
    print("Enter the target:")
    target = int(input())
    solution = Solution()
    result = solution.twoSum(nums, target)
    if result:
        print(result)
    else:
        print("No solution found.")