class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        min_heap = []
        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        k_most_frequent_elements = []
        while min_heap:
            k_most_frequent_elements.append(heapq.heappop(min_heap)[1])
        
        return k_most_frequent_elements
