class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            buffer = [0] * 26
            for char in string:
                buffer[ord(char) - ord("a")] += 1

            anagrams[tuple(buffer)].append(string)

        return list(anagrams.values())