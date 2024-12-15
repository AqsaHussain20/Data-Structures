#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for i in s:
            if countS[i] != countT.get(i,0):
                return False

        return True

        