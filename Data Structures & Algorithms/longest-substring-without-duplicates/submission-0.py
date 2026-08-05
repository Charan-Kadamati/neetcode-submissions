class Solution:
    def lengthOfLongestSubstring(self, s):
        i = 0
        maxlength = 0
        hashset = set()

        for j in range(len(s)):
            while s[j] in hashset:
                hashset.remove(s[i])
                i += 1

            hashset.add(s[j])
            maxlength = max(maxlength, j-i+1)
        return maxlength





        