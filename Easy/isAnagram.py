# https://leetcode.com/problems/valid-anagram/submissions/

class Solution:
    # Time: O(n log n) -> the time it takes to sort
    # Space: O(n) -> n length str where str is the longest string between s and t
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
