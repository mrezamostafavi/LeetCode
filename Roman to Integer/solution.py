class Solution:
    def romanToInt(self, s: str) -> int:
        c = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        z = 0
        if 'IV' in s or 'IX' in s:
            z += -2
        if 'XL' in s or 'XC' in s:
            z += -20
        if 'CD' in s or 'CM' in s:
            z += -200

        for i in range(len(s)):
            z += c[s[i]]
        return z
