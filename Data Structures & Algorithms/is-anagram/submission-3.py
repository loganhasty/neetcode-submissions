class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        If anagrams are two strs with the same letters, regardless of order,
        we can to convert to a sorted dict and compare. They will then be easily
        comparable.
        '''
        return sorted(s) == sorted(t)