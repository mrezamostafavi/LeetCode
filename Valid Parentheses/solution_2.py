class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in dic:
                if stack:
                    last = stack.pop()
                    if dic[char] != last:
                        return False
                else:
                    stack.append('@')
            else:
                stack.append(char)

        if stack:
            return False
        else:
            return True

# Get input from the user
if __name__ == "__main__":
    s = input("Enter the string of brackets: ")
    solution = Solution()
    print(solution.isValid(s))
