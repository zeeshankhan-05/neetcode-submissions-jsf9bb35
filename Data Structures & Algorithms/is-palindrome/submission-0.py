class Solution:
    def isPalindrome(self, s: str) -> bool:
        letterS = "".join(l for l in s if l.isalnum())
        L, R = 0, len(letterS) - 1

        while L < R:
            if letterS[L].lower() == letterS[R].lower():
                L += 1
                R -= 1
            else:
                return False
        
        return True