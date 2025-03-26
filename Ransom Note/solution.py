class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x = len(ransomNote)
        y = len(magazine)
        z = 0
        if x > y:
            return False
        else:
            for i in range(x):
                for j in range(len(magazine)):
                    if ransomNote[i] == magazine[j]:
                        z += 1
                        magazine = magazine[:j] + magazine[j+1:]
                        break
            return z == x

if __name__ == "__main__":
    ransomNote = input("Enter the ransom note string: ")
    magazine = input("Enter the magazine string: ")
    solution = Solution()
    result = solution.canConstruct(ransomNote, magazine)
    print("Can construct ransom note:", result)
