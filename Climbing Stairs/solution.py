class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if n <= 2:
            return n
        else:
            for i in range(3, n + 1):
                c = a + b
                a = b
                b = c
            return c

n = int(input())
solution = Solution()
print(solution.climbStairs(n))