class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a) + int(b)
        c = list(str(c))

        for i in range(len(c)):

            if int(c[-1 - i]) == 2:
                if (-1 - i) * -1 >= len(c):
                    c[-1 - i] = 0
                    c.insert(0, 1)
                    break
                else:
                    c[-1 - i] = 0
                    c[-1 - i - 1] = int(c[-1 - i - 1]) + 1

            if int(c[-1 - i]) == 3:
                if (-1 - i) * -1 >= len(c):
                    c[-1 - i] = 1
                    c.insert(0, 1)
                    break
                else:
                    c[-1 - i] = 1
                    c[-1 - i - 1] = int(c[-1 - i - 1]) + 1

        c = [str(element) for element in c]
        c = "".join(c)
        return c

if __name__ == "__main__":
    a = input("Enter the first binary string: ")
    b = input("Enter the second binary string: ")
    solution = Solution()
    result = solution.addBinary(a, b)
    print("The sum of the binary strings is:", result)
