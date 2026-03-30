class Solution:
    def reorganizeString(self, s: str) -> str:
        character_frequency = {}
        for char in s:
            if char in character_frequency:
                character_frequency[char] += 1
            else:
                character_frequency[char] = 1

        max_frequency_count = max(character_frequency.values())
        if max_frequency_count > (len(s) + 1) // 2:
            return ""
        
        heap = [[count, char] for char, count in character_frequency.items()]
        
        rearranged_string = []
        prev_count = 0
        prev_char = ''

        while heap:
            heap.sort(reverse=True)

            for i in range(len(heap)):
                count, char = heap[i]
                if char != prev_char:
                    rearranged_string.append(char)
                    heap[i][0] -= 1

                    prev_char = char

                    if heap[i][0] == 0:
                        heap.pop(i)
                    break
            else:
                return ""
        return ''.join(rearranged_string)