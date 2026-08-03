class Solution(object):
    def groupAnagrams(self, strs):
        hashMap ={}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in hashMap:
                hashMap[sorted_string].append(string)
            else:
                    hashMap[sorted_string] = [string]
        return list(hashMap.values())