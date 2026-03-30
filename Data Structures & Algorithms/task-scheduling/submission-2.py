class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = Counter(tasks)
        
        maxHeap = [-freq for freq in taskCounts.values()]
        heapq.heapify(maxHeap)

        cycles = 0
        queue = []

        while maxHeap or queue:
            cycles += 1
            if maxHeap:
                currentFreq = heapq.heappop(maxHeap)
                if currentFreq < -1:
                    queue.append((currentFreq + 1, cycles + n))

            if queue and queue[0][1] == cycles:
                heapq.heappush(maxHeap, queue.pop(0)[0])

        return cycles