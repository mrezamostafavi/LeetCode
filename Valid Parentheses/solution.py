class Solution:
    def isValid(self, s: str) -> bool:
        o = '([{'
        c = ')]}'
        z = 0
        open = 0
        idx = []
        while open >= 0:
            for i in s:
                if i in o:
                    idx.append(o.find(i)) 
                    open += 1
                else:
                    if open >> 0:
                        if idx[-1] == c.find(i):
                            idx.pop(-1)
                            open -= 1
                        else:
                            return False
                            z = 1
                            break
                    else:
                        return False
                        z = 1
                        break
            if z == 1:
                break                
            if z != 1 and open == 0:
                return True
                break

# Getting input from the user
if __name__ == "__main__":
    input_string = input("Enter the string of brackets: ")
    solution = Solution()
    result = solution.isValid(input_string)
    print(f"The input string is {'valid' if result else 'invalid'}.")
