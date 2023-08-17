# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_numbers = {}

        for i, num in enumerate(nums):

            if num not in dict_numbers:
                dict_numbers[target - num] = i
            else:
                return [dict_numbers[num], i]
