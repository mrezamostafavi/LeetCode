class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        z = 0
        output = []
        k = 0
        if k == len(nums) - 1:
            output.append(str(nums[k]))
        else:    
            for i in range(len(nums)-1):
                z = 0
                while nums[k] + 1 == nums[k+1]:
                    z += 1
                    k += 1
                    if k == len(nums) - 1:
                        y = str(nums[k-z]) + '->' + str(nums[k])
                        output.append(y)
                        break
                if k == len(nums) - 1:
                    break        
                if z != 0:
                    y = str(nums[k-z]) + '->' + str(nums[k])
                    output.append(y)
                else:
                    output.append(str(nums[k]))

                k += 1
                if k == len(nums) - 1:
                    output.append(str(nums[k]))
                    break

        return output

# Input from user
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    solution = Solution()
    print(solution.summaryRanges(nums))
