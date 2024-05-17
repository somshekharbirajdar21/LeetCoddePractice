class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 == str2:
            return str1
        if str1+str2 != str2+str1:
            return ""
        if str1 > str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return self.gcdOfStrings(str1, str2[len(str1):])

print(Solution().gcdOfStrings("ABAB","ABABAB"))
        