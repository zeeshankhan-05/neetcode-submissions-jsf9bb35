class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1. Count the frequency of each character
        character_frequency = {}
        for char in s:
            character_frequency[char] = character_frequency.get(char, 0) + 1

        # 2. Check if the most frequent character <= (len(s) + 1) // 2
        max_frequency_count = max(character_frequency.values())
        if max_frequency_count > (len(s) + 1) // 2:
            return ""

        # 3. Use a max-heap (store negative counts for max behavior)
        heap = [(-count, char) for char, count in character_frequency.items()]
        heapq.heapify(heap)

        rearranged_string = []
        prev_count, prev_char = 0, ''

        # 4. Build the rearranged string
        while heap:
            count, char = heapq.heappop(heap)
            rearranged_string.append(char)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            count += 1

            prev_count, prev_char = count, char

        return ''.join(rearranged_string)