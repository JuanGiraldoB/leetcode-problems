# https://leetcode.com/problems/valid-palindrome/submissions/

class Solution:
    # Time: O(n) -> lenght of s
    # Space: O(n) -> lenght of s
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:
            while left < right and not self.is_lowercase_letter(s[left]):
                left += 1

            while left < right and not self.is_lowercase_letter(s[right]):
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def is_lowercase_letter(self, char: str) -> bool:
        # could use s.isalnum()
        return (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 48 and ord(char) <= 57)


sl = Solution()

print(sl.isPalindrome("0A man, a plan, a canal: Panama0"))
