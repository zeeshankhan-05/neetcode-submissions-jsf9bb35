class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Compare both lengths of the strings to make sure that they are possible to be anagrams (must have the same length to be an anagram)
        
        # Count how many times a character appears in each string and store the letters and values into a hashmap
        # Compare both hashmaps and return true or false, depending on the result

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for char in range(len(s)):
            countS[s[char]] = 1 + countS.get(s[char], 0)
            countT[t[char]] = 1 + countT.get(t[char], 0)
        
        return countS == countT