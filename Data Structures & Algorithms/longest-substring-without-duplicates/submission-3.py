class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return 0


        maxLen, L = 0, 0
        hashSet = set()

        for R in range(len(s)):
            while s[R] in hashSet:
                hashSet.remove(s[L])
                L += 1
            hashSet.add(s[R])
            maxLen = max(R-L+1, maxLen)
        return maxLen

        