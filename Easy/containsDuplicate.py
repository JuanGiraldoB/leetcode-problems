# https://leetcode.com/problems/contains-duplicate/

class Solution:
    # Time: O(n) -> n length of nums
    # Space: O(n) -> n length of nums
    def containsDuplicate(self, nums: list[int]) -> bool:

        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)

        return False


print(ord("a"))
