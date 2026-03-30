class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)

            if key not in anagramMap:
                anagramMap[key] = [word]
            else:
                anagramMap[key].append(word)
        
        return list(anagramMap.values())