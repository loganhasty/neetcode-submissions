class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        If anagrams are two strs with the same letters, regardless of order,
        we can to convert to a sorted dict and compare. They will then be easily
        comparable.
        '''
        s1 = []
        s2 = []
        for letter in s:
            s1.append(letter)
        for letter in t:
            s2.append(letter)
        return sorted(s1) == sorted(s2)