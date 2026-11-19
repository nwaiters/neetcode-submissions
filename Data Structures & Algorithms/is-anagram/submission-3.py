class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        str_s = {}
        str_t = {}

        for i in s:
            if i not in str_s:
                str_s[i] = 1
            else:
                str_s[i] += 1
        
        for j in t:
            if j not in str_t:
                str_t[j] = 1
            else:
                str_t[j] += 1

        
        if str_s == str_t:
            return True
        else:
            return False


        
        