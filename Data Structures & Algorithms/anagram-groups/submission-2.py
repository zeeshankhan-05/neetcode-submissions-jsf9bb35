class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            buffer = [0] * 26
            for char in string:
                buffer[ord(char) - ord("a")] += 1

            anagrams[tuple(buffer)].append(string)

        return list(anagrams.values())
            

        # 2. Create a list of each string that tracks the unique letters
        # that string has
        # 3. Compare lists together to see
        # {"[1, 0, 1, 0, 0, 1]" : act, cat}
