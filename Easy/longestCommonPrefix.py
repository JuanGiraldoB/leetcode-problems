class Solution:
    # Time: O(n) -> n length of shortest word
    # Space: O(n) -> n length of shortest word
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sol = ""

        for val in zip(*strs):
            letter_set = set(val)

            if len(letter_set) == 1:
                sol += val[0]

        return sol
