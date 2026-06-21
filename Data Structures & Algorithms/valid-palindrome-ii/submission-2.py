class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 1. Create two pointers at both ends of the string
        # 2. Check the characters at the pointers are equal
        # If they are increment and decrement the respective pointers
        # If they aren't, create two substrings by stripping
        # one for deleting the left char, one for deleting the right char
        # bbd
        # bd
        # bb
        # 3. For the two substrings, check if either is a palindrome
        # Create a helper function for checking if it is a palindrome
        # If either substring is a palindrome, return True, else False

        def isPalindrome(string: str) -> bool:
            left, right = 0, len(string) - 1

            while left < right:
                if string[left] != string[right]:
                    return False

                left += 1
                right -= 1

            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                del_left = s[left + 1:right + 1]
                del_right = s[left:right]

                return isPalindrome(del_left) or isPalindrome(del_right)

        return True

        