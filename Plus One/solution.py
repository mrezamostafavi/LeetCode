class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        digits = list(str(int("".join(digits)) + 1 ))
        for i in range(len(digits)):
            digits[i] = int(digits[i])
        return digits

if __name__ == "__main__":
    digits = list(map(int, input().split()))
    result = Solution().plusOne(digits)
    print(result)
