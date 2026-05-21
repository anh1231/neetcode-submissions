class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if self.left and -self.left[0] > num:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if len(self.left) - len(self.right) > 1:
            pop = -heapq.heappop(self.left)
            heapq.heappush(self.right, pop)
        elif len(self.right) - len(self.left) > 1:
            pop = -heapq.heappop(self.right)
            heapq.heappush(self.left, pop)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return (-self.left[0])
        else:
            return self.right[0]