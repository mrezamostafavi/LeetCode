class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = list(t)
        z = 0
        c = []
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    del t[:j+1]
                    z += 1
                    c.append(j)
                    break
        return z == len(s)

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    sol = Solution()
    print(sol.isSubsequence(s, t))
