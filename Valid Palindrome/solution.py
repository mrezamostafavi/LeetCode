class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        if len(s) >> 1:
            while len(s) >> 1:
                if s[0] == s[-1]:
                    s = s[1:-1]
                else:
                    return False
            return len(s) <= 1
        else:
            return True

def main():
    input_string = input("Enter a string to check if it's a palindrome: ")
    solution = Solution()
    result = solution.isPalindrome(input_string)
    print(f"Is the string a palindrome? {result}")

if __name__ == "__main__":
    main()
