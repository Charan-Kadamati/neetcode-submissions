class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq = {}
        windowfreq = {}
        
        for character in s1:
            freq[character] = freq.get(character, 0) + 1

        left = 0

        for right in range(len(s2)):
            windowfreq[s2[right]] = windowfreq.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):

                windowfreq[s2[left]] -= 1

                if windowfreq[s2[left]] == 0:
                    del windowfreq[s2[left]]

                left += 1

            if windowfreq == freq:
                return True

        return False
        
        