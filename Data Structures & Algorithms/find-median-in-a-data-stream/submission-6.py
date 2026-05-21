class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
        self.size = 0

    def addNum(self, num: int) -> None:
        if self.size <= 1:
            heapq.heappush(self.min_heap, num)
            self.size += 1
            return
        if self.min_heap[0] < num:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        if len(self.max_heap) - len(self.min_heap) > 1:
            popped = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped)
        elif len(self.min_heap) - len(self.max_heap) > 1:
            popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped)
        self.size += 1


    def findMedian(self) -> float:
        print(self.min_heap)
        print(self.max_heap)
        if not self.size % 2:
            if not self.max_heap:
                return (self.min_heap[0] + self.min_heap[1]) / 2
            else:
                return (self.min_heap[0] + -self.max_heap[0]) / 2
        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
        